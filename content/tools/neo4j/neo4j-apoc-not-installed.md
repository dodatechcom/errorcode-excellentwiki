---
title: "[Solution] Neo4j APOC Not Installed Error"
description: "How to fix Neo4j APOC plugin not installed errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- APOC JAR not in plugins directory
- APOC version incompatible with Neo4j version

## How to Fix

Install APOC:

```bash
cp apoc-*.jar /var/lib/neo4j/plugins/
sudo systemctl restart neo4j
```

## Examples

```bash
ls /var/lib/neo4j/plugins/
neo4j version
```
