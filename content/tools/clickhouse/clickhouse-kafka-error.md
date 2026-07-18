---
title: "[Solution] ClickHouse Kafka Engine Error — How to Fix"
description: "Fix ClickHouse Kafka engine errors including consumer failures, message parsing issues, and Kafka topic connection problems"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Kafka Engine Error

Kafka engine errors in ClickHouse occur when the Kafka table engine cannot connect to Kafka brokers, consume messages, or parse incoming data.

## Why It Happens

- The Kafka broker is unreachable
- The consumer group ID conflicts with other consumers
- The topic does not exist or has been deleted
- Message format does not match the table schema
- The consumer offset is too old and data has been deleted
- Too many partitions overwhelm the consumer

## Common Error Messages

```
Code: 474. DB::Exception: Failed to subscribe to topic
```

```
Code: 210. DB::Exception: Connection refused to Kafka broker
```

```
Code: 62. DB::Exception: Failed to parse Kafka message
```

```
Code: 474. DB::Exception: Kafka consumer error: Broker: Topic authorization failed
```

## How to Fix It

### 1. Check Kafka Connection

```bash
# Test Kafka broker connectivity
kafka-broker-api-versions --bootstrap-listener localhost:9092

# Check topic existence
kafka-topics --bootstrap-server localhost:9092 --list

# Check consumer group
kafka-consumer-groups --bootstrap-server localhost:9092 --list
```

### 2. Fix Kafka Engine Table Definition

```sql
CREATE TABLE kafka_events (
  id UInt64,
  message String,
  event_time DateTime
) ENGINE = Kafka
SETTINGS
  kafka_broker_list = 'localhost:9092',
  kafka_topic_list = 'my_topic',
  kafka_group_name = 'clickhouse_consumer',
  kafka_format = 'JSONEachRow',
  kafka_num_consumers = 2;
```

### 3. Fix Consumer Group Issues

```sql
-- Check consumer status
SELECT * FROM system.kafka_consumers;

-- Reset consumer group offset
-- Use kafka-consumer-groups CLI tool
kafka-consumer-groups --bootstrap-server localhost:9092   --group clickhouse_consumer --reset-offsets --to-earliest --execute --topic my_topic
```

### 4. Fix Message Format Issues

```sql
-- Ensure table schema matches message format
-- For JSON messages, the column names must match the JSON keys

-- For Avro messages
CREATE TABLE kafka_avro (
  id UInt64,
  name String
) ENGINE = Kafka
SETTINGS
  kafka_broker_list = 'localhost:9092',
  kafka_topic_list = 'avro_topic',
  kafka_group_name = 'avro_consumer',
  kafka_format = 'Avro';
```

## Common Scenarios

- **Kafka consumer stops after broker restart**: The consumer offset may be stale. Reset offset and restart.
- **Messages not appearing in ClickHouse**: The topic name or consumer group is wrong. Verify with `system.kafka_consumers`.
- **Schema mismatch causes message drops**: Ensure table columns match message fields exactly.

## Prevent It

- Monitor `system.kafka_consumers` for consumer lag and errors
- Use a dedicated consumer group for ClickHouse to avoid conflicts
- Test Kafka integration with sample messages before production deployment

## Related Pages

- [ClickHouse Connection Error](/tools/clickhouse/clickhouse-connection-error)
- [ClickHouse Table Error](/tools/clickhouse/clickhouse-table-error)
- [ClickHouse Format Error](/tools/clickhouse/clickhouse-format-error)
