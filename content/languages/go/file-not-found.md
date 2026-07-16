---
title: "[Solution] Go No Such File or Directory Error Fix"
description: "Fix Go no such file or directory error. Check file paths, use os.Stat to verify existence, and handle relative vs absolute paths."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["file", "not-found", "directory", "path", "os"]
weight: 5
---

# No Such File or Directory — Fix

A "no such file or directory" error occurs when your Go program tries to open, read, or stat a file path that doesn't exist.

## Description

Go's `os` and `ioutil` packages return this error when the specified file path cannot be found. The error is an `*os.PathError` with `syscall.ENOENT`. This is the Go equivalent of Python's `FileNotFoundError`.

Common scenarios:

- **Relative path from wrong working directory** — script run from a different directory.
- **Typo in filename** — `config.json` vs `config.JSON` vs `config.jsonc`.
- **Case sensitivity on Linux** — `File.txt` and `file.txt` are different.
- **File deleted or moved** — path was valid but no longer exists.

## Common Causes

```go
// Cause 1: Relative path from wrong directory
data, err := os.ReadFile("config.json") // Fails if CWD is wrong

// Cause 2: Typo in filename
data, err := os.ReadFile("config.json") // Actual file is "config.JSON"

// Cause 3: Directory instead of file
info, err := os.Stat("/etc")
data, err := os.ReadFile("/etc") // Is a directory, not a file

// Cause 4: Missing file
f, err := os.Open("data.csv") // File doesn't exist yet
```

## How to Fix

### Fix 1: Check file existence before opening

```go
// Wrong
data, err := os.ReadFile("config.json")
if err != nil {
    log.Fatal(err)
}

// Correct
if _, err := os.Stat("config.json"); os.IsNotExist(err) {
    fmt.Println("config.json not found")
    return
}
data, err := os.ReadFile("config.json")
```

### Fix 2: Use absolute paths or resolve relative to executable

```go
// Wrong — depends on working directory
data, err := os.ReadFile("config.json")

// Correct — resolve relative to executable
execPath, _ := os.Executable()
execDir := filepath.Dir(execPath)
configPath := filepath.Join(execDir, "config.json")
data, err := os.ReadFile(configPath)

// Correct — or use current working directory explicitly
wd, _ := os.Getwd()
configPath := filepath.Join(wd, "config.json")
```

### Fix 3: Handle path errors specifically

```go
// Wrong — treats all errors the same
data, err := os.ReadFile(path)
if err != nil {
    log.Fatal(err)
}

// Correct — handle path errors
data, err := os.ReadFile(path)
if err != nil {
    if pathErr, ok := err.(*os.PathError); ok {
        fmt.Printf("path error: %v (op=%s, path=%s)\n",
            pathErr.Err, pathErr.Op, pathErr.Path)
    }
    log.Fatal(err)
}
```

### Fix 4: Create directories if needed before writing

```go
// Wrong — parent directory may not exist
os.WriteFile("/data/output/result.txt", content, 0644)

// Correct — create directory first
dir := filepath.Dir("/data/output/result.txt")
os.MkdirAll(dir, 0755)
os.WriteFile("/data/output/result.txt", content, 0644)
```

### Fix 5: Use filepath.Walk to find files

```go
// Correct — search for files in a directory
filepath.Walk("/some/path", func(path string, info os.FileInfo, err error) error {
    if err != nil {
        return err
    }
    if !info.IsDir() && strings.HasSuffix(path, ".json") {
        fmt.Println(path)
    }
    return nil
})
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
    data, err := os.ReadFile("nonexistent.txt")
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(string(data))
}
```

## Related Errors

- [permission-denied]({{< relref "/languages/go/permission-denied" >}}) — file exists but no permission.
- [too-many-open-files]({{< relref "/languages/go/too-many-open-files" >}}) — file descriptor limit reached.
- [io-eof]({{< relref "/languages/go/io-eof" >}}) — end of file on read.
