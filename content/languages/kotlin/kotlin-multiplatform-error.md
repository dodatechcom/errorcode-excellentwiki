---
title: "[Solution] Kotlin Multiplatform Source Set — expect/actual Mismatch"
description: "Fix Kotlin Multiplatform source set errors and expect/actual mismatch. Learn correct KMP configuration and platform-specific code."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 1025
---

## Common Causes

- Missing `actual` implementation for `expect` declaration in target platform
- Source set hierarchy misconfigured (commonMain vs platformMain)
- `expect`/`actual` signature mismatch (different parameter types)
- Wrong dependency scope (`implementation` vs `commonMainImplementation`)

```kotlin
// commonMain
expect fun platformName(): String
// androidMain — missing actual fun platformName(): String
```

## How to Fix

**1. Add actual implementations for all targets**

```kotlin
// commonMain
expect fun getPlatform(): String

// androidMain
actual fun getPlatform(): String = "Android"

// iosMain
actual fun getPlatform(): String = "iOS"
```

**2. Configure source sets correctly**

```kotlin
kotlin {
    jvm()
    iosX64()
    iosArm64()
    iosSimulatorArm64()

    sourceSets {
        val commonMain by getting
        val jvmMain by getting
        val iosMain by creating { dependsOn(commonMain) }
        val iosX64Main by getting { dependsOn(iosMain) }
        val iosArm64Main by getting { dependsOn(iosMain) }
    }
}
```

**3. Use correct dependency configuration**

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
                implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3")
            }
        }
    }
}
```

**4. Handle intermediate source sets**

```kotlin
kotlin {
    jvm()
    iosX64()
    iosArm64()

    // Shared iOS source set
    val iosMain by creating { dependsOn(commonMain.get()) }
    iosX64Main.get().dependsOn(iosMain)
    iosArm64Main.get().dependsOn(iosMain)
}
```

## Examples

```kotlin
// Example 1: expect/actual for platform API
// commonMain
expect class PlatformContext

// androidMain
actual class PlatformContext(val context: android.content.Context)

// iosMain
actual class PlatformContext

// Example 2: expect/actual with parameters
// commonMain
expect fun httpGet(url: String): String

// jvmMain
actual fun httpGet(url: String): String = java.net.URL(url).readText()

// iosMain
actual fun httpGet(url: String): String = /* NSURLSession call */

// Example 3: Source set dependencies
kotlin {
    jvm()
    sourceSets {
        val commonMain by getting {
            dependencies {
                api("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3")
                api("org.jetbrains.kotlinx:kotlinx-serialization-json:1.6.0")
            }
        }
    }
}
```

## Related Errors

- [Expect/actual error](expect-actual-error) — expect/actual mismatch
- [Gradle plugin error](kotlin-gradle-plugin-error) — plugin version
- [Compose compiler error](kotlin-compose-compiler-error) — compiler plugin
