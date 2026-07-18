---
title: "[Solution] Go Test Error — How to Fix"
description: "Fix Go test errors. Handle test setup, table-driven tests, mock initialization, test isolation, and parallel execution."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Test Error

Fix Go test errors. Handle test setup, table-driven tests, mock initialization, test isolation, and parallel execution.

## Why It Happens

- Test setup does not clean up resources causing test pollution
- Table-driven test cases share state causing flaky results
- Test fixtures are not properly isolated between test runs
- t.Parallel causes race conditions when tests share mutable state

## Common Error Messages

```
testing: t.Fatal called in goroutine
```
```
FAIL: test timed out after
```
```
race detected during execution of test
```
```
cannot use testing.TB in parallel test
```

## How to Fix It

### Solution 1: Write proper table-driven tests

```go
func TestAdd(t *testing.T) {
    tests := []struct {
        name string
        a, b int
        want int
    }{{"pos", 1, 2, 3}, {"neg", -1, -2, -3}}
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            if got := Add(tt.a, tt.b); got != tt.want {
                t.Errorf("Add(%d,%d) = %d, want %d", tt.a, tt.b, got, tt.want)
            }
        })
    }
}
```

### Solution 2: Use t.Cleanup for resource cleanup

```go
func TestWithDB(t *testing.T) {
    db := setupTestDB(t)
    t.Cleanup(func() { db.Close() })
}
```

### Solution 3: Handle t.Fatal in goroutines

```go
go func() {
    defer func() {
        if r := recover(); r != nil { t.Errorf("panic: %v", r) }
    }()
    process(input)
}()
```

### Solution 4: Use test fixtures for database tests

```go
func TestMain(m *testing.M) {
    db := setupTestDB()
    code := m.Run()
    db.Close()
    os.Exit(code)
}
```

## Common Scenarios

- Tests fail because test data is not cleaned up between runs
- Parallel tests share state causing intermittent failures
- t.Fatal is called inside a goroutine causing a panic

## Prevent It

- Always use t.Cleanup for resource cleanup instead of defer in TestMain
- Use t.Parallel carefully and ensure tests do not share mutable state
- Never call t.Fatal or t.FailNow from a goroutine
