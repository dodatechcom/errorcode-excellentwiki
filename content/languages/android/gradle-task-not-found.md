---
title: "Gradle Task Not Found"
description: "Fix Gradle task not found errors when running custom build tasks"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
The requested Gradle task does not exist or is not recognized

## Common Causes

- Typo in task name
- Task not defined in current module
- Plugin providing the task is not applied
- Using incorrect Gradle command syntax

## Fixes

- Run ./gradlew tasks to list available tasks
- Verify plugin application in build.gradle
- Check task name spelling and module scope
- Use full qualified task path like :app:assembleDebug

## Code Example

```kotlin
# List all tasks
./gradlew tasks --all

# Run a specific task
./gradlew :app:assembleDebug
```

# Find what tasks are available
./gradlew tasks --group=build
# Apply missing plugin if needed
