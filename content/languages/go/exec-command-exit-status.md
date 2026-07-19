---
title: "[Solution] Go exec: wait: exit status — System Error Fix"
description: "Fix Go exec.Command exit status error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# exec: wait: exit status

The error `exit status 1` or `signal: killed` occurs when an executed command fails or is killed.

## How to Fix

### Fix 1: Check exit code

```go
cmd := exec.Command("ls", "nonexistent")
err := cmd.Run()
if exitErr, ok := err.(*exec.ExitError); ok {
    fmt.Printf("exit status: %d\n", exitErr.ExitCode())
}
```

### Fix 2: Capture output

```go
out, err := cmd.CombinedOutput()
if err != nil {
    fmt.Printf("error: %v\noutput: %s\n", err, out)
}
```

## Related Errors

- [exec-command]({{< relref "/languages/go/exec-command" >}}) — command not found.
- [permission-denied]({{< relref "/languages/go/permission-denied" >}}) — permission denied.
