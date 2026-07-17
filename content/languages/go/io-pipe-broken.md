---
title: "[Solution] Go Broken Pipe Error Fix"
description: "Fix Go broken pipe error when writing to a pipe or socket. Handle SIGPIPE, use try patterns, and check connection state before writing."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Write |0: Broken Pipe — Error Fix

A broken pipe error occurs when you write to a pipe, socket, or file descriptor whose reading end has been closed.

## Description

In Go, writing to a pipe or socket whose other end is closed causes a "broken pipe" error. On Unix systems, this generates a `SIGPIPE` signal. Go's runtime ignores `SIGPIPE` for standard file descriptors (1 and 2), but for other file descriptors (like network sockets), the error is returned as `EPIPE`.

Common scenarios:

- **Client disconnects mid-response** — writing to a client that closed the connection.
- **Piped command closes stdin** — writing to a subprocess that has already exited.
- **Socket peer closes** — writing after the remote end has closed the connection.

## Common Causes

```go
// Cause 1: Writing to a closed pipe
r, w := io.Pipe()
r.Close()
w.Write([]byte("data")) // write |0: broken pipe

// Cause 2: Client disconnects from server
conn, _ := listener.Accept()
conn.Write([]byte("response")) // May fail if client disconnected

// Cause 3: Writing to closed file descriptor
f, _ := os.Create("temp.txt")
f.Close()
f.Write([]byte("data")) // write on closed file

// Cause 4: Subprocess stdin closed
cmd := exec.Command("head", "-1")
cmd.Start()
cmd.Process.Kill()
cmd.stdin.Write([]byte("data\n")) // broken pipe
```

## How to Fix

### Fix 1: Handle broken pipe errors gracefully

```go
// Wrong — treats broken pipe as fatal
_, err := conn.Write(data)
if err != nil {
    log.Fatal(err)
}

// Correct — handle broken pipe
_, err := conn.Write(data)
if err != nil {
    if opErr, ok := err.(*net.OpError); ok {
        if opErr.Err.Error() == "broken pipe" {
            conn.Close()
            return // Client disconnected, don't crash
        }
    }
    log.Printf("write error: %v", err)
}
```

### Fix 2: Check if connection is still open before writing

```go
// Wrong — blindly writes to connection
conn.Write(response)

// Correct — check connection state
func writeToConn(conn net.Conn, data []byte) error {
    conn.SetWriteDeadline(time.Now().Add(5 * time.Second))
    _, err := conn.Write(data)
    if err != nil {
        conn.Close()
        return err
    }
    return nil
}
```

### Fix 3: Use io.Copy with error handling

```go
// Wrong
io.Copy(conn, reader)

// Correct
_, err := io.Copy(conn, reader)
if err != nil {
    if err == io.ErrClosedPipe || err == io.ErrShortWrite {
        log.Printf("pipe error: %v", err)
    } else if netErr, ok := err.(net.Error); ok {
        if netErr.Error() == "broken pipe" {
            log.Printf("client disconnected")
        }
    }
}
```

### Fix 4: Handle SIGPIPE in command-line tools

```go
// For CLI tools that pipe output to head, less, etc.
func main() {
    // Go runtime handles SIGPIPE for stdout/stderr
    // But you may want explicit handling
    for _, line := range generateOutput() {
        fmt.Println(line)
    }
}
```

### Fix 5: Use net.Conn with write deadlines

```go
// Wrong — no timeout on write
conn.Write(data)

// Correct — set write deadline
func safeWrite(conn net.Conn, data []byte) error {
    deadline := time.Now().Add(10 * time.Second)
    conn.SetWriteDeadline(deadline)
    _, err := conn.Write(data)
    conn.SetWriteDeadline(time.Time{}) // Clear deadline
    return err
}
```

## Examples

```go
// This triggers: write |0: broken pipe
package main

import (
    "fmt"
    "io"
)

func main() {
    r, w := io.Pipe()
    r.Close()
    _, err := w.Write([]byte("hello"))
    fmt.Println(err) // write |0: broken pipe
}
```

## Related Errors

- [io-eof]({{< relref "/languages/go/io-eof" >}}) — end of file on read.
- [io-pipe-broken]({{< relref "/languages/go/io-pipe-broken" >}}) — broken pipe error.
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — connection refused.
