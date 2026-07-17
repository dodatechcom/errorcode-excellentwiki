---
title: "[Solution] sqlx Database Connection Error Fix"
description: "Fix sqlx database connection errors. Handle connection pool exhaustion, authentication, and query execution failures."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# sqlx Database Connection Error

Fix sqlx database connection errors. Handle connection pool exhaustion, authentication, and query execution failures.

## What This Error Means

sqlx database connection errors occur when the pool cannot establish or maintain a connection:

```
error occurred while interacting with the database: error connecting to database: No route to host
PoolTimedOut: connection pool timed out
PoolClosed: connection pool was closed
```

## Common Causes

```rust
// Cause 1: Wrong DATABASE_URL or missing environment variable
let pool = SqlitePool::connect("postgres://wrong-host/db").await?;

// Cause 2: Connection pool exhaustion under load
// All connections are in use, new requests time out

// Cause 3: Database not running or unreachable
// Cause 4: Authentication failure (wrong password/user)
// Cause 5: SSL mode mismatch
```

## How to Fix

### Fix 1: Configure pool size and timeouts

```rust
use sqlx::postgres::PgPoolOptions;

let pool = PgPoolOptions::new()
    .max_connections(5)
    .min_connections(1)
    .acquire_timeout(std::time::Duration::from_secs(10))
    .idle_timeout(std::time::Duration::from_secs(300))
    .connect(std::env::var("DATABASE_URL")?)
    .await?;
```

### Fix 2: Add retry logic with exponential backoff

```rust
use sqlx::PgPool;
use std::time::Duration;

async fn connect_with_retry() -> PgPool {
    let mut delay = Duration::from_secs(1);
    loop {
        match PgPool::connect(&std::env::var("DATABASE_URL").unwrap()).await {
            Ok(pool) => return pool,
            Err(e) => {
                eprintln!("Connection failed: {}, retrying in {:?}", e, delay);
                tokio::time::sleep(delay).await;
                delay = (delay * 2).min(Duration::from_secs(60));
            }
        }
    }
}
```

### Fix 3: Validate connection on startup

```rust
use sqlx::PgPool;

async fn init_db() -> PgPool {
    let pool = PgPoolOptions::new()
        .max_connections(5)
        .connect(&std::env::var("DATABASE_URL").expect("DATABASE_URL must be set"))
        .await
        .expect("Failed to connect to database");

    // Verify the connection works
    sqlx::query("SELECT 1")
        .execute(&pool)
        .await
        .expect("Database health check failed");

    pool
}
```

## Examples

```rust
use sqlx::PgPool;

#[derive(Debug, sqlx::FromRow)]
struct User {
    id: i64,
    name: String,
    email: String,
}

async fn list_users(pool: &PgPool) -> Result<Vec<User>, sqlx::Error> {
    let users = sqlx::query_as::<_, User>("SELECT id, name, email FROM users")
        .fetch_all(pool)
        .await?;

    Ok(users)
}

#[tokio::main]
async fn main() {
    let pool = PgPool::connect("postgres://localhost/mydb").await.unwrap();
    let users = list_users(&pool).await.unwrap();
    println!("Found {} users", users.len());
}
```

## Related Errors

- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — connection refused
- [Connection Refused 2]({{< relref "/languages/rust/connection-refused-2" >}}) — connection refused
- [Diesel Error]({{< relref "/languages/rust/diesel-error" >}}) — diesel error
