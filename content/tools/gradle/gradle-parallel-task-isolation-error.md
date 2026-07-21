---
title: "Gradle Parallel Task Isolation Error"
description: "Gradle parallel execution fails because tasks share uncontrolled access to resources causing race conditions or file conflicts."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Parallel Task Isolation Error

Gradle parallel execution runs independent tasks simultaneously. An isolation error occurs when tasks write to the same files or directories without declaring the relationship, causing data corruption.

## Common Causes

- Multiple tasks write output to the same directory without declaring outputs
- A task reads files that another task is modifying concurrently
- Shared state directories like `build/generated` are accessed by multiple tasks
- Tasks in different subprojects write to a common output location

## How to Fix

1. Declare exclusive task outputs to prevent overlap:

```groovy
tasks.register('generateA') {
    outputs.dir('build/generated/a')
    doLast { /* generate A sources */ }
}

tasks.register('generateB') {
    outputs.dir('build/generated/b') // different directory
    doLast { /* generate B sources */ }
}
```

2. Use task dependencies to serialize conflicting tasks:

```groovy
tasks.named('generateB') {
    mustRunAfter tasks.named('generateA')
}
```

3. Enable parallel isolation in Gradle properties:

```properties
# gradle.properties
org.gradle.parallel=true
org.gradle.workers.max=4
```

4. Check for overlapping task outputs:

```bash
./gradlew build --parallel --info 2>&1 | grep -i "overlap\|conflict\|race"
```

## Examples

```bash
# Error output
Cannot use parallel builds with overlapping outputs:
  Tasks ':app:generateSources' and ':lib:generateSources' both output to
  build/generated/
```

```groovy
// Fixed with unique output directories
tasks.register('generateSources') {
    outputDirectory = layout.buildDirectory.dir("generated/${project.name}")
}
```

## Related Errors

- [Parallel Execution Error]({{< relref "/tools/gradle/gradle-parallel-execution-error" >}}) -- parallel build configuration
- [Build Cache Error]({{< relref "/tools/gradle/gradle-build-cache-error" >}}) -- cache isolation issues
