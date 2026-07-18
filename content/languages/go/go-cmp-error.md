---
title: "[Solution] Go cmp Error — How to Fix"
description: "Fix Go cmp errors. Handle deep comparison failures, type mismatches, unexported fields, and custom comparers."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go cmp Error

Fix Go cmp errors. Handle deep comparison failures, type mismatches, unexported fields, and custom comparers.

## Why It Happens

- cmp.Diff fails because unexported fields are not comparable
- Type mismatches between expected and actual values cause comparison failures
- Custom comparers are not registered for complex types
- cmp.Diff output is too verbose for debugging specific fields

## Common Error Messages

```
cmp.Diff: unexported field not comparable
```
```
cmp: mismatched types
```
```
cmp: cannot compare type
```
```
cmp: option conflicts with another option
```

## How to Fix It

### Solution 1: Use cmpopts to ignore unexported fields

```go
import "github.com/google/go-cmp/cmp/cmpopts"
diff := cmp.Diff(expected, actual,
    cmpopts.IgnoreUnexported(Type{}),
    cmpopts.IgnoreFields(Type{}, "CreatedAt"),
)
```

### Solution 2: Register custom comparers

```go
cmp.Comparer(func(x, y time.Time) bool {
    return x.Truncate(time.Second) == y.Truncate(time.Second)
})
```

### Solution 3: Use cmpopts.EquateApprox for float comparison

```go
diff := cmp.Diff(expected, actual,
    cmpopts.EquateApprox(0.001, 0.0001),
)
```

### Solution 4: Use cmp.Equal for assertions

```go
if !cmp.Equal(expected, actual) {
    t.Errorf("mismatch: %s", cmp.Diff(expected, actual))
}
```

## Common Scenarios

- A test fails because cmp.Diff cannot compare unexported struct fields
- Float comparison fails because of precision differences
- cmp.Diff output is too large to read in test failure messages

## Prevent It

- Use cmpopts.IgnoreUnexported for types with unexported fields
- Use cmpopts.EquateApprox for floating point comparisons
- Use cmpopts.IgnoreFields to focus comparison on specific fields
