---
title: "[Solution] ClickHouse Kafka Engine Error"
description: "Fix ClickHouse Kafka engine errors when consuming or producing messages fails"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Kafka Engine Error

Kafka engine errors occur when ClickHouse cannot read from or write to Kafka topics.

## Common Causes

- Kafka broker unreachable
- Consumer group already in use
- Topic does not exist in Kafka cluster
- Schema registry connection failure

## How to Fix

Check Kafka engine status:

```sql
SELECT database, table, engine FROM system.tables WHERE engine = 'Kafka';
```

Check Kafka consumer lag:

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group clickhouse
```

Verify topic exists:

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --list
```

## Examples

```sql
CREATE TABLE kafka_queue (message String)
ENGINE = Kafka
SETTINGS kafka_broker_list = 'kafka1:9092',
         kafka_topic_list = 'my_topic',
         kafka_group_name = 'clickhouse',
         kafka_format = 'JSONEachRow';
```
