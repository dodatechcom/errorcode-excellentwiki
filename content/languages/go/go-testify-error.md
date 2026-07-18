---
title: "[Solution] Go Testify Error — How to Fix"
description: "Fix Go Testify errors. Handle assertion failures, suite lifecycle, mock configuration, and require vs assert usage."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Testify Error

Fix Go Testify errors. Handle assertion failures, suite lifecycle, mock configuration, and require vs assert usage.

## Why It Happens

- require causes immediate test failure without running cleanup code
- assert continues execution after failure causing secondary panics
- Suite SetupTest/TeardownTest methods are not implemented correctly
- Mock expectations are not set up before the test assertions

## Common Error Messages

```
Error: Received unexpected error
```
```
Error: Not equal: expected != actual
```
```
panic: test timed out
```
```
Error: Expected nil, but got:
```

## How to Fix It

### Solution 1: Use require for fatal assertions

```go
func TestSetup(t *testing.T) {
    db, err := setupDB()
    require.NoError(t, err, "database setup failed")
    require.NotNil(t, db)
}
```

### Solution 2: Use assert for non-fatal assertions

```go
func TestUser(t *testing.T) {
    user := service.GetUser(123)
    assert.Equal(t, "Alice", user.Name)
    assert.NotEmpty(t, user.Email)
}
```

### Solution 3: Use testify suites for complex tests

```go
type APITestSuite struct {
    suite.Suite
    server *httptest.Server
}
func (s *APITestSuite) SetupTest() {
    s.server = httptest.NewServer(handler)
}
func (s *APITestSuite) TearDownTest() {
    s.server.Close()
}
```

### Solution 4: Configure testify mocks properly

```go
type MockRepo struct { mock.Mock }
func (m *MockRepo) GetUser(id int) (*User, error) {
    args := m.Called(id)
    return args.Get(0).(*User), args.Error(1)
}
```

## Common Scenarios

- A test panics because require fails and defer cleanup code runs on nil
- Assert does not use proper comparison causing false positive failures
- Suite tests fail because SetupTest is misspelled

## Prevent It

- Use require for critical setup steps that must succeed
- Use assert for individual assertions that should not stop the test
- Name suite lifecycle methods exactly: SetupTest, TearDownTest, SetupSuite
