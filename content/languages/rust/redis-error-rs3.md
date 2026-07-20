---
title: "[Solution] redis Cluster Connection Error Fix"
description: "Fix redis cluster connection errors. Handle cluster topology, slot redirection, and connection pool issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Redis Cluster Error

Redis cluster errors occur when using `redis` crate with cluster mode — slot redirection and topology issues.

## Common Causes

```rust
// Slot not on this node
// MOVED 3999 127.0.0.1:6380

// Cluster not initialized properly
let cluster = ClusterClient::new(nodes)?;
```

## How to Fix

1. **Use cluster client**

```rust
use redis::cluster::ClusterClient;

let nodes = vec!["redis://127.0.0.1:6379", "redis://127.0.0.1:6380"];
let client = ClusterClient::new(nodes)?;
let mut conn = client.get_connection()?;
```

2. **Handle MOVED/ASK redirections**

```rust
use redis::Commands;

let _: () = conn.set("key", "value")?;
let val: String = conn.get("key")?;
```

3. **Use read from replicas**

```rust
use redis::cluster::ClusterClient;

let mut conn = client.get_read_only_connection()?;
let val: String = conn.get("key")?;
```

## Examples

```rust
use redis::cluster::ClusterClient;
use redis::Commands;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let nodes = vec!["redis://127.0.0.1:6379", "redis://127.0.0.1:6380"];
    let client = ClusterClient::new(nodes)?;
    let mut conn = client.get_connection()?;
    let _: () = conn.set("cluster_key", "cluster_value")?;
    let val: String = conn.get("cluster_key")?;
    println!("Value: {}", val);
    Ok(())
}
```

## Related Errors

- [Redis Error]({{< relref "/languages/rust/redis-error-rs" >}}) — Redis single node
- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — network
- [Tokio Error]({{< relref "/languages/rust/tokio-error" >}}) — async runtime
