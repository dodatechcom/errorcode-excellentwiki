---
title: "[Solution] go-sql-driver Invalid Connection Fix"
description: "Fix MySQL driver connection errors. Handle invalid connections, timeouts, and driver configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# go-sql-driver Invalid Connection

The `go-sql-driver/mysql` driver fails with "invalid connection" or "bad connection" errors when the MySQL server closes the connection unexpectedly, the connection pool contains stale connections, or the `maxAllowedPacket` size is exceeded. This driver uses a connection pool managed by `database/sql`.

## Common Causes

```go
// Cause 1: Stale connection in pool — server closed it
db, _ := sql.Open("mysql", "user:pass@tcp(localhost:3306)/db")
db.SetMaxIdleConns(10)
db.SetConnMaxLifetime(0) // connections never expire — server may close them
// error: invalid connection

// Cause 2: Packet too large
db.Exec("INSERT INTO data VALUES (?)", hugeBlob)
// Packet for query is too large (1048576 > max_allowed_packet)

// Cause 3: Connection timeout on slow queries
db.SetConnMaxLifetime(5 * time.Second)
// query takes 10 seconds — connection recycled mid-query

// Cause 4: Wrong driver name
sql.Open("mysql", dsn) // must be exactly "mysql"

// Cause 5: DSN format incorrect
sql.Open("mysql", "user pass tcp(localhost:3306)/db") // spaces wrong
// parse time parameter missing — time columns return []byte not time.Time
```

## How to Fix

### Fix 1: Configure connection pool properly

```go
import (
    "database/sql"
    "time"

    _ "github.com/go-sql-driver/mysql"
)

func openDB() (*sql.DB, error) {
    db, err := sql.Open("mysql",
        "user:password@tcp(127.0.0.1:3306)/mydb?parseTime=true&timeout=10s")
    if err != nil {
        return nil, err
    }

    db.SetMaxOpenConns(25)
    db.SetMaxIdleConns(10)
    db.SetConnMaxLifetime(5 * time.Minute) // recycle before server closes
    db.SetConnMaxIdleTime(3 * time.Minute)

    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()
    if err := db.PingContext(ctx); err != nil {
        return nil, err
    }
    return db, nil
}
```

### Fix 2: Increase max_allowed_packet on server or use chunked writes

```sql
-- MySQL server side
SET GLOBAL max_allowed_packet = 67108864; -- 64MB
```

### Fix 3: Use context with timeout for all queries

```go
func getUser(ctx context.Context, db *sql.DB, id int) (*User, error) {
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()

    var u User
    err := db.QueryRowContext(ctx,
        "SELECT id, name, email FROM users WHERE id = ?", id,
    ).Scan(&u.ID, &u.Name, &u.Email)
    if err != nil {
        return nil, fmt.Errorf("get user %d: %w", id, err)
    }
    return &u, nil
}
```

## Examples

```go
package main

import (
    "context"
    "database/sql"
    "fmt"
    "log"
    "time"

    _ "github.com/go-sql-driver/mysql"
)

func main() {
    db, err := sql.Open("mysql",
        "root:password@tcp(127.0.0.1:3306)/testdb?parseTime=true")
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    db.SetMaxOpenConns(25)
    db.SetMaxIdleConns(10)
    db.SetConnMaxLifetime(5 * time.Minute)

    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()

    var version string
    err = db.QueryRowContext(ctx, "SELECT VERSION()").Scan(&version)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("MySQL version:", version)
}
```

## Related Errors

- [go-postgres-error]({{< relref "/languages/go/go-postgres-error" >}}) — PostgreSQL connection issues
- [go-pgerror]({{< relref "/languages/go/go-pgerror" >}}) — PostgreSQL error codes
- [connection-refused]({{< relref "/languages/go/net-dial" >}}) — TCP connection to MySQL port fails
