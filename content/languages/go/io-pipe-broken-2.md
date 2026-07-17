---
title: "[Solution] Go Broken Pipe Error Fix"
description: "Fix Go broken pipe error when writing to a closed pipe or connection. Handle SIGPIPE, check connection state before writing, and use error recovery."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Broken Pipe Error Fix

The `write |0: broken pipe` error occurs when a process writes to a pipe or socket whose read end has been closed.

## Description

A broken pipe happens when one end of a pipe or socket connection is closed while the other end is still writing. In Unix-like systems, this generates a SIGPIPE signal which Go ignores by default (unlike C programs). Instead, the write operation returns an `EPIPE` error. This commonly occurs with HTTP responses to clients that disconnect early.

Common scenarios:

- **Client disconnects during response** — browser closes before server finishes sending.
- **Piped command output** — head/tail reads partial output and closes pipe.
- **Closed file descriptor** — writing to a file that was closed by another goroutine.
- **Network connection reset** — remote peer closed the connection.

## Common Causes

```go
// Cause 1: HTTP client disconnects mid-response
func slowHandler(w http.ResponseWriter, r *http.Request) {
    for i := 0; i < 1000000; i++ {
        fmt.Fprintf(w, "%d\n", i) // broken pipe if client disconnects
    }
}

// Cause 2: Writing to closed pipe
func main() {
    r, w := io.Pipe()
    w.Close()
    w.Write([]byte("hello")) // broken pipe
}

// Cause 3: Piped process output
func main() {
    cmd := exec.Command("head", "-1")
    cmd.Stdout = os.Stdout
    // If stdout is a pipe that closes early
    cmd.Run()
}

// Cause 4: Writing to closed network connection
func handleConn(conn net.Conn) {
    go func() {
        time.Sleep(time.Second)
        conn.Close()
    }()
    conn.Write([]byte("data")) // may get broken pipe
}
```

## How to Fix

### Fix 1: Check for broken pipe and handle gracefully

```go
func slowHandler(w http.ResponseWriter, r *http.Request) {
    for i := 0; i < 1000000; i++ {
        _, err := fmt.Fprintf(w, "%d\n", i)
        if err != nil {
            if errors.Is(err, io.ErrClosedPipe) || strings.Contains(err.Error(), "broken pipe") {
                return // client disconnected, stop writing
            }
            log.Printf("write error: %v", err)
            return
        }
        // Flush if using Flusher
        if f, ok := w.(http.Flusher); ok {
            f.Flush()
        }
    }
}
```

### Fix 2: Handle SIGPIPE explicitly

```go
func main() {
    // Go ignores SIGPIPE by default, but you can handle it
    signal.Notify(make(chan os.Signal, 1), syscall.SIGPIPE)
    // Or let the write error be returned instead
}
```

### Fix 3: Check if pipe/writer is closed before writing

```go
func safeWrite(w io.Writer, data []byte) error {
    _, err := w.Write(data)
    if err != nil {
        return fmt.Errorf("write failed: %w", err)
    }
    return nil
}
```

### Fix 4: Use context to detect client disconnects

```go
func handler(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()
    for i := 0; i < 1000; i++ {
        select {
        case <-ctx.Done():
            return // client disconnected
        default:
            fmt.Fprintf(w, "%d\n", i)
            if f, ok := w.(http.Flusher); ok {
                f.Flush()
            }
        }
    }
}
```

## Examples

```go
// This triggers: write |0: broken pipe
package main

import (
    "io"
    "fmt"
)

func main() {
    r, w := io.Pipe()
    r.Close()
    _, err := w.Write([]byte("hello"))
    fmt.Println(err) // broken pipe
}
```

## Related Errors

- [io-eof]({{< relref "/languages/go/io-eof" >}}) — end of data stream.
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — connection refused.
- [context-canceled]({{< relref "/languages/go/context-canceled" >}}) — context canceled when client disconnects.
