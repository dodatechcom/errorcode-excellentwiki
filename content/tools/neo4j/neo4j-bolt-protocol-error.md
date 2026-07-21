---
title: "[Solution] Neo4j Bolt Protocol Error"
description: "How to fix Neo4j Bolt protocol errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Client using wrong Bolt version
- Bolt connector not enabled
- SSL/TLS configuration mismatch

## How to Fix

Check Bolt configuration:

```
dbms.connector.bolt.enabled=true
dbms.connector.bolt.listen_address=:7687
```

## Examples

```bash
neo4j version
cat /etc/neo4j/neo4j.conf | grep bolt
```
