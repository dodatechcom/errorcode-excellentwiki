---
title: "[Solution] Kotlin File I/O Error — Read/Write, Access Denied, Path Not Found"
description: "Fix Kotlin file I/O errors including access denied, path not found, and read/write failures. Learn robust file handling patterns."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1034
---

## Common Causes

- File path not found (relative vs absolute path confusion)
- Access denied (missing file permissions)
- Concurrent file access without synchronization
- Using `readText()` on very large files (memory exhaustion)

```kotlin
// File not found — relative path issue
val file = File("data/config.json")  // Relative to working directory
file.readText()  // FileNotFoundException
```

## How to Fix

**1. Use absolute paths or verify file existence**

```kotlin
val file = File("/absolute/path/to/file.txt")
if (!file.exists()) {
    file.parentFile?.mkdirs()
    file.createNewFile()
}
```

**2. Handle permissions properly**

```kotlin
val file = File("/data/app.log")
try {
    file.appendText("New log entry\n")
} catch (e: SecurityException) {
    // Permission denied — use context.filesDir on Android
}
```

**3. Use buffered I/O for large files**

```kotlin
// WRONG: Loads entire file into memory
val content = hugeFile.readText()

// CORRECT: Stream processing
hugeFile.bufferedReader().useLines { lines ->
    lines.forEach { line -> processLine(line) }
}
```

**4. Use path.toPath() for cross-platform compatibility**

```kotlin
import java.nio.file.Paths
val path = Paths.get("/", "data", "file.txt")
```

## Examples

```kotlin
// Example 1: Safe file reading with use
fun readFile(path: String): String? {
    return try {
        File(path).bufferedReader().use { it.readText() }
    } catch (e: FileNotFoundException) {
        println("File not found: $path")
        null
    }
}

// Example 2: Write with atomic rename
fun atomicWrite(target: File, content: String) {
    val temp = File.createTempFile("temp", ".tmp", target.parentFile)
    try {
        temp.writeText(content)
        temp.renameTo(target)
    } finally {
        temp.delete()
    }
}

// Example 3: Directory listing
fun listKotlinFiles(dir: File): List<File> {
    return dir.listFiles { file -> file.extension == "kt" }?.toList() ?: emptyList()
}
```

## Related Errors

- [File not found](file-not-found) — file not found
- [IO exception](io-exception) — IO exception
- [Access denied](illegal-access) — permission denied
