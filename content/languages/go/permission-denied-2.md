---
title: "[Solution] Go Permission Denied Error Fix"
description: "Fix Go permission denied error when accessing files. Set correct file permissions, run with appropriate privileges, and handle permission errors gracefully."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["permission", "denied", "access", "file", "os", "runtime"]
weight: 5
---

# Permission Denied Error Fix

The `permission denied` error occurs when a Go program tries to access a file or directory without the necessary operating system permissions.

## Description

Go's `os` package returns `*os.PathError` wrapping `syscall.EACCES` when a file operation is denied by the OS. This applies to read, write, execute, and directory listing operations. Permissions are enforced by the OS based on the user running the process and file permission bits.

Common scenarios:

- **File owned by different user** — process running as wrong user.
- **Restrictive file permissions** — file mode doesn't grant access to the process user.
- **Directory not executable** — directory needs execute permission for traversal.
- **Root-only files** — accessing `/etc/shadow` or similar without root.
- **Read-only filesystem** — mounted filesystem doesn't allow writes.

## Common Causes

```go
// Cause 1: Writing to read-only file
func main() {
    err := os.WriteFile("/etc/hostname", []byte("newname"), 0644)
    // permission denied unless root
}

// Cause 2: Reading restricted file
func main() {
    data, err := os.ReadFile("/etc/shadow")
    // permission denied — only root can read
}

// Cause 3: Executing script without permission
func main() {
    err := os.Chmod("script.sh", 0644) // no execute bit
    cmd := exec.Command("./script.sh")
    err = cmd.Run() // permission denied
}

// Cause 4: Creating file in restricted directory
func main() {
    f, err := os.Create("/usr/local/file.txt")
    // permission denied unless root
}
```

## How to Fix

### Fix 1: Set appropriate file permissions

```go
func createFile(path string) error {
    f, err := os.OpenFile(path, os.O_CREATE|os.O_WRONLY, 0644)
    if err != nil {
        return fmt.Errorf("create file: %w", err)
    }
    defer f.Close()
    return nil
}
```

### Fix 2: Check permissions before accessing

```go
func canRead(path string) bool {
    _, err := os.OpenFile(path, os.O_RDONLY, 0)
    return err == nil
}

func canWrite(path string) bool {
    f, err := os.OpenFile(path, os.O_WRONLY, 0)
    if err != nil {
        return false
    }
    f.Close()
    return true
}
```

### Fix 3: Handle permission errors specifically

```go
func readFile(path string) ([]byte, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        if errors.Is(err, fs.ErrPermission) {
            return nil, fmt.Errorf("permission denied: %s", path)
        }
        return nil, err
    }
    return data, nil
}
```

### Fix 4: Use os.UserHomeDir for user-specific paths

```go
func getConfigPath() string {
    home, err := os.UserHomeDir()
    if err != nil {
        return ".config"
    }
    return filepath.Join(home, ".config", "myapp")
}
```

## Examples

```go
// This triggers: open /root/secret.txt: permission denied
package main

import (
    "fmt"
    "os"
)

func main() {
    _, err := os.ReadFile("/root/secret.txt")
    fmt.Println(err) // permission denied
}
```

## Related Errors

- [file-not-found]({{< relref "/languages/go/file-not-found" >}}) — file doesn't exist.
- [too-many-open-files]({{< relref "/languages/go/too-many-open-files" >}}) — file descriptor limit reached.
- [io-pipe-broken]({{< relref "/languages/go/io-pipe-broken" >}}) — pipe closed during operation.
