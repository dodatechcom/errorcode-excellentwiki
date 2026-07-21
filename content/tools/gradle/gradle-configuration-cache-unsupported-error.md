---
title: "Configuration Cache Unsupported Feature"
description: "Gradle configuration cache fails because a plugin or build script uses an unsupported API that is not compatible with caching."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Configuration Cache Unsupported Feature

The Gradle configuration cache caches the result of the configuration phase for faster subsequent builds. This error occurs when a plugin or build script uses APIs that cannot be serialized and restored from the cache.

## Common Causes

- A plugin reads `Project` objects during task execution instead of during configuration
- The build script stores non-serializable objects like `Thread` or `FileInputStream`
- A plugin modifies the project state during the execution phase
- `buildSrc` contains code that uses deprecated configuration-time APIs

## How to Fix

1. Enable configuration cache and check the error report:

```bash
./gradlew build --configuration-cache
```

2. Replace project references in task actions with value suppliers:

```groovy
// Problematic -- captures Project in task action
tasks.register('myTask') {
    doLast {
        println project.name // project is not serializable
    }
}

// Fixed -- use providers
tasks.register('myTask') {
    val projectName = providers.provider { project.name }
    doLast {
        println projectName.get()
    }
}
```

3. Use `ValueSource` for computed values:

```kotlin
// Fixed with ValueSource
abstract class MyValueSource : ValueSource<String, ValueSourceParameters.None> {
    @get:Input
    abstract val myValue: Property<String>

    override fun obtain(): String = myValue.get()
}
```

4. Check plugins for configuration cache compatibility:

```bash
./gradlew build --configuration-cache --info | grep "not compatible"
```

## Examples

```bash
# Error output
Configuration cache state could not be reused: task `:app:myTask` of type
  `org.gradle.api.DefaultTask` does not support the configuration cache.
```

```groovy
// Configuration cache compatible task
tasks.register('myTask', MyTask::class) {
    inputFile.set(file('input.txt'))
    outputFile.set(file('build/output.txt'))
}

abstract class MyTask : DefaultTask() {
    @get:InputFile
    abstract val inputFile: RegularFileProperty

    @get:OutputFile
    abstract val outputFile: RegularFileProperty
}
```

## Related Errors

- [Configuration Cache Error]({{< relref "/tools/gradle/gradle-configuration-cache-error" >}}) -- general cache errors
- [Configuration Cache Serialization]({{< relref "/tools/gradle/gradle-configuration-cache-serialization" >}}) -- serialization failures
