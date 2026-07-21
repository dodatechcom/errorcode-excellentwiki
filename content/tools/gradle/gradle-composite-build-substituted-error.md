---
title: "Composite Build Substitution Error"
description: "Gradle composite build substitution fails because the substituted module cannot be resolved from the included build."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Composite Build Substitution Error

Composite builds allow one Gradle build to substitute dependencies from another build. A substitution error occurs when the included build does not produce the expected module.

## Common Causes

- The `using project` reference points to a subproject that does not exist
- The included build has a different group ID than the substituted module
- The replacement project uses a different module name
- The included build has not been evaluated yet when substitution runs

## How to Fix

1. Verify the included build structure:

```bash
# Check the included build has the referenced project
ls -la included-build/
ls -la included-build/library/
```

2. Ensure the substitution mapping is correct:

```groovy
// settings.gradle
includeBuild('included-build') {
    dependencySubstitution {
        substitute module('com.example:library') using project(':library')
    }
}
```

3. Match the group and version in the replacement project:

```groovy
// included-build/library/build.gradle
plugins {
    id 'java-library'
}

group = 'com.example'  // must match the substituted module's group
version = '1.0.0'
```

4. Run with substitution diagnostics:

```bash
./gradlew build --info 2>&1 | grep -i "substitut\|composite"
```

## Examples

```bash
# Error output
Included build '/path/to/included-build' does not contain a project ':wrong-name'
  Requested substitution: com.example:library using project ':library'
```

```groovy
// Correct composite build configuration
// settings.gradle (root)
includeBuild('libs/core') {
    dependencySubstitution {
        substitute module('com.example:core') using project(':')
    }
}
```

## Related Errors

- [Dependency Substitution Error]({{< relref "/tools/gradle/gradle-dependency-substitution-error" >}}) -- substitution mapping issues
- [Include Module Not Found]({{< relref "/tools/gradle/gradle-include-module-not-found" >}}) -- missing included modules
