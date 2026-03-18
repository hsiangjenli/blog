---
title: '[tutorial] Taikai 介紹（based on ArchUnit）'
date: '2026-03-18'
updated: '2026-03-18'
author:
- Hsiang-Jen Li
- ' & DeepWiki'
tags:
- java
- policy-as-code
toc: true
lang: zh-TW
slug: tutorial-taikai-based-on-archunit
permalink: zh-TW/tutorial-taikai-based-on-archunit/
translations:
  en: /tutorial-taikai-based-on-archunit.en/
---

# 📌 簡介

Taikai 是基於 ArchUnit 的 Java 架構檢查工具，提供預建規則檢查程式碼架構，支援建立共用 Rules Profile 在多專案間重複使用，透過單元測試自動驗證程式碼是否符合架構要求

<!-- more -->

# 🚀 介紹 Taikai

Taikai 是一個 Java 程式碼架構檢查函式庫，可以用來檢查套件和類別之間的依賴關係、層級、檢查循環依賴等等。Taikai 是 Based on [ArchUnit](https://github.com/TNG/archUnit)，提供常見框架會需要檢查的規則，並且提供 Rules Profile 讓架構規則可以被重複使用，目前提供的 Rules 有以下幾種：

- Java Rules
- Logging Rules
- Test Rules
- Spring Rules
- Quarkus Rules

## 實作

總共會有兩種 Repo，分別為：
1. 定義通用規則（Rules Profile）的 `shared-architecture-rules`
1. 開發服務用的 Repo

### 共用的 Architecture Rules

- 目前有實作一份簡單的 Rule，可以在 [`shared-architecture-rules-0.1.0-SNAPSHOT`](https://github.com/hsiangjenli/shared-architecture-rules/releases/tag/0.1.0-SNAPSHOT) 找到
- 簡單做些限制，像是禁止使用 Deprecated 的 API 以及 Method 的 Params 不能超過 5 個

```java
package com.hsiangjenli;

import com.enofex.taikai.configures.Customizer;
import com.enofex.taikai.java.JavaConfigurer;

public final class ArchitectureRules {

  static int MAX_METHOD_PARAMETERS = 5;

  // Basic Java Rules
  public static final Customizer<JavaConfigurer> BASE_JAVA_RULES =
      java -> {
        java.noUsageOfDeprecatedAPIs().methodsShouldNotExceedMaxParameters(MAX_METHOD_PARAMETERS);
      };
}
```

### Repo 內檢查是否符合規則

實作細節可參考 [quarkus-demo-architecture-rules](https://github.com/hsiangjenli/tiny-colab/tree/main/quarkus-demo-architecture-rules)

### 設置 `pom.xml`

> 因為共用 Architecture Rules 只有放在 GitHub 上，並沒有 publish 到 Maven 上，所以要記得使用 jitpack，並且注意 `shared-architecture-rules` 的 tag 是否與 GitHub 上的相符

```xml
<repositories>
    <repository>
        <id>jitpack.io</id>
        <url>https://jitpack.io</url>
    </repository>
</repositories>

<dependencies>
    <dependency>
        <groupId>com.github.hsiangjenli</groupId>
        <artifactId>shared-architecture-rules</artifactId>
        <version>0.1.0-SNAPSHOT</version>
    </dependency>
</dependencies>
```

### 撰寫不符合規則的程式碼

```java
// ManyParameters.java

package com.hsiangjenli;

public class ManyParameters {
  public static void main(String a, String b, String c, String d, String e, String f) {}
}
```

### 測試 Architecture

```java
// ArchitectureTest.java

package com.hsiangjenli;

import com.enofex.taikai.Taikai;
import org.junit.jupiter.api.Test;

public class ArchitectureTest {

  @Test
  void shouldValidateJavaRules() {
    Taikai.builder().namespace("com.hsiangjenli").java(ArchitectureRules.BASE_JAVA_RULES).build().checkAll();
  }
}
```

```shell
mvn test
```

可以看到測試出現錯誤，因為 `ManyParameters` 的 method 中的參數超過 `ArchitectureRules.BASE_JAVA_RULES` 中設置的最大值 5 

![image](https://hackmd.io/_uploads/rJIj69v9be.png)

# 🔁 重點回顧

- Taikai 是基於 ArchUnit 的 Java 架構檢查工具，提供 Java、Spring、Quarkus 等框架的預建規則
- 支援 Rules Profile 重複使用，可建立共用規則庫在多專案間共享架構標準
- 透過單元測試執行檢查，違反規則時測試失敗，確保程式碼符合架構要求

# 🔗 參考資料

- DeepWiki
