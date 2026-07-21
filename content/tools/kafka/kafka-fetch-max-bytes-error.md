---
title: "[Solution] Kafka Fetch Max Bytes Error"
description: "Fix Kafka fetch.max.bytes errors. Resolve message fetching failures from large message batches."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Fetch Max Bytes Error

Kafka fetch.max.bytes errors occur when a consumer or follower replica requests more data in a single fetch request than the broker allows, causing partial or failed fetches.

## Common Causes

- fetch.max.bytes on broker set lower than consumer expectations
- Individual partition message batch larger than max.partition.fetch.bytes
- Consumer trying to fetch from many partitions simultaneously
- Large message sizes from compressed batches

## How to Fix

1. Increase fetch.max.bytes on the broker:

```properties
fetch.max.bytes=52428800
```

2. Set matching consumer-side limits:

```properties
max.partition.fetch.bytes=1048576
fetch.min.bytes=1
fetch.max.wait.ms=500
```

3. Check the actual message sizes in the topic:

```bash
kafka-run-class.sh kafka.tools.GetOffsetShell \
  --broker-list localhost:9092 \
  --topic my-topic --time -1
```

4. Reduce the number of partitions fetched per poll:

```java
Properties props = new Properties();
props.put("fetch.max.bytes", 52428800);
props.put("max.partition.fetch.bytes", 1048576);
```

## Examples

```bash
# Check message sizes per partition
for part in $(seq 0 5); do
  kafka-run-class.sh kafka.tools.GetOffsetShell \
    --broker-list localhost:9092 \
    --topic my-topic --partitions $part --time -1
done
```
