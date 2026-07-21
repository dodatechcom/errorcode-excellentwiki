---
title: "Circular Include Module Error"
description: "Gradle settings file references a circular include path causing the project structure to fail during initialization."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Circular Include Module Error

Gradle project structure is defined in `settings.gradle` using include statements. A circular include error occurs when module references create a cycle, preventing Gradle from determining the build order.

## Common Causes

- A module includes itself as a dependency or subproject
- Two modules depend on each other as composite builds
- The `settings.gradle` file contains duplicate include statements with conflicting paths
- A dynamic include evaluates to a circular reference

## How to Fix

1. Review the `settings.gradle` file for circular references:

```groovy
// settings.gradle
rootProject.name = 'my-project'
include 'app'
include 'lib-core'
include 'lib-utils'
// Verify no module references itself
```

2. Check composite build includes for circular substitutions:

```groovy
// settings.gradle
includeBuild('lib-a') {
    dependencySubstitution {
        substitute module('com.example:lib-b') using project(':')
    }
}
```

3. List the project structure to verify the hierarchy:

```bash
./gradlew projects
```

4. Remove or fix the circular dependency:

```groovy
// Instead of circular dependency, use an interface module
include 'api'
// 'api' contains shared interfaces
// 'lib-a' and 'lib-b' both depend on 'api'
```

## Examples

```bash
# Error output
Circular inclusion detected between ':app' and ':lib-a'
  :app includes :lib-a
  :lib-a includes :app
```

```groovy
// Fixed settings.gradle
rootProject.name = 'my-project'
include 'app', 'lib-core', 'lib-utils'
```

## Related Errors

- [Include Module Not Found]({{< relref "/tools/gradle/gradle-include-module-not-found" >}}) -- missing included modules
- [Multi Project Build]({{< relref "/tools/gradle/gradle-multi-project-build" >}}) -- multi-project configuration issues
