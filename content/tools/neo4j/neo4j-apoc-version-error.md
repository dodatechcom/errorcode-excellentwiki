---
title: "[Solution] Neo4j APOC Version Error"
description: "How to fix Neo4j APOC version mismatch errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- APOC version does not match Neo4j version
- Using APOC Full instead of APOC Core or vice versa

## How to Fix

Match versions:

```bash
neo4j version  # e.g., 5.x
# Use apoc-5.x.x.jar for Neo4j 5.x
```

## Examples

```bash
ls /var/lib/neo4j/plugins/apoc-
neo4j version
```
