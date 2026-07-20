---
title: "[Solution] pq Connection Refused Fix"
description: "Fix PostgreSQL (pq) connection errors. Handle database connectivity, SSL configuration, and pool settings."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# pq Connection Refused

The `lib/pq` PostgreSQL driver fails to connect due to wrong connection string, SSL mode mismatch, the PostgreSQL server not running, or `pg_hba.conf` rejecting the connection. The `lib/pq` driver is the older PostgreSQL driver; newer projects should prefer `pgx`.

## Common Causes

```go
// Cause 1: Wrong DSN format
db, err := sql.Open("postgres", "user:pass@localhost:5432/db")
// parse "user:pass@localhost:5432/db": missing protocol scheme

// Cause 2: SSL mode not matching server config
db, err := sql.Open("postgres", "host=localhost port=5432 user=postgres dbname=test sslmode=require")
// server has sslmode=disable

// Cause 3: Password with special characters not escaped
db, err := sql.Open("postgres", "user=postgres password=p@ss/db dbname=test")
// @ is treated as host separator

// Cause 4: Connection timeout
db.SetConnMaxLifetime(1 * time.Second)
// connection to server established but query times out

// Cause 5: PostgreSQL not accepting connections
// max_connections reached — FATAL: too many connections
```

## How to Fix

### Fix 1: Use proper DSN format with all parameters

```go
import (
    "database/sql"
    "fmt"
    "time"

    _ "github.com/lib/pq"
)

func openDB() (*sql.DB, error) {
    connStr := fmt.Sprintf(
        "host=%s port=%d user=%s password=%s dbname=%s sslmode=%s connect_timeout=%d",
        "localhost", 5432, "user", "password", "mydb", "disable", 10,
    )

    db, err := sql.Open("postgres", connStr)
    if err != nil {
        return nil, err
    }

    db.SetMaxOpenConns(25)
    db.SetMaxIdleConns(5)
    db.SetConnMaxLifetime(5 * time.Minute)

    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()
    if err := db.PingContext(ctx); err != nil {
        return nil, fmt.Errorf("ping: %w", err)
    }
    return db, nil
}
```

### Fix 2: URL-encoded password in connection string

```go
// Password with special characters: p@ss/word
// URL-encoded: p%40ss%2Fword
connStr := "postgres://user:p%40ss%2Fword@localhost:5432/mydb?sslmode=disable"
db, err := sql.Open("postgres", connStr)
```

### Fix 3: Use environment variables for credentials

```go
func dbURL() string {
    return fmt.Sprintf("postgres://%s:%s@%s:%s/%s?sslmode=%s",
        os.Getenv("DB_USER"),
        url.QueryEscape(os.Getenv("DB_PASSWORD")),
        os.Getenv("DB_HOST"),
        os.Getenv("DB_PORT"),
        os.Getenv("DB_NAME"),
        os.Getenv("DB_SSLMODE"),
    )
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
    "os"

    _ "github.com/lib/pq"
)

func main() {
    db, err := sql.Open("postgres", os.Getenv("DATABASE_URL"))
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()

    var version string
    err = db.QueryRowContext(ctx, "SELECT version()").Scan(&version)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("PostgreSQL:", version)
}
```

## Related Errors

- [go-pgerror]({{< relref "/languages/go/go-pgerror" >}}) — PostgreSQL error codes from pgx
- [go-sqlx-error]({{< relref "/languages/go/go-sqlx-error" >}}) — sqlx named query errors
- [tls-handshake]({{< relref "/languages/go/tls-handshake-error" >}}) — SSL/TLS handshake with PostgreSQL
