---
title: "[Solution] Apache Kafka Broker Error"
description: "Fix Apache Kafka broker errors. Learn why this happens and how to resolve it quickly."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Apache Kafka Broker Error

Kafka broker errors occur when brokers fail to start, become unavailable, or lose synchronization.

## Why This Happens

- Broker not available
- Leader election failed
- Under-replicated partitions
- Controller unavailable

## Common Error Messages

- `broker_not_available`
- `broker_leader_error`
- `broker_under_replicated`
- `broker_controller_error`

## How to Fix It

### Solution 1: Check broker status

View broker status:

```bash
kafka-broker-api-versions.sh --bootstrap-server localhost:9092
```

### Solution 2: Fix leader election

Check under-replicated partitions:

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions
```

### Solution 3: Check controller

Verify controller is available:

```bash
kafka-metadata.sh --snapshot /path/to/metadata.log
```


## Common Scenarios

- **Broker not responding:** Check if the broker process is running.
- **Leader election stuck:** Verify ZooKeeper/KRaft connectivity.

## Prevent It

- Monitor broker health
- Set up replication
- Plan capacity
