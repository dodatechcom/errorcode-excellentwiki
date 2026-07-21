---
title: "[Solution] Neo4j Transaction Log Full Error"
description: "How to fix Neo4j transaction log full errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Transaction logs consuming too much disk
- Retention period too long

## How to Fix

Check log size:

```bash
du -sh /var/lib/neo4j/data/transactions/
```

Adjust retention:

```
dbms.tx_log.rotation.retention_policy=7 days
```

## Examples

```bash
du -sh /var/lib/neo4j/data/transactions/
grep tx_log /etc/neo4j/neo4j.conf
```
