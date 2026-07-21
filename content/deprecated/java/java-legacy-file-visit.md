---
title: "[Solution] Deprecated Function Migration: File.listFiles to Files.walk"
description: "Migrate from deprecated File.listFiles to Files.walk."
deprecated_function: "File.listFiles()"
replacement_function: "Files.walk(path)"
languages: ["java"]
deprecated_since: "Java 8+"
---

# [Solution] Deprecated Function Migration: File.listFiles to Files.walk

The `File.listFiles()` has been deprecated in favor of `Files.walk(path)`.

## Migration Guide

Files.walk is more powerful.

## Before (Deprecated)

```java
File dir = new File("/path");
File[] files = dir.listFiles();
if (files != null) {
    for (File f : files) {
        System.out.println(f.getName());
    }
}
```

## After (Modern)

```java
try (Stream<Path> paths = Files.walk(Path.of("/path"))) {
    paths.filter(Files::isRegularFile)
         .forEach(System.out::println);
}
```

## Key Differences

- Files.walk returns Stream
