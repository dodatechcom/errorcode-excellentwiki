---
title: "[Solution] Go Mock Error — How to Fix"
description: "Fix Go mock errors. Handle mock setup, call matching, return value configuration, and assertion failures."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Mock Error

Fix Go mock errors. Handle mock setup, call matching, return value configuration, and assertion failures.

## Why It Happens

- Mock is not properly configured causing unexpected nil return values
- Call expectations do not match actual calls causing test failures
- Mock is not called the expected number of times
- After cleanup is not called leaving goroutines running

## Common Error Messages

```
mock: unexpected call to
```
```
mock: expected N calls but got M
```
```
mock: argument mismatch
```
```
mock: function not registered
```

## How to Fix It

### Solution 1: Set up mock expectations properly

```go
mockService := NewMockService(ctrl)
mockService.EXPECT().GetUser(gomock.Any()).Return(&User{Name: "Alice"}, nil)
```

### Solution 2: Use matchers for flexible call matching

```go
mockDB.EXPECT().Query(gomock.Any(), gomock.Any()).
    DoAndReturn(func(ctx context.Context, q string) ([]Row, error) {
        return testRows, nil
    })
```

### Solution 3: Verify all expectations are met

```go
defer ctrl.Finish() // or t.Cleanup(ctrl.Finish)
```

### Solution 4: Handle mock errors in assertions

```go
result, err := service.GetUser(ctx, 123)
if err != nil { t.Fatalf("unexpected error: %v", err) }
if result.Name != "Alice" { t.Errorf("expected Alice, got %s", result.Name) }
```

## Common Scenarios

- A mock returns nil because the expectation was not set up
- A test fails because the mock was called with unexpected arguments
- Mock goroutines leak because Finish is not called

## Prevent It

- Always call ctrl.Finish via t.Cleanup to verify all expectations
- Use gomock.Any for arguments you do not care about in the test
- Use DoAndReturn for complex mock behavior that depends on arguments
