---
title: "[Solution] Rust AMQP Error — How to Fix"
description: "Fix AMQP message broker errors in Rust. Resolve channel, queue, and consumer issues with the lapin crate."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# AMQP Error

AMQP errors occur when using the `lapin` crate to communicate with RabbitMQ or other AMQP message brokers. Failures can arise from connection issues, channel errors, or message deserialization problems.

## Common Causes

```rust
use lapin::{Connection, ConnectionProperties, options::*, types::FieldTable};
use tokio_amqp::LapinTokioExt;

// Connection failure — broker unreachable or wrong credentials
let conn = Connection::connect(
    "amqp://wrong_host:5672/%2f",
    ConnectionProperties::default().with_tokio(),
).await?;

// Channel error — publishing to a closed channel
let channel = conn.create_channel().await?;
channel.close(0, "").await?;
channel.basic_publish("exchange", "key", BasicPublishOptions::default(),
    b"hello".to_vec(), BasicProperties::default()).await?;
```

## How to Fix

1. **Verify connection strings and credentials**

```rust
use lapin::{Connection, ConnectionProperties};
use tokio_amqp::LapinTokioExt;

let addr = std::env::var("AMQP_URL")
    .unwrap_or_else(|_| "amqp://guest:guest@localhost:5672/%2f".into());

let conn = Connection::connect(&addr,
    ConnectionProperties::default().with_tokio(),
).await.expect("Failed to connect to AMQP broker");
```

2. **Acknowledge messages to prevent channel prefetch saturation**

```rust
use lapin::options::*;

channel.basic_qos(1, BasicQosOptions::default()).await?;
let mut consumer = channel.basic_consume("my_queue", "tag",
    BasicConsumeOptions::default(), FieldTable::default()).await?;

while let Some(delivery) = consumer.next().await {
    let delivery = delivery?;
    println!("Received: {:?}", String::from_utf8_lossy(&delivery.data));
    channel.basic_ack(delivery.delivery_tag, BasicAckOptions::default()).await?;
}
```

3. **Reconnect on channel/connection errors**

```rust
use lapin::Connection;
use std::sync::Arc;
use tokio::sync::Mutex;

async fn ensure_connection(conn: &Arc<Mutex<Option<Connection>>>) -> lapin::Result<Connection> {
    let mut guard = conn.lock().await;
    if let Some(c) = guard.as_ref() {
        if c.status().connected() {
            return Ok(c.clone());
        }
    }
    let new_conn = Connection::connect(
        "amqp://guest:guest@localhost:5672/%2f",
        lapin::ConnectionProperties::default().with_tokio(),
    ).await?;
    *guard = Some(new_conn.clone());
    Ok(new_conn)
}
```

## Examples

```rust
use lapin::{options::*, types::FieldTable, BasicProperties, Connection, ConnectionProperties};
use tokio_amqp::LapinTokioExt;

#[tokio::main]
async fn main() -> lapin::Result<()> {
    let conn = Connection::connect(
        "amqp://guest:guest@localhost:5672/%2f",
        ConnectionProperties::default().with_tokio(),
    ).await?;

    let channel = conn.create_channel().await?;
    channel.queue_declare("hello", QueueDeclareOptions::default(),
        FieldTable::default()).await?;

    channel.basic_publish("", "hello", BasicPublishOptions::default(),
        b"Hello from Rust!".to_vec(),
        BasicProperties::default().with_content_type("text/plain".into()),
    ).await?.await?;

    let mut consumer = channel.basic_consume("hello", "my_consumer",
        BasicConsumeOptions::default(), FieldTable::default()).await?;

    if let Some(delivery) = consumer.next().await {
        let delivery = delivery?;
        println!("Got {:?}", String::from_utf8_lossy(&delivery.data));
        channel.basic_ack(delivery.delivery_tag, BasicAckOptions::default()).await?;
    }
    Ok(())
}
```

## Related Errors

- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — broker unreachable
- [Timed Out]({{< relref "/languages/rust/timed-out" >}}) — AMQP operation timed out
- [IO Error]({{< relref "/languages/rust/io-error" >}}) — underlying I/O failure
