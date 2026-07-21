---
title: "Gradle Missing Build File Error"
description: "Gradle cannot find a build.gradle or build.gradle.kts file in the expected project directory, preventing build initialization."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Missing Build File Error

Gradle expects a `build.gradle` or `build.gradle.kts` file in every included project directory. A missing build file error means the settings script references a subproject that lacks its build file.

## Common Causes

- A subproject directory exists but has no build file
- The `settings.gradle` includes a module that has not been set up yet
- A build file was accidentally deleted or moved
- The file extension is wrong (e.g., `.gradle.txt` instead of `.gradle`)

## How to Fix

1. Verify the project structure matches the settings file:

```bash
ls -la settings.gradle
ls -la app/build.gradle
ls -la core/build.gradle
```

2. Create a minimal build file for the missing project:

```groovy
// app/build.gradle -- minimal build file
plugins {
    id 'java-library'
}

group = 'com.example'
version = '1.0.0'
```

3. Check for file extension issues:

```bash
find . -name "build.gradle*" -type f
# Ensure files are named build.gradle or build.gradle.kts
```

4. Remove the subproject from settings if it is not needed:

```groovy
// settings.gradle
include 'app'
// include 'old-module' -- removed
```

## Examples

```bash
# Error output
Project with path ':app' could not be found in project ':my-project'.
  It was included in settings.gradle but no build.gradle file exists.
```

```groovy
// Minimal build.gradle for a new subproject
plugins {
    id 'java-library'
}

repositories {
    mavenCentral()
}

dependencies {
    api 'com.google.guava:guava:31.1-jre'
}
```

## Related Errors

- [Settings Gradle Missing]({{< relref "/tools/gradle/gradle-settings-gradle-missing" >}}) -- missing settings file
- [Include Module Not Found]({{< relref "/tools/gradle/gradle-include-module-not-found" >}}) -- module resolution issues
