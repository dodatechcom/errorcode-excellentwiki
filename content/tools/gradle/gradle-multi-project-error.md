---
title: "Gradle Multi-Project Configuration Error"
description: "Gradle multi-project build fails during configuration phase."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Gradle Multi-Project Configuration Error

This error occurs when a Gradle multi-project build fails during the configuration phase. Issues with `settings.gradle`, subproject builds, or cross-project references cause the entire build to fail.

## Common Causes

- Missing subproject in `settings.gradle`
- Circular dependency between subprojects
- Subproject build script references parent-only dependencies
- Incorrect `allprojects` or `subprojects` block
- Missing `include` for a new module

## How to Fix

### Verify settings.gradle Includes

```groovy
// settings.gradle
rootProject.name = 'my-app'
include 'app', 'core', 'data', 'domain'
```

### Fix Cross-Project Dependencies

```groovy
// subproject build.gradle
dependencies {
    implementation project(':core')  // correct
    // implementation project(':nonexistent')  // error
}
```

### Use allprojects Correctly

```groovy
allprojects {
    repositories {
        mavenCentral()
    }
}

subprojects {
    apply plugin: 'java'
}
```

### Validate Project Structure

```bash
./gradlew projects
```

### Fix Circular Dependencies

```groovy
// Use API/implementation to break cycles
// module-a/build.gradle
dependencies {
    api project(':module-b')
}

// module-b/build.gradle
dependencies {
    implementation project(':module-c')  // not :module-a
}
```

### Configure Composite Builds

```groovy
// settings.gradle
includeBuild('plugin-project') {
    dependencySubstitution {
        substitute module('com.example:plugin') using project(':')
    }
}
```

## Examples

```text
* What went wrong:
  Project with path ':core' could not be found in project ':app'.

* What went wrong:
  Circular dependency between the following tasks:
  - ':app:compileJava'
    - ':core:classes'
      - ':app:classes'
```

## Related Errors

- [Gradle Configuration Error]({{< relref "/tools/gradle/gradle-configuration-error" >}}) — script evaluation failure
- [Gradle Dependency Error]({{< relref "/tools/gradle/gradle-dependency-error" >}}) — dependency resolution failure
- [Gradle Task Error]({{< relref "/tools/gradle/gradle-task-error" >}}) — task execution failure
