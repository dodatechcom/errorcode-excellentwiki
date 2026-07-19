---
title: "[Solution] Go context: canceled not propagated — Context Error Fix"
description: "Fix Go context propagation issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# context: canceled not propagated

When a context is canceled, child contexts must also check for cancellation.

## How to Fix

### Fix 1: Always pass context through

```go
func handler(ctx context.Context) {
    result, err := doWork(ctx)
    if err != nil {
        if errors.Is(err, context.Canceled) {
            return // context was canceled
        }
    }
}
```

### Fix 2: Use context.AfterFunc (Go 1.21+)

```go
stop := context.AfterFunc(ctx, func() {
    log.Println("context canceled, cleaning up")
})
defer stop()
```

## Related Errors

- [context-canceled]({{< relref "/languages/go/context-canceled" >}}) — context canceled.
- [context-deadline]({{< relref "/languages/go/context-deadline" >}}) — context deadline.
