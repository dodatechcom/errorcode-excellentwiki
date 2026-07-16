---
title: "[Solution] Go Too Many Open Files Error Fix"
description: "Fix Go too many open files error. Close file handles properly, use defer, and increase file descriptor limits."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["files", "open", "file-descriptor", "ulimit", "resource"]
weight: 5
---

# Too Many Open Files — Fix

A "too many open files" error occurs when your Go program exceeds the operating system's limit on open file descriptors.

## Description

Each open file, socket, or pipe uses a file descriptor. Operating systems impose limits on how many file descriptors a process can have simultaneously. When this limit is reached, new `open()` calls fail with `EMFILE` (too many open files).

Common scenarios:

- **File handles not closed** — forgetting `Close()` or `defer f.Close()`.
- **Goroutine leak with open files** — goroutines holding unclosed file handles.
- **Connection leak** — HTTP connections not closed (response body not read).
- **Default ulimit too low** — system default is often 1024.

## Common Causes

```go
// Cause 1: Forgetting to close files
func readFile(path string) {
    f, _ := os.Open(path)
    // f.Close() never called — file handle leaks
    data, _ := io.ReadAll(f)
    _ = data
}

// Cause 2: Not closing HTTP response body
func fetchURL(url string) {
    resp, _ := http.Get(url)
    // resp.Body never closed — socket handle leaks
    _ = resp
}

// Cause 3: Opening many files in loop
for _, path := range paths {
    f, _ := os.Open(path)
    process(f)
    // f not closed in loop
}

// Cause 4: Goroutine leak with open files
func leakyWorker(files <-chan string) {
    for path := range files {
        f, _ := os.Open(path)
        go func() {
            // f never closed — goroutine and file handle leak
            io.ReadAll(f)
        }()
    }
}
```

## How to Fix

### Fix 1: Always use defer to close files

```go
// Wrong
func readFile(path string) ([]byte, error) {
    f, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    data, err := io.ReadAll(f)
    // f.Close() may be skipped on error
    return data, err
}

// Correct
func readFile(path string) ([]byte, error) {
    f, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer f.Close()
    return io.ReadAll(f)
}
```

### Fix 2: Close HTTP response bodies

```go
// Wrong
func fetchURL(url string) {
    resp, err := http.Get(url)
    if err != nil {
        log.Fatal(err)
    }
    // resp.Body not closed — leaks socket
    _ = resp.Body
}

// Correct
func fetchURL(url string) {
    resp, err := http.Get(url)
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
    data, _ := io.ReadAll(resp.Body)
    _ = data
}
```

### Fix 3: Close files in loops

```go
// Wrong
for _, path := range paths {
    f, _ := os.Open(path)
    process(f)
}

// Correct
for _, path := range paths {
    func() {
        f, err := os.Open(path)
        if err != nil {
            return
        }
        defer f.Close()
        process(f)
    }()
}
```

### Fix 4: Increase file descriptor limit

```bash
# Check current limit
ulimit -n

# Increase temporarily
ulimit -n 65536

# Increase permanently (Linux)
# Edit /etc/security/limits.conf:
# * soft nofile 65536
# * hard nofile 65536
```

### Fix 5: Monitor open file descriptors

```go
import "syscall"

func countOpenFiles() int {
    var r syscall.Rlimit
    syscall.Getrlimit(syscall.RLIMIT_NOFILE, &r)
    return int(r.Cur)
}

func monitorOpenFiles() {
    ticker := time.NewTicker(10 * time.Second)
    for range ticker.C {
        fmt.Printf("Open files: %d\n", countOpenFiles())
    }
}
```

## Examples

```go
// This triggers: too many open files (if run enough times)
package main

import (
    "fmt"
    "os"
)

func main() {
    for i := 0; i < 100000; i++ {
        f, err := os.Create(fmt.Sprintf("/tmp/file_%d", i))
        if err != nil {
            fmt.Println(err) // too many open files
            return
        }
        // Never closed — leaks file descriptors
        _ = f
    }
}
```

## Related Errors

- [file-not-found]({{< relref "/languages/go/file-not-found" >}}) — file doesn't exist.
- [permission-denied]({{< relref "/languages/go/permission-denied" >}}) — no permission to access file.
- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — system resource exhaustion.
