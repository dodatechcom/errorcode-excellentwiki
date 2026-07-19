---
title: "[Solution] Go connection pool exhausted — Database Error Fix"
description: "Fix Go connection pool exhausted error. Tune MaxOpenConns and connection timeouts."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# connection pool exhausted

The error occurs when all database connections in the pool are in use and new queries block.

## Common Causes

- **Too many concurrent queries** — more queries than available connections
- **Long-running queries** — holding connections open too long
- **Connection leak** — not closing rows or connections properly

## How to Fix

### Fix 1: Increase pool size

```go
db.SetMaxOpenConns(50)
db.SetMaxIdleConns(10)
db.SetConnMaxLifetime(5 * time.Minute)
```

### Fix 2: Always close rows

```go
rows, err := db.Query("SELECT name FROM users")
if err != nil { log.Fatal(err) }
defer rows.Close()
```

## Examples

```go
package main

import (
    "context"
    "database/sql"
    "fmt"
    "time"
    _ "github.com/lib/pq"
)

func main() {
    db, _ := sql.Open("postgres", "host=localhost dbname=test")
    db.SetMaxOpenConns(1)
    defer db.Close()
    ctx, cancel := context.WithTimeout(context.Background(), 1*time.Second)
    defer cancel()
    var result int
    err := db.QueryRowContext(ctx, "SELECT pg_sleep(5)").Scan(&result)
    fmt.Println(err)
}
```

## Related Errors

- [sql-connection-closed]({{< relref "/languages/go/sql-connection-closed" >}}) — connection closed.
- [context-deadline]({{< relref "/languages/go/context-deadline" >}}) — context timeout.
