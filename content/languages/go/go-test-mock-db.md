---
title: "[Solution] Go test mock database error — Testing Error Fix"
description: "Fix Go test mock database setup."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test mock database errors

Mock databases require implementing the full interface and handling edge cases.

## How to Fix

### Fix 1: Use sqlmock

```go
import "github.com/DATA-DOG/go-sqlmock"

func TestQuery(t *testing.T) {
    db, mock, _ := sqlmock.New()
    defer db.Close()
    rows := sqlmock.NewRows([]string{"name"}).AddRow("Alice")
    mock.ExpectQuery("SELECT name").WillReturnRows(rows)
    // test code
}
```

## Related Errors

- [sql-no-rows]({{< relref "/languages/go/sql-no-rows" >}}) — no rows.
- [sql-connection-closed]({{< relref "/languages/go/sql-connection-closed" >}}) — connection closed.
