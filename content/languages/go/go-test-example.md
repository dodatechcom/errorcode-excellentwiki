---
title: "[Solution] Go test example error — Testing Error Fix"
description: "Fix Go test example errors."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test example errors

Go testable examples must have correct output comments.

## How to Fix

### Fix 1: Correct output comments

```go
func ExampleAdd() {
    fmt.Println(Add(2, 3))
    // Output: 5
}
```

### Fix 2: Use unordered output

```go
func ExampleKeys() {
    m := map[string]int{"a": 1, "b": 2}
    for _, k := range Keys(m) {
        fmt.Println(k)
    }
    // Unordered output: a b
}
```

## Related Errors

- [test-fail]({{< relref "/languages/go/test-fail" >}}) — test failed.
- [go-build-error]({{< relref "/languages/go/go-build-error" >}}) — build error.
