---
title: "[Solution] Neo4j APOC Configuration Error"
description: "How to fix Neo4j APOC configuration errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- APOC not in plugins directory
- Version mismatch
- Missing APOC config entries

## How to Fix

```ini
dbms.security.procedures.unrestricted=apoc.*
```

## Examples

```bash
ls /var/lib/neo4j/plugins/apoc*.jar
```
