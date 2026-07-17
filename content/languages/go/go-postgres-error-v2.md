---
title: "[Solution] pgx: PostgreSQL Connection Error Fix"
description: "Fix pgx PostgreSQL connection errors in Go. Handle connection refused, auth failures, and pool exhaustion."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["postgresql", "pgx", "database", "connection", "pool"]
weight: 5
---

# pgx: PostgreSQL Connection Error

This error occurs when the pgx driver cannot establish or maintain a connection to PostgreSQL. It covers direct connection failures, pool exhaustion, and authentication issues.

## What This Error Means

Common error messages:

- `dial tcp 127.0.0.1:5432: connect: connection refused`
- `pq: password authentication failed for user "app"`
- `pq: the database system is shutting down`
- `connpool: pool exhausted`
- `pq: too many connections already`

pgx is a pure Go PostgreSQL driver. Connection errors come from network issues, PostgreSQL configuration limits, authentication problems, or connection pool misconfiguration.

## Common Causes

```go
// Cause 1: PostgreSQL not running
conn, err := pgx.Connect(ctx, "postgres://localhost:5432/mydb")

// Cause 2: Wrong credentials
conn, err := pgx.Connect(ctx, "postgres://user:wrongpass@localhost:5432/mydb")

// Cause 3: Database does not exist
conn, err := pgx.Connect(ctx, "postgres://localhost:5432/nonexistent")

// Cause 4: Connection pool exhausted
pool, err := pgxpool.New(ctx, connString)

// Cause 5: Max connections exceeded at PostgreSQL level
```

## How to Fix

### Fix 1: Configure connection pool properly

```go
config, err := pgxpool.ParseConfig(connString)
if err != nil {
    log.Fatal(err)
}

config.MaxConns = 20
config.MinConns = 5
config.MaxConnLifetime = time.Hour
config.MaxConnIdleTime = 30 * time.Minute
config.HealthCheckPeriod = time.Minute

pool, err := pgxpool.NewWithConfig(ctx, config)
if err != nil {
    log.Fatal(err)
}
defer pool.Close()
```

### Fix 2: Add connection validation

```go
func validateConnection(ctx context.Context, pool *pgxpool.Pool) error {
    return pool.Ping(ctx)
}

if err := validateConnection(ctx, pool); err != nil {
    log.Printf("Database connection failed: %v", err)
}
```

### Fix 3: Use connection string with options

```go
connString := "postgres://user:pass@localhost:5432/mydb?sslmode=require&connect_timeout=10&pool_max_conns=20&pool_min_conns=5"

pool, err := pgxpool.New(ctx, connString)
if err != nil {
    log.Fatal(err)
}
```

### Fix 4: Handle connection errors with retry

```go
func queryWithRetry(ctx context.Context, pool *pgxpool.Pool, query string, args ...interface{}) (pgx.Rows, error) {
    var rows pgx.Rows
    var err error

    for i := 0; i < 3; i++ {
        rows, err = pool.Query(ctx, query, args...)
        if err == nil {
            return rows, nil
        }
        if !errors.Is(err, context.DeadlineExceeded) {
            break
        }
        time.Sleep(time.Duration(i+1) * time.Second)
    }
    return nil, err
}
```

### Fix 5: Use pgxpool config builder

```go
func newPool(connString string) (*pgxpool.Pool, error) {
    config, err := pgxpool.ParseConfig(connString)
    if err != nil {
        return nil, err
    }
    config.MaxConns = 25
    config.MinConns = 5
    config.BeforeAcquire = func(ctx context.Context, conn *pgx.Conn) bool {
        return conn.Ping(ctx) == nil
    }
    return pgxpool.NewWithConfig(context.Background(), config)
}
```

## Examples

```
dial tcp 127.0.0.1:5432: connect: connection refused
```

```go
// Fix: check PostgreSQL availability before connecting
func waitForPostgres(dsn string, timeout time.Duration) error {
    deadline := time.Now().Add(timeout)
    for time.Now().Before(deadline) {
        conn, err := pgx.Connect(context.Background(), dsn)
        if err == nil {
            conn.Close(context.Background())
            return nil
        }
        time.Sleep(2 * time.Second)
    }
    return fmt.Errorf("postgresql not available after %v", timeout)
}
```

## Related Errors

- [go-postgres-error]({{< relref "/languages/go/go-postgres-error" >}}) — basic PostgreSQL error
- [sql-no-rows]({{< relref "/languages/go/sql-no-rows-2" >}}) — no rows returned
- [go-redis-error-v2]({{< relref "/languages/go/go-redis-error-v2" >}}) — Redis connection error
