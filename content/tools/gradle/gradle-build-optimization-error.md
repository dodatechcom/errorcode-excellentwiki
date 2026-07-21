---
title: "Gradle Build Optimization Error"
description: "Gradle build optimization fails due to incompatible task configurations or incorrectly applied optimization plugins."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Build Optimization Error

Gradle provides build optimization features like configuration cache, build cache, and parallel execution. An optimization error occurs when these features encounter incompatible task configurations.

## Common Causes

- Build cache is enabled but tasks produce non-deterministic output
- Parallel execution causes race conditions in shared resource writes
- Configuration cache cannot serialize a task's inputs or outputs
- The build optimization plugin conflicts with another plugin

## How to Fix

1. Verify build cache configuration:

```groovy
// settings.gradle
buildCache {
    local {
        enabled = true
        directory = new File(rootDir, '.gradle/build-cache')
    }
    remote(HttpBuildCache) {
        url = 'https://cache.example.com/'
        enabled = true
    }
}
```

2. Mark tasks as cacheable with proper inputs and outputs:

```groovy
@CacheableTask
abstract class MyOptimizedTask extends DefaultTask {
    @InputFile
    abstract RegularFileProperty getSourceFile()

    @OutputFile
    abstract RegularFileProperty getOutputFile()
}
```

3. Enable parallel execution cautiously:

```bash
# In gradle.properties
org.gradle.parallel=true
org.gradle.caching=true
org.gradle.configureondemand=true
```

4. Diagnose optimization failures:

```bash
./gradlew build --build-cache --info 2>&1 | grep -i "cache\|optimization\|FAILED"
```

## Examples

```bash
# Error output
Build cache entry for task :app:compileJava could not be stored
  Task outputs are not stable: property 'outputDir' has type File but is not annotated
```

```groovy
// Properly annotated cacheable task
@CacheableTask
abstract class ProcessData extends DefaultTask {
    @InputDirectory abstract DirectoryProperty getSourceDir()
    @OutputDirectory abstract DirectoryProperty getOutputDir()

    @TaskAction
    void execute() { /* processing logic */ }
}
```

## Related Errors

- [Build Cache Error]({{< relref "/tools/gradle/gradle-build-cache-error" >}}) -- build cache failures
- [Parallel Execution Error]({{< relref "/tools/gradle/gradle-parallel-execution-error" >}}) -- parallel build issues
