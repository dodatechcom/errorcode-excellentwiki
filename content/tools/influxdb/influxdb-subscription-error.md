---
title: "[Solution] InfluxDB Subscription Error — How to Fix"
description: "Fix InfluxDB subscription errors including subscription creation failures, Kafka subscription issues, and data forwarding problems"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Subscription Error

Subscription errors in InfluxDB occur when creating, managing, or using subscriptions to forward data to other InfluxDB instances or Kafka topics.

## Why It Happens

- The subscription endpoint is unreachable
- The subscription type is not supported (Kafka vs HTTP)
- The target InfluxDB instance is not configured to receive subscriptions
- The subscription name already exists
- Network firewall blocks the subscription connection

## Common Error Messages

```
error: subscription already exists
```

```
error: failed to create subscription: connection refused
```

```
subscription error: kafka broker unreachable
```

```
error: subscription type not supported
```

## How to Fix It

### 1. Create Subscription

```influxql
-- HTTP subscription
CREATE SUBSCRIPTION "sub0" ON "mydb".
  DESTINATIONS ALL 'http://replica-host:8086'

-- Kafka subscription
CREATE SUBSCRIPTION "kafka_sub" ON "mydb".
  DESTINATIONS ALL 'kafka://broker1:9092,topic=mydb'
```

### 2. Check Subscriptions

```influxql
SHOW SUBSCRIPTIONS
```

### 3. Drop Subscription

```influxql
DROP SUBSCRIPTION "sub0" ON "mydb"
```

### 4. Fix Kafka Subscription

```bash
# Ensure Kafka broker is reachable
telnet kafka-host 9092

# Check Kafka topic exists
kafka-topics --bootstrap-server kafka-host:9092 --list
```

## Common Scenarios

- **Subscription fails to connect**: Ensure the target is reachable and accepting data.
- **Kafka subscription drops messages**: Check Kafka broker health and topic configuration.
- **Subscription already exists**: Drop the existing subscription first.

## Prevent It

- Test subscriptions on staging before production
- Monitor subscription lag and throughput
- Use HTTP subscriptions for simpler setups, Kafka for high-throughput

## Related Pages

- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Connection Error](/tools/influxdb/influxdb-connection-error)
- [InfluxDB Meta Error](/tools/influxdb/influxdb-meta-error)
