---
title: "[Solution] Rust Kafka Error — How to Fix"
description: "Fix Kafka errors in Rust. Resolve producer, consumer, and broker connection issues with the rdkafka crate."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Kafka Error

Kafka errors occur when using the `rdkafka` crate (or similar) to interact with Apache Kafka — broker connection failures, producer/consumer configuration issues, and message deserialization problems.

## Common Causes

```rust
use rdkafka::consumer::{Consumer, StreamConsumer};
use rdkafka::config::ClientConfig;

// Wrong broker address
let consumer: StreamConsumer = ClientConfig::new()
    .set("bootstrap.servers", "wrong_host:9092")
    .set("group.id", "my-group")
    .create()?; // Connection failure

// Missing required configuration
let consumer: StreamConsumer = ClientConfig::new()
    .set("group.id", "my-group")
    // Missing: bootstrap.servers
    .create()?;

// Consumer not subscribed to topics
let consumer: StreamConsumer = /* created */;
// consumer.poll() returns None if not subscribed
```

## How to Fix

1. **Verify broker configuration and connectivity**

```rust
use rdkafka::consumer::{Consumer, StreamConsumer};
use rdkafka::config::ClientConfig;

let consumer: StreamConsumer = ClientConfig::new()
    .set("bootstrap.servers", "localhost:9092")
    .set("group.id", "my-group")
    .set("auto.offset.reset", "earliest")
    .set("enable.auto.commit", "false")
    .create()
    .expect("Failed to create consumer");
```

2. **Handle consumer errors with proper offset management**

```rust
use rdkafka::consumer::{Consumer, StreamConsumer};
use rdkafka::message::Message;
use std::time::Duration;

#[tokio::main]
async fn main() -> rdkafka::error::KafkaResult<()> {
    let consumer: StreamConsumer = ClientConfig::new()
        .set("bootstrap.servers", "localhost:9092")
        .set("group.id", "my-group")
        .create()?;

    consumer.subscribe(&["my-topic"])?;

    loop {
        match consumer.recv().await {
            Ok(msg) => {
                if let Some(Ok(payload)) = msg.payload_view::<str>() {
                    println!("Received: {}", payload);
                }
                consumer.commit_message(&msg, rdkafka::consumer::CommitMode::Async)?;
            }
            Err(e) => eprintln!("Error: {}", e),
        }
    }
}
```

3. **Configure producer with proper error handling**

```rust
use rdkafka::producer::{FutureProducer, FutureRecord};
use std::time::Duration;

async fn send_message(topic: &str, key: &str, payload: &str) -> Result<(), Box<dyn std::error::Error>> {
    let producer: FutureProducer = rdkafka::config::ClientConfig::new()
        .set("bootstrap.servers", "localhost:9092")
        .set("message.timeout.ms", "5000")
        .create()?;

    let delivery_status = producer
        .send(FutureRecord::to(topic).key(key).payload(payload), Duration::from_secs(5))
        .await?;

    println!("Delivered to partition {}", delivery_status.0);
    Ok(())
}
```

## Examples

```rust
use rdkafka::config::ClientConfig;
use rdkafka::producer::{FutureProducer, FutureRecord};
use rdkafka::consumer::{Consumer, StreamConsumer};
use rdkafka::message::Message;

#[tokio::main]
async fn main() -> rdkafka::error::KafkaResult<()> {
    // Producer
    let producer: FutureProducer = ClientConfig::new()
        .set("bootstrap.servers", "localhost:9092")
        .create()?;

    for i in 0..5 {
        let record = FutureRecord::to("test-topic")
            .key(&format!("key-{}", i))
            .payload(&format!("message-{}", i));
        producer.send(record, std::time::Duration::from_secs(0)).await?;
    }

    // Consumer
    let consumer: StreamConsumer = ClientConfig::new()
        .set("bootstrap.servers", "localhost:9092")
        .set("group.id", "test-group")
        .set("auto.offset.reset", "earliest")
        .create()?;

    consumer.subscribe(&["test-topic"])?;
    for _ in 0..5 {
        if let Ok(msg) = consumer.recv().await {
            if let Some(Ok(payload)) = msg.payload_view::<str>() {
                println!("Got: {}", payload);
            }
        }
    }
    Ok(())
}
```

## Related Errors

- [AMQP Error]({{< relref "/languages/rust/rust-amqp-error" >}}) — RabbitMQ messaging
- [NATS Error]({{< relref "/languages/rust/rust-nats-error" >}}) — NATS messaging
- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — broker unreachable
