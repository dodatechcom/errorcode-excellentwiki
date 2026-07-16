---
title: "[Solution] Go File Not Found Error Fix"
description: "Fix Go no such file or directory error. Use correct file paths, check file existence before access, and handle embedded filesystems properly."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["file", "not-found", "os", "filesystem", "path", "runtime"]
weight: 5
---

# File Not Found Error Fix

The `no such file or directory` error occurs when a Go program tries to open, read, or stat a file that doesn't exist at the specified path.

## Description

Go's `os` package interacts with the filesystem through system calls. When a file path doesn't exist, the syscall returns `ENOENT`, which Go translates to `*os.PathError` wrapping `syscall.ENOENT`. This is the most common file-related error.

Common scenarios:

- **Incorrect file path** — typo or wrong relative/absolute path.
- **Working directory changed** — relative paths resolve differently than expected.
- **File deleted between check and open** — TOCTOU race condition.
- **Embedded filesystem missing files** — `embed.FS` doesn't contain expected file.
- **Case sensitivity** — Linux is case-sensitive, macOS is not.

## Common Causes

```go
// Cause 1: Wrong file path
func main() {
    data, err := os.ReadFile("config.json")
    if err != nil {
        log.Fatal(err) // no such file or directory
    }
}

// Cause 2: Relative path resolves differently
func main() {
    // Running from different directory
    data, err := os.ReadFile("./data/file.txt")
    // Fails if working directory is not as expected
}

// Cause 3: TOCTOU race
func main() {
    if _, err := os.Stat("file.txt"); err == nil {
        data, err := os.ReadFile("file.txt") // file may have been deleted
    }
}

// Cause 4: Wrong path separator
func main() {
    path := "data\\file.txt" // Windows path on Linux
    data, err := os.ReadFile(path)
}
```

## How to Fix

### Fix 1: Use absolute paths or path relative to executable

```go
func getConfigPath() string {
    exe, err := os.Executable()
    if err != nil {
        return "config.json"
    }
    return filepath.Join(filepath.Dir(exe), "config.json")
}
```

### Fix 2: Check file exists before opening

```go
func readConfig(path string) ([]byte, error) {
    info, err := os.Stat(path)
    if os.IsNotExist(err) {
        return nil, fmt.Errorf("config file not found: %s", path)
    }
    if err != nil {
        return nil, err
    }
    if info.IsDir() {
        return nil, fmt.Errorf("expected file, got directory: %s", path)
    }
    return os.ReadFile(path)
}
```

### Fix 3: Use filepath.Join for cross-platform paths

```go
// Wrong
path := "data/config.json"

// Correct
path := filepath.Join("data", "config.json")
```

### Fix 4: Use embed.FS for embedded files

```go
import "embed"

//go:embed static/*
var staticFiles embed.FS

func main() {
    data, err := staticFiles.ReadFile("static/index.html")
    if err != nil {
        log.Fatal(err)
    }
    _ = data
}
```

## Examples

```go
// This triggers: open nonexistent.txt: no such file or directory
package main

import (
    "fmt"
    "os"
)

func main() {
    _, err := os.Open("nonexistent.txt")
    fmt.Println(err)
}
```

## Related Errors

- [permission-denied]({{< relref "/languages/go/permission-denied" >}}) — file exists but not accessible.
- [io-eof]({{< relref "/languages/go/io-eof" >}}) — reading past end of file.
- [io-pipe-broken]({{< relref "/languages/go/io-pipe-broken" >}}) — pipe closed during read/write.
