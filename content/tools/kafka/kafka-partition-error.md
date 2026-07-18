---
title: "[Solution] Apache Kafka Partition Error"
description: "Fix Apache Kafka partition errors. Learn why this happens and how to resolve it quickly."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Apache Kafka Partition Error

Kafka partition errors occur when partitions fail to elect leaders, become unbalanced, or have data issues.

## Why This Happens

- Partition leader lost
- Under-replicated partition
- Partition offline
- ISR shrink

## Common Error Messages

- `partition_leader_lost`
- `partition_under_replicated`
- `partition_offline`
- `partition_isr_shrink`

## How to Fix It

### Solution 1: Check partition status

View partition status:

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic mytopic
```

### Solution 2: Reassign partitions

Use partition reassignment:

```bash
kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --reassignment-json-file reassignment.json --execute
```

### Solution 3: Monitor ISR

Check ISR size:

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic mytopic | grep -o 'Isr: [0-9]*'
```


## Common Scenarios

- **Partition offline:** Check broker health.
- **ISR shrink:** Verify broker connectivity and disk health.

## Prevent It

- Monitor partition balance
- Set replication factor appropriately
- Plan capacity
