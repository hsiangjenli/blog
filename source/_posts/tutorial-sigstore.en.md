---
title: '[tutorial] Introduction to sigstore''s model signing tool'
date: '2025-11-06'
updated: '2025-11-06'
author:
- Hsiang-Jen Li
- ' & DeepWiki'
tags:
- ai
- security
toc: true
lang: en
slug: tutorial-sigstore
source_sha: fa43507f77d7388d146338d2fe384a8b2899b1195dcadbfb3e12dfbf50dc82ef
origin_lang: zh-TW
permalink: tutorial-sigstore.en/
translations:
  zh-TW: /zh-TW/tutorial-sigstore/
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.

# 📌 Introduction

Introducing Sigstore's model signing tool and describing how its three-layer structure (Sigstore Bundle, DSSE Envelope, In‑Toto Statement) provides integrity, authenticity, and transparency for machine learning model signing and verification. Also demonstrates simple signing and verification commands.

<!-- more -->

# 🚀 Introducing `sigstore/model-transparency`

<!-- The goal is to increase the security of ML models in the supply chain, allowing model integrity and provenance claims to be verified -->

- **Model integrity**: Sign models with Sigstore to produce cryptographic hashes that protect model integrity
- **Transparency**: Anyone can verify model signatures via Sigstore's transparency log Rekor
- **Ease of use**: Easier to use than traditional signing mechanisms, and offers an option for keyless signing

## Model signing

### 4 main pain points

- **Integrity**: Ensure the model has not been tampered with during release and is still the original
- **Authenticity**: Be able to know who created the model; the source can be trusted and traced
- **Security**: Prevent attacks like model or dataset poisoning and unauthorized modifications
- **Compliance**: Prove the model adhered to relevant regulations during development and deployment (e.g., not trained on unknown or unauthorized personal data)

### Supported signing methods

<!-- https://github.com/sigstore/model-transparency/blob/36e01a9bd611436b847da633461afcc8f74891c4/README.md?plain=1#L34-L39 -->

- **Keyless signing**: Use Sigstore for signing, avoiding complex key generation, storage, and management, and enabling public audit via Rekor
- **Traditional keys & certificate signing**: Users manage keys themselves, including raw keys, self-signed certificates, or CA-signed certificates
- **Hardware device signing**: Supports signing via the PKCS #11 standard interface, commonly used in finance, government, and other high-security/compliance contexts

### Workflow

When an ML model is ready for deployment, the system generates cryptographic hashes for the model itself, all internal files, and metadata, and writes them into a manifest. This manifest records the path and corresponding hash for each file, fully describing the contents of the ML repo. The format is also compatible with various metadata (e.g., Model Card), presenting model details in a structured way.

### Sigstore format & signing process

![](https://github.com/sigstore/model-transparency/raw/main/docs/images/model-signing-format-diagram.png)

#### Divided into three layers

1. Outer container: Sigstore Bundle
1. DSSE Envelope (Dead Simple Signing)
1. Actual model manifest: In-Toto Statement

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

- `raw_payload`: Convert the in-toto statement to JSON (serialize the Payload)
- `raw_signature`: [DSSE Signature](https://github.com/astral-sh/sigstore-models/blob/d0dad407dfe19a35aa24cc1c54054dc9d90ecd0e/src/sigstore_models/intoto.py#L12-L14)
   - `sig`: Digital signature, an independent cryptographic proof used to confirm the authenticity and integrity of the payload. Generation process: PAE-encode the payload --> sign the PAE result with the private key using ECDSA to produce a signature --> Base64-encode the signature for storage in JSON
   - `keyid`: Key identifier. Only one key is used for this signature, so it's left empty
- `envelope`: DSSE Envelope, contains:
   - `payload`: The raw payload Base64-encoded
   - `payload_type`: Indicates how the Verifier should parse the payload
   - `signatures`: Signature values encoded in Base64
- `sigstore_pb.Signature`: Object wrapping the Sigstore Bundle
   - `media_type`: Indicates the Sigstore bundle format version so the Verifier knows how to parse the bundle
   - `verification_material`: Contains materials needed to verify the signature, varying by signing method
   - `dsse_envelope`: DSSE Envelope

### Verification process

1. Parse the Sigstore bundle
1. Verify the DSSE signature's validity
1. Extract the predicate from the in-toto statement
1. Recompute the model hashes according to the serialization information
1. Compare the resources list with the actual computed results
1. Verify the global digest matches

<!-- Use [Sigstore](https://www.sigstore.dev/) for signing. Sigstore makes code signing transparent and removes the need to manage key material, but tools like model_signing also support traditional signing methods such as public/private key signing, signing certificates, or PKCS #11 -->

### Hands-on

#### Download a model to sign

```shell
git clone --depth=1 "https://huggingface.co/bert-base-uncased"

# Remove .git directory
rm -rf bert-base-uncased/.git 
```

#### Install model_signing

```shell
uv add model_signing
```

#### View model_signing CLI

There are two modes: `sign` and `verify`

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

#### Perform signing

```shell
uv run model_signing sign bert-base-uncased --signature model.sig
```

![image](https://hackmd.io/_uploads/Hy4Ih-j1Wl.png)

![image](https://hackmd.io/_uploads/B188KC5yZg.png)

![image](https://hackmd.io/_uploads/HJM_t0qJZx.png)

You will then see `Signing succeeded`

#### Signing result

![image](https://hackmd.io/_uploads/ByIF9Rqk-g.png)


#### Verify signature (success)

```shell
uv run model_signing verify bert-base-uncased --signature model.sig --identity "your_signing_email@mail.com" --identity_provider "oidc_provider"
```

**Common identity_providers include:**

|identity_provider|   |
|-----------------|---|
|Google|`https://accounts.google.com`|
|GitHub|`https://github.com/login/oauth`|
|GitHub Actions|`https://token.actions.githubusercontent.com`|
|Microsoft|`https://login.microsoftonline.com`|

![image](https://hackmd.io/_uploads/S1PFtWs1Ze.png)

The signing originally used GitHub as the provider, so verification will fail if you change it to Google.

#### Verify signature (failure)

Try modifying any character inside `model.sig`, for example delete the `M` in the `rawBytes` field so it becomes `IIC0zCCAlmgAwIBAgIUH.....`

![image](https://hackmd.io/_uploads/SkvJnbj1-x.png)


# 🔁 Recap

- Introduced the 4 main pain points and application contexts that model signing aims to solve
- Detailed Sigstore's three-layer format (Sigstore Bundle, DSSE Envelope, In-Toto Statement)
- Explained the meaning of various parameters in the code examples
- Performed actual model signing + verification (success and failure)

# 🔗 References

- [Sigstore Model Transparency 项目教程](https://blog.csdn.net/gitblog_00061/article/details/142242122)
- [From Theory to Practice: How MLOps Can Embed GenAI Transparency](https://lfaidata.foundation/blog/2025/07/29/from-theory-to-practice-how-mlops-can-embed-genai-transparency/)
- [Model authenticity and transparency with Sigstore](https://next.redhat.com/2025/04/10/model-authenticity-and-transparency-with-sigstore/)
- [PKCS #11 -標準方案簡介](https://cloud.ibm.com/docs/hs-crypto?topic=hs-crypto-pkcs11-intro&locale=zh-TW)
