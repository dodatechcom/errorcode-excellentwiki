---
title: "[Solution] Go bad file descriptor — System Error Fix"
description: "Fix Go bad file descriptor error. Handle closed file descriptors properly."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# bad file descriptor

The error `bad file descriptor` (EBADF) occurs when you attempt to use a file descriptor that has been closed.

## Common Causes

- **Double close** — closing a file descriptor already closed
- **Using a closed file** — calling Write after Close
- **Goroutine race** — one goroutine closes FD while another uses it

## How to Fix

### Fix 1: Do not use files after closing

```go
f, _ := os.Create("output.txt")
f.Write([]byte("hello"))
f.Close()
// f.Write([]byte("world")) // ERROR
```

### Fix 2: Use defer for cleanup

```go
f, err := os.Open("data.txt")
if err != nil { log.Fatal(err) }
defer f.Close()
data := make([]byte, 1024)
n, err := f.Read(data)
```

## Examples

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    f, _ := os.CreateTemp("", "test")
    f.Close()
    _, err := f.Write([]byte("data"))
    fmt.Println(err)
}
```

Output:
```
write /tmp/test123: bad file descriptor
```

## Related Errors

- [io-eof]({{< relref "/languages/go/io-eof" >}}) — end of file.
- [file-not-found]({{< relref "/languages/go/file-not-found" >}}) — file not found.
