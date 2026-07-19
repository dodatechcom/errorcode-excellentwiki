---
title: "[Solution] Go test table-driven test error — Testing Error Fix"
description: "Fix Go table-driven test issues."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# table-driven test errors

Common issues include variable capture in loops and incorrect test data.

## How to Fix

### Fix 1: Capture range variable (Go 1.22+ fixed)

```go
for _, tt := range tests {
    t.Run(tt.name, func(t *testing.T) {
        got := process(tt.input)
        if got != tt.want {
            t.Errorf("got %v, want %v", got, tt.want)
        }
    })
}
```

### Fix 2: Use struct with clear naming

```go
tests := []struct {
    name    string
    input   string
    want    string
    wantErr bool
}{
    {"valid", "hello", "HELLO", false},
    {"empty", "", "", false},
    {"invalid", "!@#", "", true},
}
```

## Related Errors

- [test-fail]({{< relref "/languages/go/test-fail" >}}) — test failed.
- [race-condition]({{< relref "/languages/go/race-condition" >}}) — race condition.
