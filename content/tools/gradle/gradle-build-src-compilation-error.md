---
title: "Gradle BuildSrc Compilation Error"
description: "Gradle buildSrc directory contains build logic that fails to compile, preventing the main build from starting."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle BuildSrc Compilation Error

The `buildSrc` directory is compiled automatically before the main build. A compilation error here blocks all subsequent build tasks because shared build logic cannot be resolved.

## Common Causes

- A Kotlin or Groovy file in `buildSrc` has syntax errors
- Dependencies declared in `buildSrc/build.gradle` are missing from repositories
- The `buildSrc` code references classes not on its classpath
- A version conflict between `buildSrc` dependencies and the main build

## How to Fix

1. Compile `buildSrc` separately to isolate errors:

```bash
cd buildSrc && ../gradlew build
```

2. Verify the `buildSrc` build file has correct dependencies:

```groovy
// buildSrc/build.gradle
plugins {
    id 'groovy-gradle-plugin'
}

repositories {
    gradlePluginPortal()
    mavenCentral()
}

dependencies {
    implementation gradleApi()
    implementation localGroovy()
}
```

3. Check for Kotlin compilation errors in `buildSrc`:

```bash
./gradlew :buildSrc:compileKotlin --stacktrace
```

4. Temporarily exclude broken code to unblock the main build:

```kotlin
// buildSrc/src/main/kotlin/MyPlugin.kt
// Comment out broken code and add a TODO
// TODO: Fix compilation error
```

## Examples

```bash
# Error output
Could not compile build file 'buildSrc/build.gradle'.
  > buildSrc/src/main/kotlin/MyExtension.kt:10: Unresolved reference: Helper
```

```groovy
// buildSrc/build.gradle with Kotlin
plugins {
    id 'org.jetbrains.kotlin.jvm' version '1.9.22'
}

repositories {
    mavenCentral()
}

dependencies {
    implementation gradleApi()
    implementation 'org.jetbrains.kotlin:kotlin-stdlib'
}
```

## Related Errors

- [Build Script Error]({{< relref "/tools/gradle/gradle-build-script-error" >}}) -- main build script issues
- [Kotlin DSL Error]({{< relref "/tools/gradle/gradle-kotlin-dsl-error" >}}) -- Kotlin DSL problems
