---
title: "[Solution] Python kafka-python Error — How to Fix"
description: "Fix Python kafka-python errors. Resolve broker connection, offset, and consumer group issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python kafka-python Error

A `kafka.errors.NoBrokersAvailable` or `kafka.errors.ConsumerTimeoutError` occurs when kafka-python fails to connect to brokers, encounters offset issues, or when consumer group coordination fails.

## Why It Happens

kafka-python is a Kafka client library. Errors arise when no brokers are available, when the consumer group coordinator is unavailable, when offsets are out of range, or when message deserialization fails.

## Common Error Messages

- `NoBrokersAvailable: NoBrokersAvailable`
- `ConsumerTimeoutError: Timeout`
- `OffsetOutOfRangeError: Offset is out of range`
- `CommitFailedError: CommitFailedError`

## How to Fix It

### Fix 1: Configure producer properly

```python
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

# Wrong — no timeout or retry configuration
# producer = KafkaProducer(bootstrap_servers=["localhost:9092"])

# Correct — configure with retry and timeout
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    request_timeout_ms=30000,
    retries=3,
    acks="all",
    value_serializer=lambda v: v.encode("utf-8"),
)

# Send message
future = producer.send("my-topic", value="Hello Kafka")
record_metadata = future.get(timeout=10)
print(f"Sent to {record_metadata.topic} partition {record_metadata.partition}")
```

### Fix 2: Handle consumer properly

```python
from kafka import KafkaConsumer
from kafka.errors import ConsumerTimeoutError

# Wrong — no timeout, may hang forever
# consumer = KafkaConsumer("my-topic")

# Correct — configure consumer with timeout
consumer = KafkaConsumer(
    "my-topic",
    bootstrap_servers=["localhost:9092"],
    group_id="my-group",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    consumer_timeout_ms=5000,
)

try:
    for message in consumer:
        print(f"Topic: {message.topic}, Partition: {message.partition}")
        print(f"Offset: {message.offset}, Key: {message.key}")
        print(f"Value: {message.value.decode()}")
except ConsumerTimeoutError:
    print("No more messages")

consumer.close()
```

### Fix 3: Manage offsets correctly

```python
from kafka import KafkaConsumer, TopicPartition

consumer = KafkaConsumer(
    bootstrap_servers=["localhost:9092"],
    group_id="my-group",
    enable_auto_commit=False,
)

# Manually assign partition and offset
partition = TopicPartition("my-topic", 0)
consumer.assign([partition])

# Seek to specific offset
consumer.seek(partition, 0)

# Read messages
for _ in range(5):
    message = consumer.poll(timeout_ms=1000)
    if message:
        print(f"Offset: {message.offset}, Value: {message.value.decode()}")
        consumer.commit()

consumer.close()
```

### Fix 4: Handle serialization errors

```python
from kafka import KafkaProducer, KafkaConsumer
import json

# Wrong — no serializer specified
# producer = KafkaProducer(bootstrap_servers=["localhost:9092"])
# producer.send("topic", value={"key": "value"})  # TypeError

# Correct — use proper serializers
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    key_serializer=lambda k: k.encode("utf-8") if k else None,
)

producer.send("my-topic", key="user-1", value={"name": "Alice", "age": 25})

consumer = KafkaConsumer(
    "my-topic",
    bootstrap_servers=["localhost:9092"],
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    key_deserializer=lambda k: k.decode("utf-8") if k else None,
)

for message in consumer:
    print(f"Key: {message.key}, Value: {message.value}")
    break
```

## Common Scenarios

- **No brokers available** — Kafka broker not running or not accessible on the configured port.
- **Offset out of range** — Consumer tries to read an offset that has been deleted by the broker.
- **Consumer timeout** — No messages available within the configured timeout period.

## Prevent It

- Always set `acks="all"` on producers for reliable message delivery.
- Use `enable_auto_commit=False` with explicit commits for exactly-once semantics.
- Handle `ConsumerTimeoutError` in consumer loops to allow graceful shutdown.

## Related Errors

- [NoBrokersAvailable](/languages/python/no-brokers/) — cannot connect to Kafka
- [ConsumerTimeoutError](/languages/python/timeouterror/) — consumer poll timeout
- [OffsetOutOfRangeError](/languages/python/offset-error/) — invalid offset
