---
title: "[Solution] Go Too Many Open Files Error Fix"
description: "Fix Go too many open files error. Close file descriptors properly, use connection pooling, and increase ulimits when needed."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["files", "open", "file-descriptor", "limit", "ulimit", "runtime"]
weight: 5
---

# Too Many Open Files Error Fix

The `too many open files` error occurs when a process exceeds the operating system's limit on open file descriptors.

## Description

Every open file, socket, pipe, or database connection consumes a file descriptor. Operating systems impose per-process limits (default often 1024 on Linux/macOS). When this limit is reached, new open/connect operations fail with `EMFILE` — `too many open files`.

Common scenarios:

- **File handles not closed** — opening files in loops without closing.
- **Database connection pool too large** — more connections than file descriptors.
- **HTTP client without connection reuse** — creating new connections per request.
- **Goroutines each opening files** — concurrent file operations exhaust limit.
- **Socket leaks** — accepting connections without closing them.

## Common Causes

```go
// Cause 1: Files not closed in loop
func processFiles(dir string) {
    files, _ := os.ReadDir(dir)
    for _, f := range files {
        data, _ := os.ReadFile(filepath.Join(dir, f.Name()))
        process(data)
        // File handle leaked — ReadFile opens but doesn't explicitly close
    }
}

// Cause 2: Database connection leak
func main() {
    for i := 0; i < 2000; i++ {
        db, _ := sql.Open("mysql", dsn)
        // Each db.Open creates connections without closing
    }
}

// Cause 3: HTTP client creating new connections
func main() {
    for i := 0; i < 2000; i++ {
        resp, _ := http.Get("https://api.example.com")
        // Each request may open a new connection
        resp.Body.Close()
    }
}

// Cause 4: Goroutine leak with open files
func worker() {
    f, _ := os.Open("data.bin")
    go func() {
        // f never closed
        time.Sleep(time.Hour)
    }()
}
```

## How to Fix

### Fix 1: Always close files with defer

```go
func readFile(path string) ([]byte, error) {
    f, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer f.Close() // guaranteed to close

    return io.ReadAll(f)
}
```

### Fix 2: Use connection pooling for databases

```go
func main() {
    db, _ := sql.Open("mysql", dsn)
    db.SetMaxOpenConns(25)   // limit open connections
    db.SetMaxIdleConns(10)   // keep idle connections ready
    db.SetConnMaxLifetime(5 * time.Minute)
}
```

### Fix 3: Reuse HTTP client and transport

```go
// Wrong — creates new transport per request
func main() {
    for i := 0; i < 1000; i++ {
        client := &http.Client{}
        client.Get("https://api.example.com")
    }
}

// Correct — reuse single client
func main() {
    client := &http.Client{
        Transport: &http.Transport{
            MaxIdleConnsPerHost: 10,
        },
    }
    for i := 0; i < 1000; i++ {
        resp, _ := client.Get("https://api.example.com")
        resp.Body.Close()
    }
}
```

### Fix 4: Increase file descriptor limit

```bash
# Check current limit
ulimit -n

# Increase for current session
ulimit -n 65536

# Increase permanently in /etc/security/limits.conf
# * soft nofile 65536
# * hard nofile 65536
```

## Examples

```go
// This triggers: too many open files
package main

import "os"

func main() {
    var files []*os.File
    for i := 0; i < 2000; i++ {
        f, _ := os.Open("/dev/null")
        files = append(files, f)
        // Never closed
    }
}
```

## Related Errors

- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — memory resource exhaustion.
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — connection refused (related network issue).
- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutines holding open resources.
