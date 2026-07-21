---
title: "[Solution] Neo4j Label Not Found Error"
description: "Fix Neo4j label not found errors when queries reference labels that do not exist in the database"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Label Not Found Error

Label not found errors occur when a Cypher query references a node label that has not been created in the database.

## Common Causes

- Query references a label from a different database
- Label was dropped as part of schema cleanup
- Typo in the label name (case-sensitive)
- Label exists but has zero nodes

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: Invalid label 'OldLabel'
```

## How to Fix It

### 1. Verify Label Exists

```cypher
CALL db.labels() YIELD label RETURN label;
```

### 2. Create Nodes with the Label

```cypher
CREATE (n:NewLabel {name: 'example'});
```

### 3. Rename Labels Using Batch Operation

```cypher
MATCH (n:OldLabel)
SET n:NewLabel
REMOVE n:OldLabel;
```

## Examples

```cypher
CALL db.labels() YIELD label
CALL apoc.cypher.run('MATCH (n:' + label + ') RETURN count(n) AS cnt', {}) YIELD value
RETURN label, value.cnt AS nodeCount;
```
