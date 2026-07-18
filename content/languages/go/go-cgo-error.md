---
title: "[Solution] Go CGO Error — How to Fix"
description: "Fix Go CGO errors. Handle C library linking, cross-compilation, and performance."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go CGO Error

Fix Go CGO errors. Handle C library linking, cross-compilation, and performance.

## Why It Happens

- CGO cannot find C header files causing compilation failures
- CGO cross-compilation fails because of missing cross-compiler
- CGO adds significant build time compared to pure Go
- CGO makes binary deployment harder because of shared library dependencies

## Common Error Messages

```
cgo: gcc failed
```
```
cgo: no such file or directory
```
```
cgo: cannot find -l
```
```
cgo: signal: killed
```

## How to Fix It

### Solution 1: Use CGO correctly

```go
// #cgo CFLAGS: -I/usr/local/include
// #cgo LDFLAGS: -L/usr/local/lib -lsqlite3
// #include <sqlite3.h>
import "C"
import "unsafe"

func openDB(path string) *C.sqlite3 {
    var db *C.sqlite3
    cPath := C.CString(path)
defer C.free(unsafe.Pointer(cPath))
    C.sqlite3_open(cPath, &db)
    return db
}
```

### Solution 2: Disable CGO for pure Go builds

```bash
CGO_ENABLED=0 go build -o myapp
```

### Solution 3: Use pkg-config

```go
// #cgo pkg-config: sqlite3
// #include <sqlite3.h>
import "C"
```

### Solution 4: Handle cross-compilation

```bash
# For Linux ARM64
CC=aarch64-linux-gnu-gcc CGO_ENABLED=1 GOOS=linux GOARCH=arm64 go build
```

## Common Scenarios

- CGO compilation fails because of missing C header files
- CGO cross-compilation fails because of missing cross-compiler
- CGO binary has shared library dependencies that are not available

## Prevent It

- Use pkg-config for dependency discovery
- Set CGO_ENABLED=0 for pure Go binaries when possible
- Include CGO cross-compilation in CI/CD pipeline
