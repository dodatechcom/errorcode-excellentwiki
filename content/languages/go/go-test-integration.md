---
title: "[Solution] Go integration test error — Testing Error Fix"
description: "Fix Go integration test setup and teardown."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# integration test errors

Integration tests require external services, proper configuration, and cleanup.

## How to Fix

### Fix 1: Use build tags

```go
//go:build integration

func TestWithPostgres(t *testing.T) {
    db, _ := sql.Open("postgres", os.Getenv("TEST_DATABASE_URL"))
    defer db.Close()
    // integration test
}
```

### Fix 2: Skip when not available

```go
func TestIntegration(t *testing.T) {
    if os.Getenv("INTEGRATION") == "" {
        t.Skip("skipping integration test")
    }
}
```

## Related Errors

- [sql-connection-closed]({{< relref "/languages/go/sql-connection-closed" >}}) — connection closed.
- [connection-refused]({{< relref "/languages/go/connection-refused" >}}) — connection refused.
