---
title: "[Solution] Go PostgreSQL Error — How to Fix"
description: "Fix Go PostgreSQL errors. Handle connection failures, query timeouts, transaction isolation, COPY operations, and LISTEN/NOTIFY."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go PostgreSQL Error

Fix Go PostgreSQL errors. Handle connection failures, query timeouts, transaction isolation, COPY operations, and LISTEN/NOTIFY.

## Why It Happens

- PostgreSQL server is not running or the connection string is incorrect
- Connection pool exhaustion because max connections are reached
- Query timeout is not set causing long-running queries to block
- Transaction isolation level causes deadlock or serialization failure

## Common Error Messages

```
pq: connection refused
```
```
pq: sorry, too many clients already
```
```
pq: canceling statement due to statement timeout
```
```
pq: deadlock detected
```

## How to Fix It

### Solution 1: Configure connection parameters properly

```go
dsn := fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=%s",
    host, port, user, pass, dbname, sslmode)
db, _ := sql.Open("postgres", dsn)
db.SetMaxOpenConns(20)
db.SetMaxIdleConns(5)
```

### Solution 2: Set statement timeout

```go
_, err = db.Exec("SET statement_timeout = 30000")
// Or per-query:
ctx, cancel := context.WithTimeout(ctx, 10*time.Second)
defer cancel()
row := db.QueryRowContext(ctx, "SELECT * FROM large_table")
```

### Solution 3: Handle deadlock with retry

```go
func withRetry(ctx context.Context, fn func(*sql.Tx) error) error {
    for attempt := 0; attempt < 3; attempt++ {
        tx, _ := db.BeginTx(ctx, nil)
        if err := fn(tx); err != nil {
            tx.Rollback()
            if pgErr, ok := err.(*pq.Error); ok && pgErr.Code == "40P01" {
                time.Sleep(time.Duration(attempt) * 100 * time.Millisecond)
                continue
            }
            return err
        }
        return tx.Commit()
    }
    return fmt.Errorf("max retries exceeded")
}
```

### Solution 4: Use COPY for bulk inserts

```go
stmt, _ := tx.Prepare(pq.CopyIn("users", "name", "email"))
for _, user := range users {
    stmt.Exec(user.Name, user.Email)
}
stmt.Close()
tx.Exec("COPY users FROM STDIN")
```

## Common Scenarios

- A PostgreSQL connection fails because sslmode is not set for cloud-hosted databases
- A production server exhausts PostgreSQL connections because the pool is too large
- A long-running query blocks other queries because statement_timeout is not set

## Prevent It

- Always set MaxOpenConns to be less than PostgreSQL max_connections
- Use statement_timeout to prevent queries from running indefinitely
- Handle pq.Error with error code checks for deadlock and serialization failures
