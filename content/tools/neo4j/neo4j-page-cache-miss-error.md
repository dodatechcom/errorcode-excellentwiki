---
title: "[Solution] Neo4j Page Cache Miss Error"
description: "How to fix Neo4j page cache miss errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Page cache too small
- Data larger than allocated cache
- Cache eviction rate too high

## How to Fix

```ini
server.memory.pagecache.size=1G
```

## Examples

```cypher
CALL dbms.listConfig() YIELD name, value WHERE name = 'dbms.memory.pagecache.size'
```
