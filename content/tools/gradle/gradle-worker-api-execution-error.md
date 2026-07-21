---
title: "Gradle Worker API Error"
description: "Gradle Worker API fails to execute work items due to classloader isolation issues or incompatible worker configuration."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Worker API Error

The Gradle Worker API allows parallel execution of work items in isolated classloaders. A Worker API error occurs when the work items cannot be executed due to classloader or configuration problems.

## Common Causes

- The worker classpath does not include required dependencies
- Worker isolation mode is incompatible with the work item implementation
- A worker tries to access Gradle internal APIs that are not exported
- Multiple workers share state through static fields causing thread-safety issues

## How to Fix

1. Declare worker dependencies correctly:

```groovy
tasks.register('processData', WorkerTask::class) {
    classpath.from(configurations.workerClasspath)
}
```

2. Configure worker classloader isolation:

```groovy
abstract class WorkerTask : DefaultTask() {
    @get:Classpath
    abstract val workerClasspath: ConfigurableFileCollection

    @TaskAction
    fun execute() {
        val workerQueue = workerExecutor.classLoaderIsolation {
            classpath.from(workerClasspath)
        }
        workerQueue.submit(MyWorker::class.java) { config ->
            config.inputFile.set(inputFile)
        }
    }
}
```

3. Use process isolation if classloader isolation fails:

```groovy
val workerQueue = workerExecutor.processIsolation {
    classpath.from(workerClasspath)
    forkOptions { jvmArgs = ['-Xmx512m'] }
}
```

4. Avoid sharing state between workers:

```groovy
// Problematic -- shared mutable state
companion object {
    var sharedCounter = AtomicInteger(0) // thread-unsafe
}

// Fixed -- worker-local state
class MyWorker : WorkAction<MyParameters> {
    private var localCounter = 0 // worker-local
    override fun execute() { /* work logic */ }
}
```

## Examples

```bash
# Error output
> Failed to submit work item to Worker API:
  Could not isolate classpath for worker 'MyWorker'
  Missing required dependency: com.example:processor:1.0.0
```

```kotlin
// Kotlin DSL Worker API usage
abstract class DataProcessor : DefaultTask() {
    @get:InputFiles
    abstract val inputFiles: ConfigurableFileCollection

    @TaskAction
    fun process() {
        workerExecutor.processIsolation {
            classpath.from(project.configurations.named("workerRuntime"))
        }.submit(ProcessorWorker::class.java) {
            it.files.from(inputFiles)
        }
    }
}
```

## Related Errors

- [Worker API Error]({{< relref "/tools/gradle/gradle-worker-api-error" >}}) -- worker API general issues
- [Process Forking Error]({{< relref "/tools/gradle/gradle-process-forking-error" >}}) -- worker process failures
