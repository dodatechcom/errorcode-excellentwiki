---
title: "[Solution] Neo4j Heap Memory Error"
description: "How to fix Neo4j heap memory out of memory errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Heap size too small
- Memory leak in query
- Too many concurrent transactions

## How to Fix

Increase heap:

```
server.memory.heap.initial_size=4g
server.memory.heap.max_size=4g
```

## Examples

```bash
grep heap /etc/neo4j/neo4j.conf
```
