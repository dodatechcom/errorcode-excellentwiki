---
title: "[Solution] Deprecated Function Migration: BufferedInputStream to NIO Channels"
description: "Migrate from deprecated BufferedInputStream to NIO Channels."
deprecated_function: "BufferedInputStream"
replacement_function: "FileChannel / ByteBuffer"
languages: ["java"]
deprecated_since: "Java NIO"
---

# [Solution] Deprecated Function Migration: BufferedInputStream to NIO Channels

The `BufferedInputStream` has been deprecated in favor of `FileChannel / ByteBuffer`.

## Migration Guide

NIO is more efficient.

## Before (Deprecated)

```java
BufferedInputStream bis = new BufferedInputStream(new FileInputStream(file));
```

## After (Modern)

```java
FileChannel channel = FileChannel.open(file.toPath());
ByteBuffer buf = ByteBuffer.allocate(1024);
channel.read(buf);
```

## Key Differences

- NIO is more efficient
