---
title: '[tutorial] 介紹 sigstore 的模型簽章工具'
date: '2025-11-06'
updated: '2025-11-06'
author:
- Hsiang-Jen Li
- ' & DeepWiki'
tags:
- ai
- security
toc: true
lang: zh-TW
slug: tutorial-sigstore
permalink: zh-TW/tutorial-sigstore/
translations:
  en: /tutorial-sigstore.en/
---

# 📌 簡介

介紹 Sigstore 的模型簽章工具，並介紹其三層結構（Sigstore Bundle、DSSE Envelope、In‑Toto Statement）如何為機器學習模型提供完整性、真實性與透明度的簽章與驗證，並示範簡易的簽署與驗證指令。

<!-- more -->

# 🚀 介紹 `sigstore/model-transparency`

<!-- 目的是為了增加 ML 模型在供應鏈的安全性，讓模型可以被驗證完整性以及來源聲明 -->

- **模型完整性**：透過 Sigstore 對模型進行簽名，產生加密的雜湊值來保護模型的完整性
- **透明度**：任何人都可以透過 Sigstore 的透明日誌 Rekor 驗證模型的簽名
- **簡單使用**：與傳統的簽章機制相比更容易使用，並且提供無無金鑰簽名的選項

## 模型簽章

### 4 大痛點

- **完整性**：確保模型在發布的過程中沒有被篡改，是否還是原始的那一個
- **真實性**：可以模型是誰創造的，來源是可以被信任以及追溯的
- **安全性**：防範模型或資料集投毒以及未經授權的修改等攻擊
- **合規性**：證明模型在開發和部署的整個過程中，遵守了所有相關的規範（例如：沒有使用來路不明或未經授權的個人資料進行訓練）

### 支援簽章方法

<!-- https://github.com/sigstore/model-transparency/blob/36e01a9bd611436b847da633461afcc8f74891c4/README.md?plain=1#L34-L39 -->

- **無金鑰簽章**：使用 Sigstore 進行簽章，可免去複雜的金鑰生成、儲存、管理，並可以透過 Rekor 進行公開查驗
- **傳統金鑰與憑證簽章**：使用者需要自行管理，包含原始金鑰（Raw Key）、自簽憑證、憑證機構簽署的憑證
- **硬體裝置簽章**：支援透過 PKCS #11 標準介面，通常用於金融、政府等對安全與合規性要求極高的場域

### 運作流程

當機器學習模型準備部署時，系統會為模型本身、其內部所有檔案及 metadata 產生一組密碼學雜湊值，並寫入一份清單（manifest）中。這份清單記錄了每個檔案的路徑及其對應的雜湊值，完整描述了整個 ML Repo 的所有檔案組成。同時，此格式也兼容各種 meta data（例如：Model Card），以結構化的方式呈現模型的詳細資訊

### Sigstore 格式 & 簽署流程

![](https://github.com/sigstore/model-transparency/raw/main/docs/images/model-signing-format-diagram.png)

#### 總共分成三層

1. 最外層容器 Sigstore Bundle
1. 簡易簽章信封 Dead Simple Signing（DSSE）Envelope 
1. 實際的模型清單 In-Toto Statement

```python
# https://github.com/sigstore/model-transparency/blob/36e01a9bd611436b847da633461afcc8f74891c4/src/model_signing/_signing/sign_ec_key.py#L82-L127

class Signer(sigstore_pb.Signer):
    """Signer using an elliptic curve private key."""
    
    @override
    def sign(self, payload: signing.Payload) -> signing.Signature:
        raw_payload = json_format.MessageToJson(payload.statement.pb).encode(
            "utf-8"
        )

        raw_signature = intoto_pb.Signature(
            sig=base64.b64encode(
                self._private_key.sign(
                    sigstore_pb.pae(raw_payload),
                    ec.ECDSA(get_ec_key_hash(self._private_key.public_key())),
                )
            ),
            keyid="",
        )

        envelope = intoto_pb.Envelope(
            payload=base64.b64encode(raw_payload),
            payload_type=signing._IN_TOTO_JSON_PAYLOAD_TYPE,
            signatures=[raw_signature],
        )

        return sigstore_pb.Signature(
            bundle_pb.Bundle(
                media_type=sigstore_pb._BUNDLE_MEDIA_TYPE,
                verification_material=self._get_verification_material(),
                dsse_envelope=envelope,
            )
        )

```

- `raw_payload`：將 in-toto statement 轉換成 JSON 格式（將 Payload 序列化）
- `raw_signature`：[DSSE Signature](https://github.com/astral-sh/sigstore-models/blob/d0dad407dfe19a35aa24cc1c54054dc9d90ecd0e/src/sigstore_models/intoto.py#L12-L14) 
   - `sig`：數位簽章，一個獨立的密碼學證明值，用於確認 payload 的真實性與完整性，生成過程：對 payload 進行 PAE 編碼 --> 使用私鑰對 PAE 結果進行 ECDSA 運算，產生一個獨立的簽章值 --> 將這個簽章值用 Base64 編碼，方便在儲存在 JSON 內
   - `keyid`：密鑰標識符，本次簽名只使用一個密鑰，因此留空
- `envelope`：DSSE Envelope，包含：
   - `payload`：使用 Base64 編碼後的原始 payload
   - `payload_type`：告訴 Verifier 如何解析 payload
   - `signatures`：簽章後使用 Base64 的值
- `sigstore_pb.Signature`：包裝 Sigstore Bundle 的物件
   - `media_type`：標示 Sigstore bundle 的格式版本，確保 Verifier 知道如何解析這個 bundle
   - `verification_material`：包含驗證簽章所需的材料，根據簽章方法不同而有所不同
   - `dsse_envelope`：DSSE Envelope

### 驗證流程

1. 解析 Sigstore bundle
1. 驗證 DSSE 簽名的有效性
1. 提取 in-toto statement 中的 predicate
1. 根據 serialization 信息重新計算模型的雜湊值
1. 比對 resources 列表與實際計算的結果
1. 驗證全局摘要是否匹配

<!-- 使用 [Sigstore](https://www.sigstore.dev/) 進行簽章，Sigstore 是一個讓程式碼簽章變得透明且無需管理密碼金鑰材料的工具，但 model_signing 這樣工具同時也支援傳統的簽章方法，像是：公私鑰簽章、簽署憑證或是 PKCS #11 -->

### 實際操作

#### 下載一個 Model 當作簽章標的

```shell
git clone --depth=1 "https://huggingface.co/bert-base-uncased"

# 刪除 .git 目錄
rm -rf bert-base-uncased/.git 
```

#### 安裝 model_signing

```shell
uv add model_signing
```

#### 查看 model_signing 的 CLI

分成 `sign` 以及 `verify` 兩種

```shell
uv run model_signing --help  
```

```shell
Usage: model_signing [OPTIONS] COMMAND [ARGS]...

  ML model signing and verification.

  Use each subcommand's `--help` option for details on each mode.

Options:
  --version          Show the version and exit.
  --log-level LEVEL  Set the logging level. This can also be set via the
                     MODEL_SIGNING_LOG_LEVEL env var.  [default: INFO]
  -h, --help         Show this message and exit.

Commands:
  sign    Sign models.
  verify  Verify models.

  Check https://sigstore.github.io/model-transparency for documentation and
  more details.
```

#### 進行簽章

```shell
uv run model_signing sign bert-base-uncased --signature model.sig
```

![image](https://hackmd.io/_uploads/Hy4Ih-j1Wl.png)

![image](https://hackmd.io/_uploads/B188KC5yZg.png)

![image](https://hackmd.io/_uploads/HJM_t0qJZx.png)

接著就會出現 `Signing succeeded`

#### 簽章的結果

![image](https://hackmd.io/_uploads/ByIF9Rqk-g.png)


#### 驗證簽章（成功）

```shell
uv run model_signing verify bert-base-uncased --signature model.sig --identity "your_signing_email@mail.com" --identity_provider "oidc_provider"
```

**常見的 identity_provider 有：**

|identity_provider|   |
|-----------------|---|
|Google|`https://accounts.google.com`|
|GitHub|`https://github.com/login/oauth`|
|GitHub Actions|`https://token.actions.githubusercontent.com`|
|Microsoft|`https://login.microsoftonline.com`|

![image](https://hackmd.io/_uploads/S1PFtWs1Ze.png)

當初是使用 GitHub 當作 provider，所以在驗證的時候改成 Google 時就會驗證失敗

#### 驗證簽章（失敗）

嘗試去修改 `model.sig` 裡面的任一個字，把 `rawBytes` 欄位裡面的 `M` 刪掉，變成 `IIC0zCCAlmgAwIBAgIUH.....`

![image](https://hackmd.io/_uploads/SkvJnbj1-x.png)


# 🔁 重點回顧

- 介紹對模型簽章所要解決的 4 大痛點以及應用場域
- 詳細介紹 Sigstore 的格式分成三層（Sigstore Bundle、DSSE Envelope、In-Toto Statement）
- 介紹裡面程式碼的各樣參數所代表的意思
- 實際操作對模型進行簽署 + 驗證（成功、失敗）

# 🔗 參考資料

- [Sigstore Model Transparency 项目教程](https://blog.csdn.net/gitblog_00061/article/details/142242122)
- [From Theory to Practice: How MLOps Can Embed GenAI Transparency](https://lfaidata.foundation/blog/2025/07/29/from-theory-to-practice-how-mlops-can-embed-genai-transparency/)
- [Model authenticity and transparency with Sigstore](https://next.redhat.com/2025/04/10/model-authenticity-and-transparency-with-sigstore/)
- [PKCS #11 -標準方案簡介](https://cloud.ibm.com/docs/hs-crypto?topic=hs-crypto-pkcs11-intro&locale=zh-TW)
