---
title: "[Solution] Neo4j Graph Data Science Library Error"
description: "How to fix Neo4j GDS library errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- GDS plugin not installed
- GDS version incompatible with Neo4j
- Memory limit exceeded for algorithm

## How to Fix

Install GDS:

```bash
cp neo4j-graph-data-science-*.jar /var/lib/neo4j/plugins/
sudo systemctl restart neo4j
```

## Examples

```cypher
CALL gds.list() YIELD name;
```
