---
title: "[Solution] Kotlin FileNotFoundException — Missing File Fix"
description: "Fix Kotlin FileNotFoundException when a file cannot be found. Verify paths, check permissions, and use proper error handling."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["filenotfoundexception", "file", "path", "read", "write"]
weight: 5
---

# FileNotFoundException — Missing File Fix

A `FileNotFoundException` is thrown when trying to access a file that doesn't exist. It's a subclass of `IOException` and is one of the most common I/O exceptions in Kotlin.

## Description

This exception occurs when the file path is wrong, the file was deleted, or the path is actually a directory. It can also occur when trying to write to a location where the parent directory doesn't exist.

Common scenarios:

- **Wrong file path** — typo or incorrect directory.
- **File deleted** — file was removed between checks.
- **Directory instead of file** — path points to a folder.
- **Parent directory missing** — for write operations.

## Common Causes

```kotlin
// Cause 1: Wrong file path
val content = File("/wrong/path/data.txt").readText()  // FileNotFoundException

// Cause 2: File doesn't exist
val file = File("config.json")
if (!file.exists()) {
    file.readText()  // FileNotFoundException
}

// Cause 3: Directory instead of file
val dir = File("/tmp")
dir.readText()  // FileNotFoundException (it's a directory)

// Cause 4: Parent directory doesn't exist for writing
File("/nonexistent/dir/file.txt").writeText("data")  // FileNotFoundException
```

## Solutions

### Fix 1: Check file existence before reading

```kotlin
// Wrong
val content = File("data.txt").readText()

// Correct
val file = File("data.txt")
if (file.exists() && file.isFile) {
    val content = file.readText()
} else {
    println("File not found: ${file.absolutePath}")
}
```

### Fix 2: Use relative paths or resources

```kotlin
// Wrong — absolute path
val content = File("/home/user/app/config.json").readText()

// Correct — relative path from project root
val content = File("config.json").readText()

// Correct — classpath resource
val content = object {}::class.java.getResourceAsStream("/config.json")?.bufferedReader()?.readText()
```

### Fix 3: Create parent directories when writing

```kotlin
// Wrong — parent directory doesn't exist
File("/new/dir/file.txt").writeText("data")  // FileNotFoundException

// Correct — create directories first
val file = File("/new/dir/file.txt")
file.parentFile?.mkdirs()
file.writeText("data")
```

### Fix 4: Provide default values for missing files

```kotlin
// Wrong
val config = File("config.json").readText()  // FileNotFoundException

// Correct
val configFile = File("config.json")
val config = if (configFile.exists()) {
    configFile.readText()
} else {
    "{}"  // Default empty JSON
}
```

## Examples

```kotlin
import java.io.File

fun loadConfig(path: String): Map<String, String> {
    val file = File(path)
    if (!file.exists()) {
        println("Config file not found at $path, using defaults")
        return mapOf("host" to "localhost", "port" to "8080")
    }
    return file.readLines().associate { line ->
        val (key, value) = line.split("=", limit = 2)
        key to value
    }
}

fun main() {
    val config = loadConfig("config.txt")
    println(config)
}
```

## Related Errors

- [IOException]({{< relref "/languages/kotlin/io-exception" >}}) — general I/O error.
- [SecurityException]({{< relref "/languages/kotlin/illegal-access" >}}) — permission denied.
- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — invalid file path.
