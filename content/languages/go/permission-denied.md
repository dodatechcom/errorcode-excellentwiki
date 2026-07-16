---
title: "[Solution] Go Permission Denied Error Fix"
description: "Fix Go permission denied error. Check file permissions, run with appropriate privileges, and use os.Chmod when needed."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["permission", "denied", "chmod", "file", "access"]
weight: 5
---

# Permission Denied — Fix

A permission denied error occurs when your Go program tries to access a file or directory without the necessary operating system permissions.

## Description

Go's `os` package returns `*os.PathError` with `syscall.EACCES` when a file operation fails due to insufficient permissions. This is an OS-level restriction — the file exists but your process doesn't have the right permissions.

Common scenarios:

- **Reading protected system files** — `/etc/shadow` or system configs.
- **Writing to read-only directories** — `/usr/bin` without root.
- **Executing scripts without +x** — file lacks execute permission.
- **Running as wrong user** — process doesn't own the file.

## Common Causes

```go
// Cause 1: Reading protected file
data, err := os.ReadFile("/etc/shadow") // permission denied

// Cause 2: Writing to read-only location
err := os.WriteFile("/usr/bin/output.txt", data, 0644)

// Cause 3: Executing script without permission
cmd := exec.Command("./myscript.sh")
err := cmd.Run() // permission denied

// Cause 4: Wrong file permissions
f, err := os.OpenFile("data.txt", os.O_WRONLY|os.O_CREATE, 0000)
// File created with no permissions
```

## How to Fix

### Fix 1: Check permissions before accessing

```go
// Wrong
data, err := os.ReadFile("/etc/shadow")

// Correct
func canRead(path string) bool {
    info, err := os.Stat(path)
    if err != nil {
        return false
    }
    return info.Mode().Perm()&0400 != 0
}

if canRead("/etc/shadow") {
    data, err := os.ReadFile("/etc/shadow")
    if err != nil {
        log.Fatal(err)
    }
    _ = data
}
```

### Fix 2: Use proper file permissions

```go
// Wrong — file created with no permissions
f, err := os.OpenFile("data.txt", os.O_WRONLY|os.O_CREATE, 0000)

// Correct — owner read/write
f, err := os.OpenFile("data.txt", os.O_WRONLY|os.O_CREATE, 0600)
if err != nil {
    log.Fatal(err)
}
defer f.Close()
```

### Fix 3: Handle permission errors specifically

```go
// Wrong — treats all errors the same
data, err := os.ReadFile(path)
if err != nil {
    log.Fatal(err)
}

// Correct — handle permission errors
data, err := os.ReadFile(path)
if err != nil {
    if pathErr, ok := err.(*os.PathError); ok {
        if os.IsPermission(pathErr.Err) {
            fmt.Println("permission denied — check file permissions")
            return
        }
    }
    log.Fatal(err)
}
```

### Fix 4: Use os.Chmod to fix permissions

```go
import "os"

// Wrong — file is read-only
f, err := os.OpenFile("config.txt", os.O_WRONLY, 0444)

// Correct — change permissions first
os.Chmod("config.txt", 0644)
f, err := os.OpenFile("config.txt", os.O_WRONLY, 0644)
```

### Fix 5: Create files in user-writable directories

```go
// Wrong — writing to system directory
os.WriteFile("/var/log/myapp.log", data, 0644)

// Correct — use user's home directory
home, _ := os.UserHomeDir()
logDir := filepath.Join(home, ".myapp")
os.MkdirAll(logDir, 0755)
os.WriteFile(filepath.Join(logDir, "myapp.log"), data, 0644)
```

## Examples

```go
// This triggers: open /etc/shadow: permission denied
package main

import (
    "fmt"
    "os"
)

func main() {
    data, err := os.ReadFile("/etc/shadow")
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(string(data))
}
```

## Related Errors

- [file-not-found]({{< relref "/languages/go/file-not-found" >}}) — file doesn't exist.
- [too-many-open-files]({{< relref "/languages/go/too-many-open-files" >}}) — file descriptor limit.
- [io-eof]({{< relref "/languages/go/io-eof" >}}) — end of file on read.
