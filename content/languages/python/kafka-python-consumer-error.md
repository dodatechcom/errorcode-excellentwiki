---
title: "[Solution] Kafka Python No Brokers Available Fix"
description: "Fix Kafka no brokers available error. Verify broker addresses, check network connectivity, and configure consumer/producer correctly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["kafka", "consumer", "broker", "no-brokers", "messaging"]
weight: 5
---

# Kafka Python: No Brokers Available Fix

A `kafka.errors.NoBrokersAvailable` error is raised when the kafka-python client cannot connect to any Kafka broker in the cluster.

## What This Error Means

Common messages:

- `kafka.errors.NoBrokersAvailable: NoBrokersAvailable`
- `NoBrokersAvailable: unable to bootstrap from [('broker1', 9092)]`
- `ConnectionError: [Errno 111] Connection refused`

The Kafka client attempted to connect to the specified broker addresses but none responded. This indicates the brokers are down, unreachable, or misconfigured.

## Common Causes

```python
from kafka import KafkaConsumer, KafkaProducer

# Cause 1: Broker not running
consumer = KafkaConsumer("my-topic", bootstrap_servers="localhost:9092")  # NoBrokersAvailable

# Cause 2: Wrong broker address
consumer = KafkaConsumer("my-topic", bootstrap_servers="wrong-host:9092")

# Cause 3: Firewall blocking port 9092
consumer = KafkaConsumer("my-topic", bootstrap_servers="10.0.0.5:9092")

# Cause 4: SASL/auth required but not configured
consumer = KafkaConsumer("my-topic", bootstrap_servers="broker:9092")  # Auth required
```

## How to Fix

### Fix 1: Verify Kafka broker is running

```bash
# Check if Kafka is running
docker ps | grep kafka

# Check broker ports
netstat -tlnp | grep 9092

# List topics from command line
kafka-topics.sh --bootstrap-server localhost:9092 --list
```

### Fix 2: Configure multiple brokers for resilience

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "my-topic",
    bootstrap_servers=[
        "broker1:9092",
        "broker2:9092",
        "broker3:9092",
    ],
    api_version=(3, 5, 0),
)
```

### Fix 3: Set connection timeout and retries

```python
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="broker:9092",
    api_version=(3, 5, 0),
    request_timeout_ms=10000,
    metadata_max_age_ms=30000,
    reconnect_backoff_ms=1000,
    reconnect_backoff_max_ms=30000,
)
```

### Fix 4: Add authentication if required

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "my-topic",
    bootstrap_servers="broker:9092",
    security_protocol="SASL_SSL",
    sasl_mechanism="PLAIN",
    sasl_username="user",
    sasl_password="pass",
    ssl_cafile="/path/to/ca.crt",
)
```

### Fix 5: Handle connection errors gracefully

```python
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

try:
    consumer = KafkaConsumer("my-topic", bootstrap_servers="broker:9092")
except NoBrokersAvailable:
    print("Kafka brokers not available. Check broker status and network.")
```

## Related Errors

- {{< relref "importerror-kafka" >}} — Kafka Python client import issue.
- {{< relref "connectionrefusederror" >}} — Python connection refused error.
