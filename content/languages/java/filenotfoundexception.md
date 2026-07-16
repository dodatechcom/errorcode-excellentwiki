---
title: "[Solution] Java FileNotFoundException — File Path and Resource Fix"
description: "Fix Java FileNotFoundException by verifying file paths exist, using correct relative/absolute paths, and handling with try-with-resources."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
tags: ["filenotfoundexception", "file-path", "io", "try-with-resources", "classloader"]
date: 2026-07-15
---

# Java FileNotFoundException

A `FileNotFoundException` is thrown when an application attempts to open a file at a specified path that does not exist, is not accessible, or cannot be opened for any reason. It is a subclass of `IOException` and is unchecked only when using `FileInputStream` or `FileReader` constructors directly.

## Common Causes

```java
// Cause 1: File does not exist at the specified path
File file = new File("data/config.txt");
FileInputStream fis = new FileInputStream(file);  // FileNotFoundException

// Cause 2: Wrong relative path (program CWD is not what you expect)
File file = new File("logs/app.log");  // relative to CWD, not the JAR

// Cause 3: Incorrect absolute path
File file = new File("/home/user/myfile.txt");  // path doesn't exist

// Cause 4: File exists but is a directory
File file = new File("/etc");
FileInputStream fis = new FileInputStream(file);  // FileNotFoundException

// Cause 5: Classpath resource not found
InputStream is = getClass().getResourceAsStream("/config.properties");  // null
```

## Solutions

### Fix 1: Check that the file exists before opening

```java
// Wrong — no existence check
File file = new File("data/config.txt");
FileInputStream fis = new FileInputStream(file);

// Correct
File file = new File("data/config.txt");
if (!file.exists()) {
    throw new FileNotFoundException("Config file not found: " + file.getAbsolutePath());
}
FileInputStream fis = new FileInputStream(file);
```

### Fix 2: Use absolute paths or resolve relative to the classpath

```java
// Wrong — relative path depends on working directory
InputStream is = new FileInputStream("config.properties");

// Correct — use classloader to find resources on the classpath
InputStream is = getClass().getClassLoader().getResourceAsStream("config.properties");
if (is == null) {
    throw new FileNotFoundException("Resource not found: config.properties");
}

// Correct — resolve relative to a known base path
Path basePath = Path.of(System.getProperty("user.home"), "myapp");
Path configPath = basePath.resolve("config.txt");
FileInputStream fis = new FileInputStream(configPath.toFile());
```

### Fix 3: Use try-with-resources for automatic cleanup

```java
// Wrong — resource leak on exception path
FileInputStream fis = new FileInputStream(file);
BufferedReader reader = new BufferedReader(new InputStreamReader(fis));
String line = reader.readLine();
// fis never closed if exception occurs above

// Correct — try-with-resources ensures close
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

### Fix 4: Use `Path.of()` and `Files` API (Java 7+)

```java
import java.nio.file.Files;
import java.nio.file.Path;

Path path = Path.of("data", "config.txt");

if (!Files.exists(path)) {
    System.err.println("File does not exist: " + path.toAbsolutePath());
    return;
}

// Read all lines safely
List<String> lines = Files.readAllLines(path);
```

### Fix 5: Create missing directories if writing a new file

```java
File outputFile = new File("output/reports/report.txt");

// Wrong — FileNotFoundException because parent dir doesn't exist
FileOutputStream fos = new FileOutputStream(outputFile);

// Correct — ensure parent directory exists first
File parentDir = outputFile.getParentFile();
if (!parentDir.exists()) {
    parentDir.mkdirs();  // creates all missing parent directories
}

FileOutputStream fos = new FileOutputStream(outputFile);
```

## Prevention Tips

- Print `file.getAbsolutePath()` in error messages so users can diagnose path issues
- Use classpath resources for config files bundled with the JAR
- Always use try-with-resources for `InputStream`, `OutputStream`, `Reader`, and `Writer`
- In build tools, verify resource directories are on the classpath (Maven `src/main/resources`, Gradle `src/main/resources`)

## Related Errors

- [NullPointerException](../nullpointerexception) — null reference from `getResourceAsStream()`
- [IllegalArgumentException](../illegalargumentexception) — invalid path argument
- [UnsupportedOperationException](../unsupportedoperationexception) — unsupported file operation
