---
title: "[Solution] rdkafka Kafka Error Fix"
description: "Fix rdkafka Kafka errors. Handle broker connectivity, consumer groups, and producer acknowledgment."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Rdkafka Error

Rdkafka errors occur when using the `rdkafka` crate for Kafka — broker connection failures and serialization issues.

## Common Causes

```rust
// Broker unreachable
let producer: BaseProducer<_ = BaseProducerConfig::new()
    .set("bootstrap.servers", "wrong:9092")
    .create()?;

// Message too large for broker
let future = producer.send(DeliveryResult::...);
```

## How to Fix

1. **Configure producer/consumer correctly**

```rust
use rdkafka::config::ClientConfig;
use rdkafka::producer::{BaseProducer, BaseRecord};

let producer: BaseProducer<_ = ClientConfig::new()
    .set("bootstrap.servers", "localhost:9092")
    .set("message.timeout.ms", "5000")
    .create()?;
```

2. **Handle delivery errors**

```rust
use rdkafka::producer::{BaseProducer, BaseRecord, DeliveryResult};

producer.send(
    BaseRecord::to("my_topic").key("key").payload("value"),
    |result: DeliveryResult| {
        match result {
            Ok(_) => println!("Message delivered"),
            Err((e, _)) => eprintln!("Delivery failed: {}", e),
        }
    },
)?;
```

3. **Configure consumer groups**

```rust
use rdkafka::consumer::{StreamConsumer, Consumer};
use rdkafka::config::ClientConfig;

let consumer: StreamConsumer<_ = ClientConfig::new()
    .set("bootstrap.servers", "localhost:9092")
    .set("group.id", "my_group")
    .set("auto.offset.reset", "earliest")
    .create()?;
```

## Examples

```rust
use rdkafka::config::ClientConfig;
use rdkafka::producer::{BaseProducer, BaseRecord};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let producer: BaseProducer<_ = ClientConfig::new()
        .set("bootstrap.servers", "localhost:9092")
        .create()?;

    producer.send(
        BaseRecord::to("test_topic").key("key").payload("Hello Kafka!"),
        |result| {
            if let Err((e, _)) = eprintln!("Error: {}", e);
        },
    )?;
    producer.flush(std::time::Duration::from_secs(1));
    Ok(())
}
```

## Related Errors

- [Kafka Error]({{< relref "/languages/rust/rust-kafka-error-rs" >}}) — Kafka errors
- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — network
- [Tokio Error]({{< relref "/languages/rust/tokio-error" >}}) — async runtime
