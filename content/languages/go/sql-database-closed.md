---
title: "[Solution] Go sql: database is closed — Database Error Fix"
description: "Fix Go sql: database is closed error. Avoid using database handles after Close()."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# sql: database is closed

The error `sql: database is closed` occurs when you attempt to use a `*sql.DB` handle after `Close()` has been called.

## Common Causes

- **Calling db.Close() in a goroutine** while other goroutines still use it
- **Using a global db variable after shutdown**

## How to Fix

### Fix 1: Never close the DB mid-lifecycle

```go
defer db.Close() // close at very end
```

### Fix 2: Use context with timeout

```go
ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
defer cancel()
var name string
err := db.QueryRowContext(ctx, "SELECT name FROM users WHERE id = 1").Scan(&name)
```

## Examples

```go
package main

import (
    "database/sql"
    "fmt"
    _ "github.com/mattn/go-sqlite3"
)

func main() {
    db, _ := sql.Open("sqlite3", ":memory:")
    db.Close()
    rows, err := db.Query("SELECT 1")
    fmt.Println(err)
}
```

Output:
```
sql: database is closed
```

## Related Errors

- [sql-connection-closed]({{< relref "/languages/go/sql-connection-closed" >}}) — connection closed.
- [sql-no-rows]({{< relref "/languages/go/sql-no-rows" >}}) — no rows returned.
