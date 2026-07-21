---
title: "[Solution] Neo4j APOC Nodes Relationship Error"
description: "Fix Neo4j APOC relationship creation errors when batch creating nodes and relationships"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Nodes Relationship Error

APOC nodes relationship errors occur when batch operations creating multiple nodes and relationships fail.

## Common Causes

- Creating duplicate relationships in batch
- Relationship type exceeding max length
- Source or target node not found during batch
- Transaction size limit exceeded

## Common Error Messages

```
Neo.ClientError.General.TransactionTimedOut: Transaction exceeded timeout
```

## How to Fix It

### 1. Use APOC Periodic for Batch

```cypher
CALL apoc.periodic.iterate(
  'MATCH (a:User), (b:User) WHERE a <> b RETURN a, b',
  'MERGE (a)-[:KNOWS]->(b)',
  {batchSize: 500, parallel: false}
);
```

### 2. Create Relationships with APOC

```cypher
CALL apoc.create.relationships(
  [{name: 'Alice'}, {name: 'Bob'}],
  'KNOWS',
  {}
) YIELD rel RETURN rel;
```

### 3. Avoid Duplicate Relationships

```cypher
MATCH (a:User), (b:User)
WHERE a <> b AND NOT (a)-[:KNOWS]->(b)
WITH a, b LIMIT 1000
CREATE (a)-[:KNOWS]->(b);
```

## Examples

```cypher
CALL apoc.periodic.iterate(
  'MATCH (a:Company), (b:Employee) WHERE b.company = a.name RETURN a, b',
  'MERGE (a)-[:EMPLOYS]->(b)',
  {batchSize: 1000}
);
```
