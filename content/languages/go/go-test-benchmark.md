---
title: "[Solution] Go test benchmark comparison — Testing Error Fix"
description: "Fix Go benchmark comparison issues."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# benchmark comparison issues

Comparing benchmarks requires stable conditions and proper methodology.

## How to Fix

### Fix 1: Use benchstat for comparison

```bash
go test -bench=. -count=5 > old.txt
go test -bench=. -count=5 > new.txt
benchstat old.txt new.txt
```

### Fix 2: Set GOMAXPROCS

```go
func BenchmarkSort(b *testing.B) {
    runtime.GOMAXPROCS(1) // isolate from other goroutines
    // benchmark code
}
```

## Related Errors

- [go-bench]({{< relref "/languages/go/go-bench" >}}) — benchmark errors.
- [integer-overflow]({{< relref "/languages/go/integer-overflow" >}}) — integer overflow.
