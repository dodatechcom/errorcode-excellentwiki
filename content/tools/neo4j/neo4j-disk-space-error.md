---
title: "[Solution] Neo4j Disk Space Error"
description: "How to fix Neo4j disk space errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Transaction log growth
- Store files growing unbounded
- Temp files not cleaned

## How to Fix

```ini
dbms.tx_log.rotation.size=100M
```

## Examples

```bash
du -sh /var/lib/neo4j/data/databases/mydb/
```
