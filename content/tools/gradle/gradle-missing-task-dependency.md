---
title: "Gradle Missing Task Dependency Error"
description: "Gradle task fails because it references another task that does not exist in the build graph or the dependency was removed."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Missing Task Dependency Error

Gradle tasks can depend on other tasks using `dependsOn` or `mustRunAfter`. This error occurs when a task references another task that does not exist in the project.

## Common Causes

- A plugin that defines the dependency task is not applied
- The task was renamed or removed from the build script
- A multi-project build references a task from a subproject that does not define it
- Conditional task registration skips creating the dependency task

## How to Fix

1. List all available tasks to verify the dependency name:

```bash
./gradlew tasks --all | grep "taskname"
```

2. Check the task registration for typos:

```groovy
// Incorrect -- task name typo
tasks.named('compileJava').configure {
    dependsOn 'genereteSources' // should be 'generateSources'
}

// Fixed
tasks.named('compileJava').configure {
    dependsOn 'generateSources'
}
```

3. Use lazy task references to avoid ordering issues:

```groovy
tasks.named('compileJava') {
    dependsOn tasks.named('generateSources')
}
```

4. Ensure the dependency plugin is applied:

```groovy
// The generateSources task requires this plugin
plugins {
    id 'java'
    id 'my-custom-plugin' // defines generateSources
}
```

## Examples

```bash
# Error output
Could not determine the dependencies of task ':app:compileJava'.
> Task with path 'generateSources' not found in project ':app'.
```

```groovy
// Conditional task dependency
tasks.named('compileJava') {
    if (project.hasProperty('withGenerated')) {
        dependsOn 'generateSources'
    }
}
```

## Related Errors

- [Task Not Found]({{< relref "/tools/gradle/gradle-task-not-found" >}}) -- missing task references
- [Task Dependency Cycle]({{< relref "/tools/gradle/gradle-task-dependency-cycle" >}}) -- circular dependencies
