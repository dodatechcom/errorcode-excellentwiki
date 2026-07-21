---
title: "[Solution] Neo4j Disk Full Error"
description: "How to fix Neo4j disk full errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Data directory on full disk
- Transaction logs growing
- Store files too large

## How to Fix

Check disk usage:

```bash
df -h /var/lib/neo4j/
du -sh /var/lib/neo4j/data/
```

## Examples

```bash
df -h /var/lib/neo4j/
```
