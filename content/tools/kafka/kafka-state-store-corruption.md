---
title: "[Solution] Kafka Streams State Store Corruption Error"
description: "Fix Kafka Streams state store corruption errors. Recover from corrupted local state store directories."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Streams State Store Corruption Error

Kafka Streams state store corruption errors occur when the RocksDB-backed local state store becomes unreadable due to filesystem corruption, crash during compaction, or disk failure.

## Common Causes

- Unclean shutdown during a state store compaction
- Disk I/O error writing to the state store directory
- RocksDB WAL file corruption after power failure
- Insufficient disk space for state store growth

## How to Fix

1. Delete the local state store directory to trigger a full restoration:

```bash
rm -rf /tmp/kafka-streams/my-app/*
```

2. Configure the application to start from scratch:

```java
props.put(StreamsConfig.APPLICATION_RESET_CONFIG, "earliest");
props.put(StreamsConfig.STATE_DIR_CONFIG, "/tmp/kafka-streams/my-app");
```

3. Start the application and allow it to restore from the changelog topic:

```bash
kafka-topics.sh --describe --bootstrap-server localhost:9092 \
  --topic my-app-changelog
```

4. Increase state store cleanup frequency:

```properties
rocksdb.cache.index.and.filter.blocks=true
rocksdb.block.cache.size=52428800
```

## Examples

```bash
# Check state store directory size
du -sh /tmp/kafka-streams/my-app/*

# Verify changelog topic exists
kafka-topics.sh --list --bootstrap-server localhost:9092 | grep changelog
```
