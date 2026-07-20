---
title: "[Solution] go-redis Connection Refused Fix"
description: "Fix go-redis connection errors. Handle Redis server connectivity, pool configuration, and command timeouts."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# go-redis Connection Refused

The `go-redis` client fails to connect to the Redis server, resulting in connection refused or timeout errors. This happens when Redis is not running, the address is wrong, authentication fails, or the connection pool is exhausted under high concurrency.

## Common Causes

```go
// Cause 1: Redis server not running or wrong address
rdb := redis.NewClient(&redis.Options{
    Addr: "localhost:6379",
})
_, err := rdb.Ping(ctx).Result()
// dial tcp 127.0.0.1:6379: connect: connection refused

// Cause 2: Missing or wrong authentication password
rdb := redis.NewClient(&redis.Options{
    Addr:     "localhost:6379",
    Password: "wrong-password",
})
_, err := rdb.Get(ctx, "key").Result()
// ERR invalid username or password

// Cause 3: Connection pool exhausted
rdb := redis.NewClient(&redis.Options{
    Addr:     "localhost:6379",
    PoolSize: 5,
})
// All pool slots occupied, new commands block or timeout

// Cause 4: TLS configuration mismatch
rdb := redis.NewClient(&redis.Options{
    Addr:      "localhost:6380",
    TLSConfig: &tls.Config{InsecureSkipVerify: true},
})
// tls: first record does not look like a TLS handshake
```

## How to Fix

### Fix 1: Verify Redis server is reachable

```go
import (
    "context"
    "fmt"
    "time"

    "github.com/redis/go-redis/v9"
)

func connectRedis() error {
    rdb := redis.NewClient(&redis.Options{
        Addr:         "localhost:6379",
        DialTimeout:  5 * time.Second,
        ReadTimeout:  3 * time.Second,
        WriteTimeout: 3 * time.Second,
    })

    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()

    pong, err := rdb.Ping(ctx).Result()
    if err != nil {
        return fmt.Errorf("redis unreachable: %w", err)
    }
    fmt.Println("Connected:", pong)
    return nil
}
```

### Fix 2: Configure connection pool for your workload

```go
rdb := redis.NewClient(&redis.Options{
    Addr:         "localhost:6379",
    PoolSize:     100,
    MinIdleConns: 10,
    PoolTimeout:  30 * time.Second,
    MaxRetries:   3,
})
```

### Fix 3: Handle reconnection and retries

```go
func resilientGet(ctx context.Context, rdb *redis.Client, key string) (string, error) {
    val, err := rdb.Get(ctx, key).Result()
    if err == redis.Nil {
        return "", fmt.Errorf("key %s does not exist", key)
    } else if err != nil {
        time.Sleep(100 * time.Millisecond)
        val, err = rdb.Get(ctx, key).Result()
        if err != nil {
            return "", fmt.Errorf("redis get failed after retry: %w", err)
        }
    }
    return val, nil
}
```

## Examples

```go
package main

import (
    "context"
    "fmt"
    "time"

    "github.com/redis/go-redis/v9"
)

func main() {
    ctx := context.Background()
    rdb := redis.NewClient(&redis.Options{
        Addr:         "localhost:6379",
        PoolSize:     50,
        MinIdleConns: 5,
        DialTimeout:  5 * time.Second,
        ReadTimeout:  3 * time.Second,
        WriteTimeout: 3 * time.Second,
    })

    if err := rdb.Ping(ctx).Err(); err != nil {
        panic(fmt.Sprintf("Cannot connect to Redis: %v", err))
    }

    err := rdb.Set(ctx, "greeting", "hello world", 10*time.Minute).Err()
    if err != nil {
        panic(err)
    }

    val, err := rdb.Get(ctx, "greeting").Result()
    if err != nil {
        panic(err)
    }
    fmt.Println("greeting:", val)
}
```

## Related Errors

- [context-deadline-exceeded]({{< relref "/languages/go/context-deadline" >}}) — operation times out waiting for Redis response
- [net-dial-refused]({{< relref "/languages/go/net-dial" >}}) — TCP connection to Redis port fails
- [connection-pool-timeout]({{< relref "/languages/go/go-redis-error" >}}) — all connection pool slots are in use
