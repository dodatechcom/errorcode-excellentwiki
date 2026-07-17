---
title: "[Solution] Kotlin IOException — Input/Output Error Fix"
description: "Fix Kotlin IOException when file or network operations fail. Handle missing files, check permissions, and use proper error handling."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# IOException — Input/Output Error Fix

An `IOException` is thrown when an I/O operation fails, such as reading/writing files, network communication, or stream operations. It's the parent class for many specific I/O exceptions.

## Description

`IOException` covers a broad range of input/output failures. In Kotlin, it's commonly seen with file operations, network requests, and stream processing. Many subclasses provide more specific error information.

Common scenarios:

- **File not found** — `FileNotFoundException` (subclass of `IOException`).
- **Permission denied** — cannot read/write file.
- **Disk full** — cannot write more data.
- **Network issues** — connection problems, timeouts.
- **Closed stream** — reading from an already-closed stream.

## Common Causes

```kotlin
// Cause 1: File not found
val content = File("nonexistent.txt").readText()  // FileNotFoundException

// Cause 2: Permission denied
val content = File("/root/secret.txt").readText()  // IOException

// Cause 3: Reading closed stream
val stream = FileInputStream("data.txt")
stream.close()
stream.read()  // IOException: Stream closed

// Cause 4: Disk full during write
File("/full/disk/output.txt").writeText("data")  // IOException: No space left
```

## Solutions

### Fix 1: Use try-catch for file operations

```kotlin
// Wrong — no error handling
val content = File("data.txt").readText()

// Correct — handle exceptions
try {
    val content = File("data.txt").readText()
    println(content)
} catch (e: FileNotFoundException) {
    println("File not found: ${e.message}")
} catch (e: IOException) {
    println("I/O error: ${e.message}")
}
```

### Fix 2: Check file existence before operations

```kotlin
// Wrong — assumes file exists
val content = File("data.txt").readText()

// Correct — check first
val file = File("data.txt")
if (file.exists() && file.isFile) {
    val content = file.readText()
} else {
    println("File not found")
}
```

### Fix 3: Use Kotlin's extension functions safely

```kotlin
// Wrong — may throw
val lines = File("data.txt").readLines()

// Correct — use runCatching
val result = runCatching {
    File("data.txt").readLines()
}
result.onSuccess { lines ->
    lines.forEach { println(it) }
}
result.onFailure { e ->
    println("Error: ${e.message}")
}
```

### Fix 4: Use use() for automatic resource cleanup

```kotlin
// Wrong — manual close
val reader = FileReader("data.txt")
val content = reader.readText()
reader.close()  // May not run if exception thrown

// Correct — use() auto-closes
File("data.txt").reader().use { reader ->
    val content = reader.readText()
    println(content)
}
```

## Examples

```kotlin
import java.io.File
import java.io.IOException

fun readFile(path: String): String? {
    return try {
        File(path).readText()
    } catch (e: IOException) {
        println("Failed to read $path: ${e.message}")
        null
    }
}

fun main() {
    val content = readFile("data.txt")
    content?.let { println(it) }
}
```

## Related Errors

- [FileNotFoundException]({{< relref "/languages/kotlin/file-not-found" >}}) — file does not exist.
- [ConnectException]({{< relref "/languages/kotlin/connection-refused" >}}) — network connection refused.
- [SocketTimeoutException]({{< relref "/languages/kotlin/socket-timeout" >}}) — network operation timed out.
