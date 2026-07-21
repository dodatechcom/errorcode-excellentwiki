---
title: "[Solution] Neo4j Database Recovery Error"
description: "How to fix Neo4j database recovery errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Transaction log corruption
- Store file corruption
- Unclean shutdown

## How to Fix

Check recovery:

```bash
neo4j-admin database recover mydb
```

## Examples

```bash
neo4j-admin database recover mydb --verbose
```
