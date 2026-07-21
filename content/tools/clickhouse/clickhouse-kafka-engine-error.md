---
title: "[Solution] ClickHouse Kafka Engine Error"
description: "How to fix ClickHouse Kafka engine errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Kafka broker unreachable
- Consumer group not initialized
- Topic does not exist
- Schema registry connection failed

## How to Fix

Create Kafka table:

```sql
CREATE TABLE kafka_queue (
  id UInt64,
  message String
) ENGINE = Kafka
SETTINGS
  kafka_broker_list = 'kafka:9092',
  kafka_topic_list = 'my-topic',
  kafka_group_name = 'clickhouse-group',
  kafka_format = 'JSONEachRow';
```

## Examples

```sql
SELECT * FROM system.tables WHERE engine = 'Kafka';
SELECT * FROM kafka_queue LIMIT 10;
```
