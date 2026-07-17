---
title: "[Solution] redis Cluster Connection Error Fix"
description: "Fix redis cluster connection errors. Handle cluster topology, slot redirection, and connection pool issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# redis Cluster Connection Error

Fix redis cluster connection errors. Handle cluster topology, slot redirection, and connection pool issues.

## What This Error Means

redis cluster connection errors occur when the client cannot communicate with the Redis cluster:

```
redis::ClusterError: Failed to connect to cluster node
MOVED 3999 127.0.0.1:7001
Connection refused
```

## Common Causes

```rust
// Cause 1: Wrong initial seed nodes
let client = ClusterClient::new(vec!["redis://wrong-host:6379"])?;

// Cause 2: Cluster node down or unreachable
// Cause 3: Connection pool exhaustion under load
// Cause 4: ACL or authentication failure
// Cause 5: Cross-slot operations not supported
```

## How to Fix

### Fix 1: Configure cluster with multiple seed nodes

```rust
use redis::cluster::ClusterClient;

let client = ClusterClient::new(vec![
    "redis://10.0.0.1:6379",
    "redis://10.0.0.2:6379",
    "redis://10.0.0.3:6379",
])?;

let mut conn = client.get_connection()?;
```

### Fix 2: Set timeouts and retry configuration

```rust
use redis::cluster::ClusterClient;
use redis::ConnectionInfo;

let mut infos: Vec<ConnectionInfo> = nodes.iter()
    .map(|node| node.parse().unwrap())
    .collect();

let client = ClusterClient::new(infos)?
    .read_from_replicas();

let mut conn = client.get_connection()?;
conn.set_read_timeout(Some(std::time::Duration::from_secs(5)))?;
conn.set_write_timeout(Some(std::time::Duration::from_secs(5)))?;
```

### Fix 3: Use Redis Cluster with async and connection pooling

```rust
use redis::cluster::ClusterClient;

async fn connect_cluster() -> Result<(), redis::RedisError> {
    let client = ClusterClient::new(vec![
        "redis://node1:6379",
        "redis://node2:6379",
        "redis://node3:6379",
    ])?;

    let mut conn = client.get_async_connection().await?;

    redis::cmd("SET")
        .arg("key")
        .arg("value")
        .query_async(&mut conn)
        .await?;

    Ok(())
}
```

## Examples

```rust
use redis::cluster::{ClusterClient, ClusterConnection};

fn cluster_example() -> Result<(), redis::RedisError> {
    let client = ClusterClient::new(vec![
        "redis://127.0.0.1:7000",
        "redis://127.0.0.1:7001",
        "redis://127.0.0.1:7002",
    ])?;

    let mut conn = client.get_connection()?;

    // Basic operations work transparently in cluster mode
    redis::cmd("SET").arg("key1").arg("value1").execute(&mut conn);
    let val: String = redis::cmd("GET").arg("key1").query(&mut conn)?;
    println!("Value: {}", val);

    Ok(())
}
```

## Related Errors

- [Redis Error]({{< relref "/languages/rust/redis-error-rs3" >}}) — redis error
- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — connection refused
- [Timed Out]({{< relref "/languages/rust/timed-out" >}}) — timeout error
