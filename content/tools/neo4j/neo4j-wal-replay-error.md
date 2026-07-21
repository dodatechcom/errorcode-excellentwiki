---
title: "[Solution] Neo4j WAL Replay Error"
description: "How to fix Neo4j WAL replay errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- WAL file corrupted
- WAL directory not writable
- Crash during WAL flush

## How to Fix

```bash
ls -la /var/lib/neo4j/data/transactions/
```

## Examples

```bash
neo4j-admin database info mydb
```
