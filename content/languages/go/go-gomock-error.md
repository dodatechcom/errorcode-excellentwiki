---
title: "[Solution] Go gomock Error — How to Fix"
description: "Fix Go gomock errors. Handle controller setup, expectation ordering, call count verification, and interface matching."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go gomock Error

Fix Go gomock errors. Handle controller setup, expectation ordering, call count verification, and interface matching.

## Why It Happens

- Controller is not created in the test function causing improper cleanup
- Expectations are set after the function under test is called
- Call count expectations are wrong causing flaky tests
- Mock interface does not match the actual interface being used

## Common Error Messages

```
gomock: expected call not satisfied
```
```
gomock: call does not match any expectation
```
```
gomock: missing call to
```
```
gomock: unexpected call
```

## How to Fix It

### Solution 1: Create controller properly

```go
func TestService(t *testing.T) {
    ctrl := gomock.NewController(t)
    defer ctrl.Finish()
    mockRepo := NewMockRepository(ctrl)
}
```

### Solution 2: Set expectations before calling the function

```go
mockRepo.EXPECT().FindUser(gomock.Any()).Return(&User{}, nil)
result := service.GetUser(ctx, 123)
```

### Solution 3: Control call order with InOrder

```go
gomock.InOrder(
    mock.EXPECT().Connect().Return(nil),
    mock.EXPECT().Query(gomock.Any()).Return([]Row{}),
    mock.EXPECT().Close().Return(nil),
)
```

### Solution 4: Use Times for call count

```go
mockRepo.EXPECT().SaveUser(gomock.Any()).Times(3)
```

## Common Scenarios

- Tests fail because controller is not created in the test function
- Expectation order is wrong causing mock to not match calls
- A mock is called an unexpected number of times

## Prevent It

- Always create gomock.NewController at the start of each test
- Set all expectations before calling the function under test
- Use gomock.InOrder for ordered call sequences
