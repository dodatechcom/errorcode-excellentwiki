---
title: "[Solution] Go exec: command not found — System Error Fix"
description: "Fix Go exec.Command error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# exec: command not found

The error `exec: "command": executable file not found in $PATH` occurs when the binary is not in PATH.

## How to Fix

### Fix 1: Use full path

```go
cmd := exec.Command("/usr/bin/git", "status")
```

### Fix 2: Use exec.LookPath

```go
path, err := exec.LookPath("git")
if err != nil {
    log.Fatal("git not found in PATH")
}
cmd := exec.Command(path, "status")
```

## Related Errors

- [connection-refused]({{< relref "/languages/go/connection-refused" >}}) — connection refused.
- [permission-denied]({{< relref "/languages/go/permission-denied" >}}) — permission denied.
