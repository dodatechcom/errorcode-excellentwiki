---
title: "[Solution] Go file exists — Filesystem Error Fix"
description: "Fix Go file exists error when creating directories or files."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# file exists

The error `file exists` occurs when you try to create a file or directory that already exists.

## Common Causes

- **Race condition** — two goroutines creating the same directory
- **Idempotent startup** — running initialization code twice

## How to Fix

### Fix 1: Use os.MkdirAll

```go
err := os.MkdirAll("data/logs", 0755)
if err != nil { log.Fatal(err) }
```

### Fix 2: Check with os.IsExist

```go
f, err := os.OpenFile("config.json", os.O_CREATE|os.O_EXCL|os.O_WRONLY, 0644)
if err != nil {
    if os.IsExist(err) {
        fmt.Println("file already exists")
    } else {
        log.Fatal(err)
    }
}
```

## Examples

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    os.MkdirAll("/tmp/test-exists", 0755)
    err := os.Mkdir("/tmp/test-exists", 0755)
    fmt.Println(err)
}
```

Output:
```
mkdir /tmp/test-exists: file exists
```

## Related Errors

- [file-not-found]({{< relref "/languages/go/file-not-found" >}}) — file not found.
- [permission-denied]({{< relref "/languages/go/permission-denied" >}}) — permission denied.
