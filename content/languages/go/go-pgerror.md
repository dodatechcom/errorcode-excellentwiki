---
title: "[Solution] pgx PostgreSQL Error Codes Fix"
description: "Fix pgx PostgreSQL error codes. Handle database errors, constraint violations, and connection issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# pgx PostgreSQL Error Codes

The `pgx` PostgreSQL driver returns typed PostgreSQL error codes (like `unique_violation`, `foreign_key_violation`, `connection_refused`) that must be handled programmatically. Unlike generic SQL errors, pgx provides `pgconn.PgError` with the SQLSTATE code for precise error handling.

## Common Causes

```go
// Cause 1: Unique constraint violation
_, err := db.Exec(ctx, "INSERT INTO users (email) VALUES ($1)", "dup@example.com")
var pgErr *pgconn.PgError
if errors.As(err, &pgErr) && pgErr.Code == "23505" {
    // unique_violation
}

// Cause 2: Foreign key violation
_, err = db.Exec(ctx, "INSERT INTO posts (user_id) VALUES ($1)", 999)
// 23503: foreign_key_violation — user_id 999 does not exist

// Cause 3: Connection refused
pool, err := pgxpool.New(ctx, "postgres://wrong-host:5432/db")
// connection refused

// Cause 4: Syntax error in SQL
_, err = db.Exec(ctx, "SELECT * FORM users")
// 42601: syntax_error

// Cause 5: Division by zero
_, err = db.Exec(ctx, "UPDATE stats SET ratio = total / 0")
// 22012: division_by_zero
```

## How to Fix

### Fix 1: Handle specific PostgreSQL error codes

```go
import (
    "context"
    "errors"
    "fmt"

    "github.com/jackc/pgx/v5"
    "github.com/jackc/pgx/v5/pgconn"
)

func createUser(ctx context.Context, db *pgx.Conn, email string) error {
    _, err := db.Exec(ctx, "INSERT INTO users (email) VALUES ($1)", email)
    if err != nil {
        var pgErr *pgconn.PgError
        if errors.As(err, &pgErr) {
            switch pgErr.Code {
            case "23505": // unique_violation
                return fmt.Errorf("email %s already exists", email)
            case "23503": // foreign_key_violation
                return fmt.Errorf("referenced record does not exist")
            case "23502": // not_null_violation
                return fmt.Errorf("required field is missing")
            default:
                return fmt.Errorf("postgres error %s: %s", pgErr.Code, pgErr.Message)
            }
        }
        return err
    }
    return nil
}
```

### Fix 2: Use connection pool with retry logic

```go
import (
    "context"
    "time"

    "github.com/jackc/pgx/v5/pgxpool"
)

func connectDB(ctx context.Context) (*pgxpool.Pool, error) {
    config, err := pgxpool.ParseConfig(os.Getenv("DATABASE_URL"))
    if err != nil {
        return nil, err
    }

    config.MaxConns = 20
    config.MinConns = 5
    config.MaxConnLifetime = 30 * time.Minute
    config.MaxConnIdleTime = 5 * time.Minute

    pool, err := pgxpool.NewWithConfig(ctx, config)
    if err != nil {
        return nil, fmt.Errorf("create pool: %w", err)
    }

    if err := pool.Ping(ctx); err != nil {
        return nil, fmt.Errorf("ping database: %w", err)
    }
    return pool, nil
}
```

## Examples

```go
package main

import (
    "context"
    "errors"
    "fmt"
    "log"
    "os"

    "github.com/jackc/pgx/v5"
    "github.com/jackc/pgx/v5/pgconn"
)

func main() {
    conn, err := pgx.Connect(context.Background(), os.Getenv("DATABASE_URL"))
    if err != nil {
        log.Fatal(err)
    }
    defer conn.Close(context.Background())

    var result int
    err = conn.QueryRow(context.Background(), "SELECT 1 + 1").Scan(&result)
    if err != nil {
        var pgErr *pgconn.PgError
        if errors.As(err, &pgErr) {
            log.Fatalf("PostgreSQL error [%s]: %s", pgErr.Code, pgErr.Message)
        }
        log.Fatal(err)
    }
    fmt.Println("1 + 1 =", result)
}
```

## Related Errors

- [sql-no-rows]({{< relref "/languages/go/sql-no-rows-2" >}}) — no rows returned by query
- [go-postgres-error]({{< relref "/languages/go/go-postgres-error" >}}) — pq driver connection issues
- [go-mysql-error]({{< relref "/languages/go/go-mysql-error" >}}) — MySQL equivalent error codes
