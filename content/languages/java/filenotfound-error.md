---
title: "[Solution] Java FileNotFoundException: No Such File or Directory Fix"
description: "Fix Java FileNotFoundException with 'No such file or directory'. Check file paths, use classpath resources, ensure parent directories exist, and handle try-with-resources."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
tags: ["filenotfoundexception", "no-such-file", "file-path", "io", "classpath"]
weight: 5
---

# FileNotFoundException: No Such File or Directory

A `java.io.FileNotFoundException: <path> (No such file or directory)` is thrown when an application attempts to open a file at a path that does not exist. Unlike the generic `IOException`, this exception is specific to file-not-found conditions and is unchecked when using `FileInputStream` or `FileReader`.

## Description

The `FileNotFoundException` extends `IOException` and is thrown when:

- The file does not exist at the specified path
- The path is a directory (not a file)
- The file cannot be opened for some other reason (permissions, locked)

The error message includes the full path that was attempted, making it easy to diagnose — if you read the actual path carefully.

## Common Causes

```java
// Cause 1: File doesn't exist
File file = new File("data/config.txt");
FileInputStream fis = new FileInputStream(file);  // FileNotFoundException

// Cause 2: Wrong working directory
File file = new File("logs/app.log");  // relative to CWD, not the JAR

// Cause 3: Incorrect absolute path
File file = new File("/home/user/myfile.txt");  // doesn't exist

// Cause 4: Path is a directory
File file = new File("/etc");
FileInputStream fis = new FileInputStream(file);  // FileNotFoundException

// Cause 5: Classpath resource not found
InputStream is = getClass().getResourceAsStream("/config.properties");  // returns null, not exception
```

## How to Fix

### Fix 1: Check file existence before opening

```java
File file = new File("data/config.txt");
if (!file.exists()) {
    throw new FileNotFoundException("Config file not found: " + file.getAbsolutePath());
}
FileInputStream fis = new FileInputStream(file);
```

### Fix 2: Use classpath resources for bundled files

```java
// Wrong — relative to CWD
InputStream is = new FileInputStream("config.properties");

// Correct — use classloader
InputStream is = getClass().getClassLoader().getResourceAsStream("config.properties");
if (is == null) {
    throw new FileNotFoundException("Resource not found: config.properties");
}
```

### Fix 3: Resolve paths relative to a known location

```java
import java.nio.file.Path;
import java.nio.file.Paths;

// Wrong — relative to CWD
Path configPath = Paths.get("config.txt");

// Correct — resolve relative to the application base
Path basePath = Path.of(System.getProperty("user.home"), "myapp");
Path configPath = basePath.resolve("config.txt");
FileInputStream fis = new FileInputStream(configPath.toFile());
```

### Fix 4: Create parent directories before writing

```java
File outputFile = new File("output/reports/report.txt");

// Wrong — FileNotFoundException because parent dir doesn't exist
FileOutputStream fos = new FileOutputStream(outputFile);

// Correct — ensure parent directory exists
File parentDir = outputFile.getParentFile();
if (!parentDir.exists()) {
    parentDir.mkdirs();
}
FileOutputStream fos = new FileOutputStream(outputFile);
```

### Fix 5: Use try-with-resources for automatic cleanup

```java
// Wrong — resource leak on exception
FileInputStream fis = new FileInputStream(file);
BufferedReader reader = new BufferedReader(new InputStreamReader(fis));
String line = reader.readLine();
// fis never closed if exception occurs

// Correct
try (FileInputStream fis = new FileInputStream(file);
     BufferedReader reader = new BufferedReader(new InputStreamReader(fis))) {
    String line = reader.readLine();
    System.out.println(line);
} catch (FileNotFoundException e) {
    System.err.println("File not found: " + e.getMessage());
} catch (IOException e) {
    System.err.println("Read error: " + e.getMessage());
}
```

## Examples

This error commonly occurs when:

- Running from an IDE vs running from a JAR (different CWD)
- Docker container file paths differ from host paths
- Configuration files haven't been generated or downloaded yet
- After refactoring, file locations changed but code references weren't updated

## Related Errors

- [NullPointerException](nullpointerexception) — null from `getResourceAsStream()` used without checking
- [IOException](ioexception) — broader I/O error category
- [InvalidPathException](#) — malformed file path
