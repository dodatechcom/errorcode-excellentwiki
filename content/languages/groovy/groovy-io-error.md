---
title: "[Solution] Groovy IO Exception Reading File Error"
description: "Fix Groovy IOException when reading or writing files. Handle file permissions, encoding, and path issues."
languages: ["groovy"]
error-types: ["io-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The `IOException` occurs when Groovy cannot perform file I/O operations such as reading, writing, or accessing files. This covers file not found, permission denied, encoding errors, and disk full conditions.

## Why It Happens

- File does not exist at specified path: The path is incorrect or the file has been moved.
- Insufficient permissions to read or write file: The process lacks necessary file system permissions.
- File encoding mismatch during read operation: The file uses a different encoding than expected.
- Disk is full during write operation: No space left on the device.
- File is locked by another process: The file is being used by another application.

## How to Fix It

Use try-catch for file operations:

```groovy
try {
    def content = new File("data.txt").text
    println content
} catch (FileNotFoundException e) {
    println "File not found: ${e.message}"
} catch (IOException e) {
    println "IO error: ${e.message}"
}
```

Check file existence before operations:

```groovy
def file = new File("config.properties")
if (file.exists() && file.canRead()) {
    def props = new Properties()
    file.withInputStream { props.load(it) }
} else {
    println "File not accessible: exists=${file.exists()}, readable=${file.canRead()}"
}
```

Specify encoding explicitly to avoid platform-dependent behavior:

```groovy
// WRONG: Uses platform default encoding
def content = new File("data.txt").text

// CORRECT: Explicit encoding
def content = new File("data.txt").getText("UTF-8")

// For writing
new File("output.txt").setText("Hello", "UTF-8")
```

Use safe file traversal:

```groovy
def dir = new File("/path/to/dir")
if (dir.isDirectory()) {
    dir.eachFile { file ->
        println "${file.name}: ${file.length()} bytes"
    }
} else {
    println "Not a directory: ${dir.absolutePath}"
}
```

Use withReader/withWriter for automatic resource management:

```groovy
new File("data.txt").withReader("UTF-8") { reader ->
    def lines = reader.readLines()
    lines.each { println it }
}
```

## Common Mistakes

- Using relative paths that resolve differently at runtime. Always use absolute paths or verify the working directory.
- Not closing file streams in finally blocks. Use withReader/withWriter for automatic cleanup.
- Assuming default encoding matches file encoding. Always specify encoding explicitly.
- Not handling file permission changes in production. Check permissions before operations.
- Not handling symlinks correctly. Use file.canonicalFile to resolve symlinks.

## Related Pages

- [groovy-json-parse-error]({{< relref "/languages/groovy/groovy-jsonerror-v2" >}}) - JSON parse errors
- [groovy-xml-parse-error]({{< relref "/languages/groovy/groovy-xmlparseerror-v2" >}}) - XML parse errors
- [groovy-null-pointer-v2]({{< relref "/languages/groovy/groovy-nullpointererror-v2" >}}) - null pointer
- [groovy-missing-method-v2]({{< relref "/languages/groovy/groovy-missingmethod-v2" >}}) - missing method
