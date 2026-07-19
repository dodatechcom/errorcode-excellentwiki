---
title: "[Solution] Go test mock error — Testing Error Fix"
description: "Fix Go test mock setup errors."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test mock errors

Mock errors occur when mock implementations don't match expected interfaces.

## How to Fix

### Fix 1: Verify interface implementation at compile time

```go
type MockDB struct{}
var _ DB = (*MockDB)(nil) // compile-time check

func (m *MockDB) Query(q string) ([]Row, error) {
    return nil, nil
}
```

## Related Errors

- [cannot-use-interface]({{< relref "/languages/go/cannot-use-interface" >}}) — interface not satisfied.
- [method-not-in-set]({{< relref "/languages/go/method-not-in-set" >}}) — method not in set.
