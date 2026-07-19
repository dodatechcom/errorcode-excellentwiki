---
title: "[Solution] Go test race with example — Testing Error Fix"
description: "Fix Go test race condition in examples."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test race with examples

Example functions can have race conditions with global variables.

## How to Fix

### Fix 1: Use local variables in examples

```go
func Example_myFunc() {
    result := myFunc(42)
    fmt.Println(result)
    // Output: 42
}
```

## Related Errors

- [race-condition]({{< relref "/languages/go/race-condition" >}}) — race condition.
- [test-fail]({{< relref "/languages/go/test-fail" >}}) — test failed.
