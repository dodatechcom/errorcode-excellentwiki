---
title: "KAPT Annotation Processing Error"
description: "Gradle KAPT annotation processor fails during compilation, preventing code generation for frameworks like Dagger or Room."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# KAPT Annotation Processing Error

KAPT (Kotlin Annotation Processing Tool) runs Java annotation processors during Kotlin compilation. A KAPT error means the processor cannot generate the required code, often breaking dependency injection or data mapping.

## Common Causes

- A generated source file has compilation errors due to invalid annotations
- The annotation processor version is incompatible with the Kotlin version
- Missing required annotation processor dependencies on the kapt classpath
- Incremental processing caches are stale or corrupted

## How to Fix

1. Ensure KAPT plugin is applied and processor dependencies use `kapt`:

```groovy
plugins {
    id 'org.jetbrains.kotlin.kapt'
}

dependencies {
    kapt 'com.google.dagger:dagger-compiler:2.48'
    implementation 'com.google.dagger:dagger:2.48'
}
```

2. Clean the build and disable incremental KAPT:

```groovy
kapt {
    incremental = false
    correctErrorTypes = true
}
```

3. Run with verbose output to find the failing processor:

```bash
./gradlew kaptDebugKotlin --info
```

4. Verify processor compatibility with your Kotlin version:

```kotlin
// Check kotlin version in build.gradle.kts
plugins {
    kotlin("jvm") version "1.9.22"
}
```

## Examples

```bash
# Error output
> Task :app:kaptDebugKotlin FAILED
e: Error occurred during annotation processing
  [Dagger/MissingBinding] Cannot provide Constructor
```

```groovy
// KAPT configuration with error reporting
kapt {
    correctErrorTypes = true
    arguments {
        arg("dagger.fastInit", "true")
    }
}
```

## Related Errors

- [Kotlin Compilation Error]({{< relref "/tools/gradle/gradle-kotlin-compilation-error" >}}) -- Kotlin compile failures
- [Annotation Processor Error]({{< relref "/tools/gradle/gradle-annotation-processor-error" >}}) -- Java annotation processor issues
