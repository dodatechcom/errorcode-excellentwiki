---
title: "[Solution] Kotlin Process Builder Error — Exit Code and Stream Handling"
description: "Fix Kotlin ProcessBuilder errors. Learn correct process execution, exit code handling, and stream management in Kotlin."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1035
---

## Common Causes

- Process exits with non-zero exit code not checked
- Deadlock from not consuming stdout/stderr streams
- Command not found on PATH (relative command name)
- Working directory not set for relative paths

```kotlin
// Deadlock: stdout buffer fills while stderr blocks
val process = ProcessBuilder("mycommand").start()
val output = process.inputStream.bufferedReader().readText()  // Blocks forever
val error = process.errorStream.bufferedReader().readText()   // Never reached
```

## How to Fix

**1. Check exit code after process completes**

```kotlin
val process = ProcessBuilder("ls", "-la").start()
val exitCode = process.waitFor()
if (exitCode != 0) {
    val error = process.errorStream.bufferedReader().readText()
    throw RuntimeException("Process failed with exit code $exitCode: $error")
}
```

**2. Consume streams concurrently to prevent deadlock**

```kotlin
val process = ProcessBuilder("mycommand").start()
val stdout = process.inputStream.bufferedReader().readText()
val stderr = process.errorStream.bufferedReader().readText()
process.waitFor()
```

**3. Use redirect for stream management**

```kotlin
val process = ProcessBuilder("mycommand")
    .redirectOutput(ProcessBuilder.Redirect.appendTo(File("output.log")))
    .redirectError(ProcessBuilder.Redirect.appendTo(File("error.log")))
    .start()
```

**4. Set working directory and environment**

```kotlin
val process = ProcessBuilder("git", "status")
    .directory(File("/project/path"))
    .environment()["PATH"] = "/usr/local/bin:/usr/bin"
    .start()
```

## Examples

```kotlin
// Example 1: Complete process execution
data class ProcessResult(
    val exitCode: Int,
    val stdout: String,
    val stderr: String
)

fun execute(vararg command: String, workDir: File? = null): ProcessResult {
    val pb = ProcessBuilder(*command)
    workDir?.let { pb.directory(it) }
    val process = pb.start()
    val stdout = process.inputStream.bufferedReader().readText()
    val stderr = process.errorStream.bufferedReader().readText()
    val exitCode = process.waitFor()
    return ProcessResult(exitCode, stdout, stderr)
}

// Example 2: Streaming output
fun executeStreaming(vararg command: String, onLine: (String) -> Unit) {
    val process = ProcessBuilder(*command).start()
    process.inputStream.bufferedReader().forEachLine(onLine)
    process.waitFor()
}

// Example 3: Timeout for process
fun executeWithTimeout(command: List<String>, timeoutMs: Long): ProcessResult {
    val process = ProcessBuilder(command).start()
    val completed = process.waitFor(timeoutMs, TimeUnit.MILLISECONDS)
    if (!completed) {
        process.destroyForcibly()
        throw TimeoutException("Process timed out")
    }
    return ProcessResult(
        process.exitValue(),
        process.inputStream.bufferedReader().readText(),
        process.errorStream.bufferedReader().readText()
    )
}
```

## Related Errors

- [File I/O error](kotlin-file-io-error) — file operations
- [IO exception](io-exception) — IO exception
- [Socket error](kotlin-socket-error) — socket errors
