---
title: "[Solution] Go sql: connection is closed — Database Error Fix"
description: "Fix Go sql: connection is closed error. Properly manage database connections."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# sql: connection is closed

The error `sql: connection is closed` occurs when you try to use a database connection that has already been closed.

## Description

This happens when a `*sql.DB` or `*sql.Conn` is closed before all queries finish.

## Common Causes

- **Calling db.Close() prematurely** — closing the pool while queries are in flight
- **Connection timeout** — the connection was closed by the database server
- **Using a leaked connection** — a connection obtained via `db.Conn()` not returned

## How to Fix

### Fix 1: Do not close the DB until program exit

```go
db, err := sql.Open("mysql", dsn)
if err != nil { log.Fatal(err) }
defer db.Close()
```

### Fix 2: Use db.Conn() for explicit connections

```go
ctx := context.Background()
conn, err := db.Conn(ctx)
if err != nil { log.Fatal(err) }
defer conn.Close()
```

### Fix 3: Set connection pool limits

```go
db.SetMaxOpenConns(25)
db.SetMaxIdleConns(5)
db.SetConnMaxLifetime(5 * time.Minute)
```

## Examples

```go
package main

import (
    "database/sql"
    "fmt"
    "log"
    _ "github.com/lib/pq"
)

func main() {
    db, _ := sql.Open("postgres", "host=localhost dbname=test")
    db.Close()
    var name string
    err := db.QueryRow("SELECT name FROM users WHERE id = 1").Scan(&name)
    fmt.Println(err)
}
```

Output:
```
sql: connection is closed
```

## Related Errors

- [sql-database-closed]({{< relref "/languages/go/sql-database-closed" >}}) — closed database handle.
- [sql-no-rows]({{< relref "/languages/go/sql-no-rows" >}}) — no rows returned.
