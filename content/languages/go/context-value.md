---
title: "[Solution] Go context: value not found — Context Error Fix"
description: "Fix Go context value not found issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# context: value not found

Using `context.Value` with an unregistered key returns nil.

## How to Fix

### Fix 1: Define typed keys

```go
type contextKey string
const myKey contextKey = "myKey"

ctx = context.WithValue(ctx, myKey, "value")
val, ok := ctx.Value(myKey).(string)
```

### Fix 2: Always check existence

```go
val := ctx.Value(key)
if val == nil {
    // handle missing value
}
```

## Related Errors

- [interface-nil]({{< relref "/languages/go/interface-nil" >}}) — nil interface.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — nil pointer.
