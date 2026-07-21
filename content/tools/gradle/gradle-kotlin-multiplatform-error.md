---
title: "Kotlin Multiplatform Build Error"
description: "Gradle Kotlin Multiplatform project fails to build due to target configuration errors or missing platform dependencies."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kotlin Multiplatform Build Error

Kotlin Multiplatform allows sharing code across JVM, JS, Native, and other targets. A build error occurs when target configurations are incompatible or platform-specific dependencies are missing.

## Common Causes

- A target like `iosArm64` requires macOS but the build runs on Linux
- Source set hierarchy is misconfigured with missing intermediate source sets
- A common dependency does not support all declared targets
- The Kotlin version is outdated and does not support a target

## How to Fix

1. Verify your build environment matches the declared targets:

```kotlin
// build.gradle.kts
kotlin {
    jvm()
    js(IR) {
        browser()
        nodejs()
    }
    // iosArm64 requires macOS -- skip on CI if needed
    if (System.getProperty("os.name").contains("Mac")) {
        iosArm64()
        iosX64()
    }
}
```

2. Set up the source set hierarchy correctly:

```kotlin
kotlin {
    sourceSets {
        val commonMain by getting {
            dependencies {
                implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3")
            }
        }
        val jvmMain by getting {
            dependencies {
                implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core-jvm:1.7.3")
            }
        }
    }
}
```

3. Check target compatibility for shared dependencies:

```kotlin
// Ensure the library supports all your targets
dependencies {
    commonMainImplementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.6.0")
}
```

4. Build with verbose output to find the failing target:

```bash
./gradlew build --info 2>&1 | grep -i "target\|platform\|FAILED"
```

## Examples

```bash
# Error output
> Failed to compute compileKotlinIosArm64 task
  Could not resolve kotlinx-coroutines-core-native
```

```kotlin
// Working multiplatform configuration
plugins {
    kotlin("multiplatform") version "1.9.22"
}

kotlin {
    jvm()
    js(IR) { browser() }
    sourceSets {
        val commonMain by getting
        val commonTest by getting
        val jvmMain by getting
        val jsMain by getting
    }
}
```

## Related Errors

- [Kotlin Compilation Error]({{< relref "/tools/gradle/gradle-kotlin-compilation-error" >}}) -- Kotlin compile failures
- [Kotlin DSL Error]({{< relref "/tools/gradle/gradle-kotlin-dsl-error" >}}) -- Kotlin DSL issues
