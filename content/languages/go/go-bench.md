---
title: "[Solution] Go benchmark error — Testing Error Fix"
description: "Fix Go benchmark errors."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# benchmark errors

Benchmark errors occur when benchmarks are not properly set up or produce inconsistent results.

## How to Fix

### Fix 1: Proper benchmark structure

```go
func BenchmarkSort(b *testing.B) {
    data := make([]int, 1000)
    for i := range data {
        data[i] = rand.Intn(1000)
    }
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        sort.Ints(data)
    }
}
```

### Fix 2: Run with memory stats

```bash
go test -bench=. -benchmem
```

## Related Errors

- [test-fail]({{< relref "/languages/go/test-fail" >}}) — test failed.
- [integer-overflow]({{< relref "/languages/go/integer-overflow" >}}) — integer overflow.
