---
title: "[Solution] Python kafka-python Error — Kafka Client Failures"
description: "Fix Python kafka-python errors like KafkaError, TopicNotFoundError, BrokerConnectionError, and consumer/producer errors. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 428
---

# Python kafka-python Error — Kafka Client Failures

kafka-python errors occur when brokers are unreachable, topics do not exist, consumer groups encounter rebalancing, or serialization fails. These are common in event-driven and streaming architectures.

## Common Causes

```python
# NoBrokersAvailable: cannot connect to any broker
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers="localhost:9092")

# TopicAuthorizationFailedError: not authorized to access topic
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers="localhost:9092")
producer.send("restricted-topic", b"message")

# CommitFailedError: consumer group offset commit failed
from kafka import KafkaConsumer
consumer = KafkaConsumer("my-topic", group_id="my-group", bootstrap_servers="localhost:9092")
consumer.commit()

# KafkaTimeoutError: operation timed out
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers="localhost:9092", request_timeout_ms=100)
producer.send("my-topic", b"message").get(timeout=0.01)

# SerializationError: cannot serialize message
producer = KafkaProducer(value_serializer=lambda v: v.encode("utf-8"))
producer.send("my-topic", 12345)  # int cannot be encoded
```

## How to Fix

### Fix 1: Verify Broker Connectivity
Ensure Kafka brokers are running and reachable.
```bash
# Check broker status
kafka-broker-api-versions.sh --bootstrap-server localhost:9092
```
```python
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

try:
    producer = KafkaProducer(bootstrap_servers="localhost:9092")
except NoBrokersAvailable:
    print("Cannot connect to Kafka broker. Check if Kafka is running.")
```

### Fix 2: Create Topics Before Producing
Ensure topics exist before sending messages.
```python
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAuthorizationFailedError

admin = KafkaAdminClient(bootstrap_servers="localhost:9092")
new_topic = NewTopic(name="my-topic", num_partitions=3, replication_factor=1)
try:
    admin.create_topics([new_topic])
except Exception as e:
    print(f"Topic creation: {e}")
```

### Fix 3: Handle Consumer Group Rebalancing
Implement proper commit strategies and rebalance callbacks.
```python
from kafka import KafkaConsumer

def on_partitions_assigned(partitions):
    print("Partitions assigned:", partitions)

def on_partitions_revoked(partitions):
    print("Partitions revoked:", partitions)

consumer = KafkaConsumer(
    "my-topic",
    group_id="my-group",
    bootstrap_servers="localhost:9092",
    enable_auto_commit=False,
    on_partitions_assigned=on_partitions_assigned,
    on_partitions_revoked=on_partitions_revoked,
)

for message in consumer:
    process(message)
    consumer.commit()
```

### Fix 4: Configure Proper Timeouts
Set appropriate timeout values for your use case.
```python
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    request_timeout_ms=30000,
    max_block_ms=60000,
    acks="all",
)

future = producer.send("my-topic", b"message")
record_metadata = future.get(timeout=10)
```

### Fix 5: Handle Serialization Errors
Use proper serializers and handle encoding issues.
```python
from kafka import KafkaProducer
import json

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=json_serializer,
)

producer.send("my-topic", {"key": "value", "number": 42})
```

## Examples

```python
# Complete producer with error handling
from kafka import KafkaProducer
from kafka.errors import KafkaError, KafkaTimeoutError
import json

def create_producer():
    return KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        acks="all",
        retries=3,
    )

def send_message(producer, topic, message):
    future = producer.send(topic, message)
    try:
        record_metadata = future.get(timeout=10)
        print(f"Sent to {record_metadata.topic} partition {record_metadata.partition}")
    except KafkaTimeoutError:
        print("Producer timed out waiting for broker response")
    except KafkaError as e:
        print(f"Failed to send message: {e}")
```

## Related Errors

- [Python PyMongo Error](/languages/python/python-pymongo-error/)
- [Python redis-py Error](/languages/python/python-redis-py-error/)
- [Python Elasticsearch Error](/languages/python/python-elasticsearch-error/)
