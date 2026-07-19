---
title: "[Solution] Go filepath.Walk error — Filesystem Error Fix"
description: "Fix Go filepath.Walk errors."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# filepath.Walk error

Errors during `filepath.Walk` include permission denied, missing directories, and symbolic link loops.

## How to Fix

### Fix 1: Handle walk errors in WalkFunc

```go
err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
    if err != nil {
        log.Printf("skipping %s: %v", path, err)
        return nil // skip and continue
    }
    // process file
    return nil
})
```

### Fix 2: Use filepath.WalkDir for better performance

```go
err := filepath.WalkDir(root, func(path string, d fs.DirEntry, err error) error {
    if err != nil { return nil }
    if d.IsDir() { return nil }
    // process file
    return nil
})
```

## Related Errors

- [permission-denied]({{< relref "/languages/go/permission-denied" >}}) — permission denied.
- [file-not-found]({{< relref "/languages/go/file-not-found" >}}) — file not found.
