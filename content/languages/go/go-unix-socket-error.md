---
title: "[Solution] Go Unix Socket Error — How to Fix"
description: "Fix Go Unix socket errors. Handle socket creation, connection, permissions, and lifecycle."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Unix Socket Error

Fix Go Unix socket errors. Handle socket creation, connection, permissions, and lifecycle.

## Why It Happens

- Unix socket file already exists causing bind failures
- Socket file permissions are wrong preventing connection
- Socket is not properly cleaned up leaving stale files

## Common Error Messages

```
unix: address already in use
```
```
unix: permission denied
```
```
unix: no such file or directory
```
```
unix: connection refused
```

## How to Fix It

### Solution 1: Create Unix socket server

```go
ln, err := net.Listen("unix", "/tmp/myapp.sock")
if err != nil {
    os.Remove("/tmp/myapp.sock")
    ln, err = net.Listen("unix", "/tmp/myapp.sock")
}
if err != nil { log.Fatal(err) }
defer os.Remove("/tmp/myapp.sock")
http.Serve(ln, nil)
```

### Solution 2: Set socket permissions

```go
ln, _ := net.Listen("unix", "/tmp/myapp.sock")
os.Chmod("/tmp/myapp.sock", 0660)
```

### Solution 3: Connect to Unix socket

```go
conn, err := net.Dial("unix", "/tmp/myapp.sock")
if err != nil { log.Fatal(err) }
defer conn.Close()
fmt.Fprintf(conn, "hello\n")
```

### Solution 4: Handle socket cleanup

```go
func cleanupSocket(path string) {
    os.Remove(path)  // Remove stale socket
}
```

## Common Scenarios

- Unix socket file already exists because the previous server did not clean up
- Socket connection fails because of wrong file permissions
- Stale socket files prevent new server from starting

## Prevent It

- Remove socket file before creating a new listener
- Set proper permissions with os.Chmod after creating the socket
- Use os.Remove in cleanup to ensure socket files are deleted
