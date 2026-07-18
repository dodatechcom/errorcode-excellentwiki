---
title: "[Solution] Apache Kafka Consumer Error"
description: "Fix Apache Kafka consumer errors. Learn why this happens and how to resolve it quickly."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Apache Kafka Consumer Error

Kafka consumer errors occur when consumers fail to connect, process messages, or manage offsets.

## Why This Happens

- Consumer not connected
- Offset out of range
- Consumer group rebalance
- Max poll exceeded

## Common Error Messages

- `consumer_connection_error`
- `consumer_offset_error`
- `consumer_rebalance_error`
- `consumer_poll_error`

## How to Fix It

### Solution 1: Check consumer status

View consumer group status:

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group mygroup
```

### Solution 2: Reset offsets

Reset consumer offsets:

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group mygroup --reset-offsets --to-earliest --topic mytopic --execute
```

### Solution 3: Fix poll interval

Adjust max.poll.interval.ms:

```properties
max.poll.interval.ms=300000
```


## Common Scenarios

- **Consumer not connecting:** Check broker connectivity.
- **Offset out of range:** Reset consumer offsets.

## Prevent It

- Monitor consumer lag
- Set appropriate poll intervals
- Handle rebalances gracefully
