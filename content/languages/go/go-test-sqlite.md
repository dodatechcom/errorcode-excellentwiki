---
title: "[Solution] Go test SQLite error — Testing Error Fix"
description: "Fix Go test SQLite in-memory database."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test SQLite errors

SQLite in-memory databases require proper connection management.

## How to Fix

### Fix 1: Use shared in-memory database

```go
func setupTestDB(t *testing.T) *sql.DB {
    db, err := sql.Open("sqlite3", ":memory:\_shared_cache=on")
    if err != nil { t.Fatal(err) }
    t.Cleanup(func() { db.Close() })
    return db
}
```

## Related Errors

- [sql-connection-closed]({{< relref "/languages/go/sql-connection-closed" >}}) — connection closed.
- [sql-no-rows]({{< relref "/languages/go/sql-no-rows" >}}) — no rows.
