---
title: "Gradle Kotlin DSL Unresolved Reference"
description: "Gradle Kotlin DSL script fails with unresolved reference errors."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gradle", "kotlin", "dsl", "unresolved", "buildscript"]
weight: 5
---

# Gradle Kotlin DSL — Unresolved Reference

This error occurs when a Gradle Kotlin DSL build script (`.gradle.kts`) references a class, method, or property that cannot be resolved. The Kotlin compiler cannot find the referenced symbol during script compilation.

## Common Causes

- Missing import statement for a class
- Plugin not applied before accessing its extensions
- API differences between Groovy DSL and Kotlin DSL
- Incorrect Kotlin DSL syntax
- Build script classpath missing a dependency

## How to Fix

### Add Missing Imports

```kotlin
// build.gradle.kts
import org.jetbrains.kotlin.gradle.dsl.KotlinJvmOptions

plugins {
    kotlin("jvm") version "1.9.0"
}
```

### Apply Plugin Before Accessing Extensions

```kotlin
plugins {
    kotlin("jvm") version "1.9.0"
    java
}

// Now access kotlin extension
kotlin {
    jvmToolchain(17)
}
```

### Fix Kotlin DSL Syntax

```kotlin
// Groovy DSL (incorrect in .kts)
// sourceCompatibility = JavaVersion.VERSION_17

// Kotlin DSL (correct)
java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}
```

### Add Plugin to Buildscript Classpath

```kotlin
buildscript {
    dependencies {
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.9.0")
    }
}
```

### Use Type-Safe Accessors

```kotlin
// Use the generated accessor
tasks.test {
    useJUnitPlatform()
}

// Instead of generic accessor
tasks.withType<Test> {
    useJUnitPlatform()
}
```

## Examples

```text
e: /home/user/build.gradle.kts:5: Unresolved reference: kotlin
e: /home/user/build.gradle.kts:10: Unresolved reference: jvmToolchain

e: /home/user/build.gradle.kts:15: Unresolved reference: testImplementation
```

## Related Errors

- [Gradle Configuration Error]({{< relref "/tools/gradle/gradle-configuration-error" >}}) — script evaluation failure
- [Gradle Plugin Error]({{< relref "/tools/gradle/gradle-plugin-error" >}}) — plugin not found
- [Gradle Version Error]({{< relref "/tools/gradle/gradle-version-error" >}}) — version compatibility issues
