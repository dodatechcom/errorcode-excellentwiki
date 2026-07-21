---
title: "[Solution] Deprecated Function Migration: manual buffering to io.Copy"
description: "Migrate from deprecated manual buffering to io.Copy."
deprecated_function: "Manual read/write loop"
replacement_function: "io.Copy(dst, src)"
languages: ["go"]
deprecated_since: "Go 1.0+"
---

# [Solution] Deprecated Function Migration: manual buffering to io.Copy

The `Manual read/write loop` has been deprecated in favor of `io.Copy(dst, src)`.

## Migration Guide

io.Copy handles buffering automatically.

## Before (Deprecated)

```go
buf := make([]byte, 4096)
for {
    n, err := src.Read(buf)
    if err != nil { break }
    dst.Write(buf[:n])
}
```

## After (Modern)

```go
_, err := io.Copy(dst, src)
if err != nil {
    log.Fatal(err)
}
```

## Key Differences

- io.Copy handles buffering
