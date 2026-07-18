---
title: "[Solution] Go Redis Error — How to Fix"
description: "Fix Go Redis errors. Handle connection pooling, command timeouts, pipeline failures, cluster slot migration, and authentication."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Redis Error

Fix Go Redis errors. Handle connection pooling, command timeouts, pipeline failures, cluster slot migration, and authentication.

## Why It Happens

- Redis server is not reachable or the connection string is incorrect
- Command timeout is not configured causing operations to hang indefinitely
- Pipeline commands fail because of connection loss during execution
- Redis cluster is rebalancing and some slots are temporarily unavailable

## Common Error Messages

```
dial tcp: connect: connection refused
```
```
redis: command timeout
```
```
redis: connection pool exhausted
```
```
CROSSSLOT keys in request do not hash to the same slot
```

## How to Fix It

### Solution 1: Configure Redis client with timeouts

```go
rdb := redis.NewClient(&redis.Options{
    Addr:         "localhost:6379",
    PoolSize:     100,
    MinIdleConns: 10,
    DialTimeout:  5 * time.Second,
    ReadTimeout:  3 * time.Second,
    WriteTimeout: 3 * time.Second,
})
```

### Solution 2: Handle Redis errors with retry

```go
err := rdb.Set(ctx, "key", "value", time.Minute).Err()
if err != nil {
    if errors.Is(err, redis.Nil) {
        // Key does not exist
    } else if strings.Contains(err.Error(), "connection refused") {
        // Redis is down
    }
}
```

### Solution 3: Use pipelines for batch operations

```go
pipe := rdb.Pipeline()
for i := 0; i < 100; i++ {
    pipe.Set(ctx, fmt.Sprintf("key%d", i), "value", 0)
}
cmds, err := pipe.Exec(ctx)
if err != nil { log.Printf("pipeline error: %v", err) }
```

### Solution 4: Use hash tags for cluster-compatible operations

```go
// Use hash tags to ensure keys are in the same slot
pipe.Set(ctx, "{user:123}:name", "Alice", 0)
pipe.Set(ctx, "{user:123}:email", "alice@example.com", 0)
```

## Common Scenarios

- A Redis connection fails because TLS is required but not configured
- Pipeline commands fail silently because individual errors are not checked
- A Redis cluster command fails because keys are in different hash slots

## Prevent It

- Always set DialTimeout, ReadTimeout, and WriteTimeout on the Redis client
- Check errors on individual pipeline commands, not just the pipeline result
- Use hash tags {} for multi-key operations in Redis Cluster
