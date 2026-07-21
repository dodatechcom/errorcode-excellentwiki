---
title: "[Solution] Neo4j APOC Nodes Link Error"
description: "Fix Neo4j APOC link nodes errors when batch linking nodes by property value"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Nodes Link Error

APOC link errors occur when batch linking nodes by matching property values fails.

## Common Causes

- Link property not indexed causing slow lookup
- Duplicate property values causing multiple links
- Relationship type name invalid
- Source and target are same node

## Common Error Messages

```
apoc.exception.InvalidArgumentException: Multiple nodes match link key
```

## How to Fix It

### 1. Create Index on Link Property

```cypher
CREATE INDEX user_email IF NOT EXISTS FOR (u:User) ON (u.email);
```

### 2. Link Nodes Safely

```cypher
MATCH (a:User), (b:User)
WHERE a.managerEmail = b.email AND a <> b
MERGE (a)-[:REPORTS_TO]->(b);
```

### 3. Use APOC Link

```cypher
CALL apoc.nodes.link(
  [(n:User) WHERE n.department IS NOT NULL],
  'WORKS_IN',
  'department'
);
```

## Examples

```cypher
MATCH (e:Employee), (d:Department)
WHERE e.deptCode = d.code
MERGE (e)-[:BELONGS_TO]->(d);
```
