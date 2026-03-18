---
title: '[tutorial] Taikai Introduction (based on ArchUnit)'
date: '2026-03-18'
updated: '2026-03-18'
author:
- Hsiang-Jen Li
- ' & DeepWiki'
tags:
- java
- policy-as-code
toc: true
lang: en
slug: tutorial-taikai-based-on-archunit
source_sha: 203576d54c22d45b689aaea656d16b444920ff46b100e4f8cf3a0fd3802d6984
origin_lang: zh-TW
permalink: tutorial-taikai-based-on-archunit.en/
translations:
  zh-TW: /zh-TW/tutorial-taikai-based-on-archunit/
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.

# 📌 Introduction

Taikai is a Java architecture-checking tool based on ArchUnit. It provides pre-built rules to check code architecture, supports creating shared Rules Profile for reuse across multiple projects, and automatically verifies via unit tests whether code meets architectural requirements.

<!-- more -->

# 🚀 Introducing Taikai

Taikai is a Java code architecture-checking library that can be used to inspect dependencies and layering between packages and classes, check for cyclic dependencies, and more. Taikai is based on [ArchUnit](https://github.com/TNG/archUnit), provides rules commonly needed by popular frameworks, and offers Rules Profile so architecture rules can be reused. The Rules currently provided include:

- Java Rules
- Logging Rules
- Test Rules
- Spring Rules
- Quarkus Rules

## Implementation

There are two types of repositories in total:
1. `shared-architecture-rules` that defines common rules (Rules Profile)
1. A repo for developing services

### Shared Architecture Rules

- A simple Rule has been implemented and can be found in [`shared-architecture-rules-0.1.0-SNAPSHOT`](https://github.com/hsiangjenli/shared-architecture-rules/releases/tag/0.1.0-SNAPSHOT)
- It imposes simple restrictions, such as disallowing the use of Deprecated APIs and ensuring a Method's params do not exceed 5

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

### Checking rules within the repo

Implementation details can be found at [quarkus-demo-architecture-rules](https://github.com/hsiangjenli/tiny-colab/tree/main/quarkus-demo-architecture-rules)

### Setting up `pom.xml`

> Because the shared Architecture Rules are only on GitHub and not published to Maven, remember to use jitpack, and make sure the tag of `shared-architecture-rules` matches the one on GitHub

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

### Example: code that violates the rules

```java
// ManyParameters.java

package com.hsiangjenli;

public class ManyParameters {
  public static void main(String a, String b, String c, String d, String e, String f) {}
}
```

### Test the Architecture

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

You can see the test fails because the method in `ManyParameters` has parameters exceeding the maximum value 5 set in `ArchitectureRules.BASE_JAVA_RULES`.

![image](https://hackmd.io/_uploads/rJIj69v9be.png)

# 🔁 Key takeaways

- Taikai is a Java architecture-checking tool based on ArchUnit, providing pre-built rules for frameworks like Java, Spring, and Quarkus
- Supports reusable Rules Profile so a shared rule set can be created and used across multiple projects
- Runs checks via unit tests; when rules are violated the tests fail, ensuring code conforms to architectural requirements

# 🔗 References

- DeepWiki
