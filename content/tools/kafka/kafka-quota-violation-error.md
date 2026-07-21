---
title: "[Solution] Kafka Quota Violation Error"
description: "Fix Kafka quota violation errors. Resolve producer or consumer throttling from broker quota enforcement."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Quota Violation Error

Kafka quota violation errors occur when a producer or consumer exceeds its configured byte-rate quota, causing the broker to throttle the client.

## Common Causes

- Default producer/consumer quota too low for the workload
- Producer sending a burst of data exceeding the quota
- Consumer reading faster than the configured quota allows
- Quota misconfigured for a specific client-id

## How to Fix

1. Check the current quota configuration:

```bash
kafka-configs.sh --describe --bootstrap-server localhost:9092 \
  --entity-type clients --entity-name my-producer
```

2. Set a higher quota for the producer:

```bash
kafka-configs.sh --bootstrap-server localhost:9092 \
  --alter --add-config 'producer_byte_rate=104857600' \
  --entity-type clients --entity-name my-producer
```

3. Set consumer quota:

```bash
kafka-configs.sh --bootstrap-server localhost:9092 \
  --alter --add-config 'consumer_byte_rate=209715200' \
  --entity-type clients --entity-name my-consumer
```

4. Monitor throttled clients in the broker logs:

```bash
grep -i "throttle\|quota" /var/log/kafka/server.log | tail -20
```

## Examples

```bash
# List all client quotas
kafka-configs.sh --describe --bootstrap-server localhost:9092 \
  --entity-type clients

# Remove a quota override
kafka-configs.sh --bootstrap-server localhost:9092 \
  --alter --delete-config producer_byte_rate \
  --entity-type clients --entity-name my-producer
```
