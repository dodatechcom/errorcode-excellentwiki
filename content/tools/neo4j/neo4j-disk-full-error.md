---
title: "[Solution] Neo4j Disk Full Error"
description: "Fix Neo4j disk full errors when database files exhaust available storage"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Disk Full Error

Disk full errors occur when Neo4j cannot write data because the filesystem has run out of space.

## Common Causes

- Transaction logs growing without pruning
- Database dump files consuming space
- Backup files left on same volume
- Temp files from large queries not cleaned up

## Common Error Messages

```
Java.io.IOException: No space left on device
```

## How to Fix It

### 1. Check Disk Usage

```bash
df -h /var/lib/neo4j/data/
```

### 2. Clean Transaction Logs

```bash
find /var/lib/neo4j/data/transactions/ -name "*.log" -mtime +7 -delete
```

### 3. Enable Log Pruning

```properties
# neo4j.conf
dbms.tx_log.rotation.retention_policy=7 days
dbms.tx_log.rotation.size=250M
```

## Examples

```bash
du -sh /var/lib/neo4j/data/*
```
