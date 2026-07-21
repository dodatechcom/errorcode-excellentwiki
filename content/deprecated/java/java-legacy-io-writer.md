---
title: "[Solution] Deprecated Function Migration: OutputStreamWriter to NIO Files"
description: "Migrate from deprecated OutputStreamWriter to NIO Files."
deprecated_function: "new OutputStreamWriter(new FileOutputStream(file))"
replacement_function: "Files.newBufferedWriter(path)"
languages: ["java"]
deprecated_since: "Java NIO"
---

# [Solution] Deprecated Function Migration: OutputStreamWriter to NIO Files

The `new OutputStreamWriter(new FileOutputStream(file))` has been deprecated in favor of `Files.newBufferedWriter(path)`.

## Migration Guide

NIO Files is simpler.

## Before (Deprecated)

```java
try (OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream(file))) {
    osw.write(data);
}
```

## After (Modern)

```java
try (BufferedWriter writer = Files.newBufferedWriter(path)) {
    writer.write(data);
}
```

## Key Differences

- NIO Files is simpler
