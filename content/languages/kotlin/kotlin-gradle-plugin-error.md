---
title: "[Solution] Kotlin Gradle Plugin Version Mismatch and Multiplatform Config"
description: "Fix Kotlin Gradle plugin version mismatch. Learn correct plugin setup, Kotlin version alignment, and multiplatform configuration."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 1024
---

## Common Causes

- Kotlin Gradle plugin version mismatch with `kotlin-stdlib`
- Using `kotlin("jvm")` and `kotlin("android")` together incorrectly
- Kotlin version incompatible with Compose compiler or other plugins
- Missing `kotlin-multiplatform` plugin in KMP projects

```kotlin
// Version mismatch
plugins {
    kotlin("jvm") version "1.9.0"  // Plugin version
}
dependencies {
    implementation("org.jetbrains.kotlin:kotlin-stdlib:1.8.0")  // Different!
}
```

## How to Fix

**1. Align Kotlin versions across plugin and dependencies**

```kotlin
// build.gradle.kts
plugins {
    kotlin("jvm") version "1.9.22"  // Matches stdlib
}

// buildSrc for version management
// buildSrc/src/main/kotlin/Dependencies.kt
object Versions {
    const val kotlin = "1.9.22"
}
```

**2. Use version catalog for consistency**

```kotlin
// libs.versions.toml
[versions]
kotlin = "1.9.22"

[plugins]
kotlin-jvm = { id = "org.jetbrains.kotlin.jvm", version.ref = "kotlin" }

// build.gradle.kts
plugins {
    alias(libs.plugins.kotlin.jvm)
}
```

**3. Check Compose compiler compatibility**

```kotlin
// Compose compiler requires specific Kotlin version
// build.gradle.kts
composeCompiler {
    kotlinCompilerExtensionVersion = "1.5.8"  // Matches Kotlin 1.9.22
}
```

**4. Use apply false for root project**

```kotlin
// Root build.gradle.kts
plugins {
    kotlin("jvm") version "1.9.22" apply false
}

// Module build.gradle.kts
plugins {
    kotlin("jvm")  // No version needed, uses root
}
```

## Examples

```kotlin
// Example 1: Multi-module consistent Kotlin
// root build.gradle.kts
plugins {
    kotlin("jvm") version "1.9.22" apply false
    kotlin("android") version "1.9.22" apply false
}

// Example 2: Kotlin version in buildSrc
buildSrc {
    dependencies {
        implementation("org.jetbrains.kotlin:kotlin-gradle-plugin:1.9.22")
    }
}

// Example 3: Check version at build time
tasks.withType<org.jetbrains.kotlin.gradle.tasks.KotlinCompile> {
    println("Kotlin version: ${kotlinVersion}")
}
```

## Related Errors

- [Multiplatform error](kotlin-multiplatform-error) — KMP source sets
- [Compose compiler error](kotlin-compose-compiler-error) — compiler plugin
- [Android bundle error](kotlin-android-bundle-error) — build variant
