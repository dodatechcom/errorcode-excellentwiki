---
title: "Gradle Dependency Substitution Error"
description: "Gradle dependency substitution in composite builds fails because the replacement module cannot be resolved or mapped incorrectly."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Dependency Substitution Error

Gradle composite builds can substitute external dependencies with local project modules. A substitution error occurs when the mapping between external and local modules is misconfigured.

## Common Causes

- The substituted module coordinates do not match any published artifact
- The replacement project has not been included in `settings.gradle`
- The substitution rule references a version that does not exist
- A transitive dependency of the substituted module is also being substituted

## How to Fix

1. Verify the composite build includes the replacement project:

```groovy
// settings.gradle
includeBuild('local-libs') {
    dependencySubstitution {
        substitute module('com.example:library') using project(':library')
    }
}
```

2. Check that the replacement project publishes the expected module:

```groovy
// local-libs/library/build.gradle
plugins {
    id 'java-library'
    id 'maven-publish'
}

group = 'com.example'
version = '1.0.0-local'

java {
    withSourcesJar()
}
```

3. Run with substitution info to see what is being replaced:

```bash
./gradlew build --info 2>&1 | grep -i "substitut"
```

4. Verify the replaced module's transitive dependencies:

```bash
./gradlew dependencies --configuration runtimeClasspath | grep "com.example"
```

## Examples

```bash
# Error output
Could not resolve com.example:library:1.0.0
  Dependency 'com.example:library' was substituted from project ':library'
  but the project does not declare group 'com.example'
```

```groovy
// Correct substitution configuration
includeBuild('local-libs') {
    dependencySubstitution {
        substitute module('com.example:library') using project(':library')
        substitute module('com.example:utils') using project(':utils')
    }
}
```

## Related Errors

- [Composite Build Error]({{< relref "/tools/gradle/gradle-multi-project-build" >}}) -- composite build issues
- [Classpath Not Resolved]({{< relref "/tools/gradle/gradle-classpath-not-resolved" >}}) -- classpath resolution failures
