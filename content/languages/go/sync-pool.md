---
title: "[Solution] Go sync.Pool — Performance Error Fix"
description: "Fix Go sync.Pool usage issues."
languages: ["go"]
error-types: ["concurrency-error"]
severities: ["error"]
weight: 5
---

# sync.Pool issues

`sync.Pool` values may be garbage collected at any time. Never assume a value from Pool is non-nil.

## How to Fix

```go
var pool = sync.Pool{
    New: func() interface{} {
        return new(bytes.Buffer)
    },
}

buf := pool.Get().(*bytes.Buffer)
buf.Reset()
defer pool.Put(buf)
```

## Related Errors

- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — nil pointer.
- [sync-mutex]({{< relref "/languages/go/sync-mutex" >}}) — mutex issues.
