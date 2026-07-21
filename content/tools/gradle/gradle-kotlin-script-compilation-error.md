---
title: "Gradle Kotlin Script Compilation Error"
description: "Gradle build script written in Kotlin DSL fails to compile due to syntax errors or unresolved references in the build file."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Kotlin Script Compilation Error

Kotlin DSL build scripts (`.gradle.kts`) are compiled before build execution. A compilation error prevents the build from starting and typically shows the failing line and error type.

## Common Causes

- Syntax errors such as missing parentheses or incorrect lambda syntax
- Unresolved references to plugins or extensions that are not applied
- Import statements reference classes not on the buildscript classpath
- Type mismatches in configuration blocks

## How to Fix

1. Verify the syntax of the failing script:

```kotlin
// build.gradle.kts -- ensure balanced braces and correct syntax
plugins {
    java
    kotlin("jvm") version "1.9.22"
}

group = "com.example"
version = "1.0.0"

repositories {
    mavenCentral()
}
```

2. Add missing imports:

```kotlin
import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

tasks.withType<KotlinCompile> {
    kotlinOptions {
        jvmTarget = "17"
    }
}
```

3. Run with stacktrace for detailed error info:

```bash
./gradlew help --stacktrace
```

4. Check for version conflicts in the buildscript:

```kotlin
// settings.gradle.kts
pluginManagement {
    repositories {
        gradlePluginPortal()
        mavenCentral()
    }
}
```

## Examples

```kotlin
// Error output
Script compilation errors:
  Line 15: Type mismatch: inferred type is String but Int was expected
    version = "1.0.0"  // should be: version = "1.0.0"
```

```kotlin
// Correct build.gradle.kts
plugins {
    java
    kotlin("jvm") version "1.9.22"
}

group = "com.example"
version = "1.0.0"

java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}
```

## Related Errors

- [Kotlin DSL Error]({{< relref "/tools/gradle/gradle-kotlin-dsl-error" >}}) -- Kotlin DSL specific issues
- [Build Script Compile]({{< relref "/tools/gradle/gradle-build-script-compile" >}}) -- build script compilation
