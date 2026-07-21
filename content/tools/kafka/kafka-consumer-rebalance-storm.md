---
title: "[Solution] Kafka Consumer Rebalance Storm Error"
description: "Fix Kafka consumer rebalance storms. Resolve frequent rebalances destabilizing consumer group processing."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Consumer Rebalance Storm Error

Kafka consumer rebalance storms occur when a consumer group enters a continuous loop of rebalancing due to unstable members, aggressive timeouts, or excessive partition count.

## Common Causes

- Consumer sessions crashing or restarting repeatedly
- session.timeout.ms set too low relative to processing time
- Too many partitions with too few consumers
- Consumer instances competing for the same group

## How to Fix

1. Increase session and heartbeat timeouts:

```properties
session.timeout.ms=45000
heartbeat.interval.ms=15000
max.poll.interval.ms=300000
```

2. Use static group membership to avoid rebalance on restart:

```properties
group.instance.id=consumer-host-1
```

3. Increase max.poll.records to process fewer per poll:

```properties
max.poll.records=100
```

4. Monitor rebalance frequency:

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --group my-consumer-group --describe
```

## Examples

```bash
# Check consumer group coordinator
kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --group my-consumer-group --describe --state
```
