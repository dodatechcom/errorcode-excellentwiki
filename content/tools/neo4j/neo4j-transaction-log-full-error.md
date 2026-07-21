---
title: "[Solution] Neo4j Transaction Log Full Error"
description: "Fix Neo4j transaction log full errors when logs consume all available disk space"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Transaction Log Full Error

Transaction log full errors occur when Neo4j cannot write more transaction data due to disk space exhaustion.

## Common Causes

- Transaction log files not being pruned
- Large transactions creating excessive log entries
- Disk space too small for transaction volume
- Log rotation configuration missing

## Common Error Messages

```
Java.io.IOException: No space left on device
```

## How to Fix It

### 1. Check Transaction Log Size

```bash
ls -lh /var/lib/neo4j/data/transactions/
```

### 2. Configure Log Pruning

```properties
# neo4j.conf
dbms.tx_log.rotation.size=250M
dbms.tx_log.rotation.retention_policy=7 days
```

### 3. Force Log Rotation

```bash
curl -X POST http://localhost:7474/db/manage/server/txlog-rotate
```

## Examples

```bash
du -sh /var/lib/neo4j/data/
```
