---
title: "[Solution] Neo4j Discovery Service Error"
description: "How to fix Neo4j cluster discovery errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Discovery service not configured
- Wrong discovery address
- Firewall blocking discovery port

## How to Fix

Configure discovery:

```
dbms.mode=CORE
dbms.discovery.type=LIST
dbms.discovery.initial_discovery_members=core1:5000,core2:5000,core3:5000
```

## Examples

```bash
grep discovery /etc/neo4j/neo4j.conf
```
