---
title: "[Solution] Go os: remove error — Filesystem Error Fix"
description: "Fix Go os.Remove and os.RemoveAll errors."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# os: remove error

Errors from `os.Remove` or `os.RemoveAll` include permission denied and file not found.

## How to Fix

### Fix 1: Check existence before removing

```go
if _, err := os.Stat(path); err == nil {
    os.Remove(path)
}
```

### Fix 2: Use os.RemoveAll for directories

```go
err := os.RemoveAll("temp_dir")
if err != nil { log.Fatal(err) }
```

## Related Errors

- [file-not-found]({{< relref "/languages/go/file-not-found" >}}) — file not found.
- [permission-denied]({{< relref "/languages/go/permission-denied" >}}) — permission denied.
