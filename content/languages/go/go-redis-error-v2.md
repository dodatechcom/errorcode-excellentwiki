---
title: "[Solution] go-redis: Connection Refused Fix"
description: "Fix go-redis connection refused errors. Handle Redis server unavailability, pool exhaustion, and cluster topology changes."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["redis", "connection", "cache", "pool", "cluster"]
weight: 5
---

# go-redis: Connection Refused (v2)

This variant covers go-redis connection errors involving cluster mode, sentinel failover, pool exhaustion, and TLS connection failures to Redis.

## What This Error Means

Common error messages:

- `dial tcp 127.0.0.1:6379: connect: connection refused`
- `redis: all sentinels are unreachable`
- `redis: cluster is down`
- `redis: dial tcp: lookup redis-cluster: no such host`
- `pool exhausted`

go-redis supports standalone, sentinel, and cluster modes. Connection errors can come from any layer — direct connection, sentinel discovery, or cluster slot routing.

## Common Causes

```go
// Cause 1: Redis not running
rdb := redis.NewClient(&redis.Options{Addr: "localhost:6379"})
rdb.Ping(ctx) // connection refused

// Cause 2: Wrong address or port
rdb := redis.NewClient(&redis.Options{Addr: "redis:6380"}) // default is 6379

// Cause 3: Cluster mode but connecting as standalone
rdb := redis.NewClient(&redis.Options{Addr: "redis:6379"})
// Should use NewClusterClient for cluster

// Cause 4: Pool size too small for concurrent load
rdb := redis.NewClient(&redis.Options{
    PoolSize: 5, // only 5 connections, need 50
})

// Cause 5: TLS required but not configured
rdb := redis.NewClient(&redis.Options{
    Addr: "redis:6380", // TLS port, no TLS config
})
```

## How to Fix

### Fix 1: Configure connection with retry

```go
rdb := redis.NewClient(&redis.Options{
    Addr:         "localhost:6379",
    Password:     "",
    DB:           0,
    DialTimeout:  5 * time.Second,
    ReadTimeout:  3 * time.Second,
    WriteTimeout: 3 * time.Second,
    PoolSize:     100,
    MinIdleConns: 10,
})

ctx := context.Background()
for i := 0; i < 3; i++ {
    err := rdb.Ping(ctx).Err()
    if err == nil {
        break
    }
    log.Printf("Redis connection attempt %d failed: %v", i+1, err)
    time.Sleep(time.Duration(i+1) * time.Second)
}
```

### Fix 2: Use cluster client for Redis Cluster

```go
rdb := redis.NewClusterClient(&redis.ClusterOptions{
    Addrs: []string{
        "redis-node1:6379",
        "redis-node2:6379",
        "redis-node3:6379",
    },
    MaxRetries:      3,
    DialTimeout:     5 * time.Second,
    ReadTimeout:     3 * time.Second,
    WriteTimeout:    3 * time.Second,
    PoolSize:        100,
    RouteByLatency:  true,
})

if err := rdb.Ping(ctx).Err(); err != nil {
    log.Printf("Cluster connection failed: %v", err)
}
```

### Fix 3: Use sentinel for high availability

```go
rdb := redis.NewFailoverClient(&redis.FailoverOptions{
    MasterName:    "mymaster",
    SentinelAddrs: []string{"sentinel1:26379", "sentinel2:26379", "sentinel3:26379"},
    DialTimeout:   5 * time.Second,
    ReadTimeout:   3 * time.Second,
    WriteTimeout:  3 * time.Second,
    PoolSize:      100,
})
```

### Fix 4: Add connection health check middleware

```go
func withHealthCheck(rdb *redis.Client) {
    go func() {
        ticker := time.NewTicker(10 * time.Second)
        for range ticker.C {
            ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
            if err := rdb.Ping(ctx).Err(); err != nil {
                log.Printf("Redis health check failed: %v", err)
            }
            cancel()
        }
    }()
}
```

### Fix 5: Configure TLS for encrypted connections

```go
rdb := redis.NewClient(&redis.Options{
    Addr:     "redis-tls:6380",
    Password: "",
    DB:       0,
    TLSConfig: &tls.Config{
        MinVersion: tls.VersionTLS12,
    },
})
```

## Examples

```
dial tcp 127.0.0.1:6379: connect: connection refused
```

```go
// Fix: check Redis availability before starting app
func waitForRedis(addr string, timeout time.Duration) error {
    deadline := time.Now().Add(timeout)
    for time.Now().Before(deadline) {
        conn, err := net.DialTimeout("tcp", addr, 2*time.Second)
        if err == nil {
            conn.Close()
            return nil
        }
        time.Sleep(time.Second)
    }
    return fmt.Errorf("redis not available at %s after %v", addr, timeout)
}

func main() {
    if err := waitForRedis("localhost:6379", 30*time.Second); err != nil {
        log.Fatal(err)
    }
    // start app
}
```

## Related Errors

- [go-redis-error]({{< relref "/languages/go/go-redis-error" >}}) — basic Redis error
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — connection refused
- [go-postgres-error-v2]({{< relref "/languages/go/go-postgres-error-v2" >}}) — PostgreSQL connection error
