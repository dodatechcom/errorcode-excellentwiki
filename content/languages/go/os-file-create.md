---
title: "[Solution] Go os: permission denied creating file — System Error Fix"
description: "Fix Go permission denied creating file."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# os: permission denied creating file

The error occurs when you lack permissions to create a file in the target directory.

## How to Fix

### Fix 1: Check directory permissions

```go
info, _ := os.Stat(dirPath)
if info.Mode().Perm()&0200 == 0 {
    log.Fatal("directory not writable")
}
```

## Related Errors

- [permission-denied]({{< relref "/languages/go/permission-denied" >}}) — permission denied.
- [file-exists]({{< relref "/languages/go/file-exists" >}}) — file exists.
