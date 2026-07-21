---
title: "[Solution] Neo4j ID Type Error"
description: "Fix Neo4j internal ID type errors when using deprecated ID() function with wrong arguments"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j ID Type Error

ID type errors occur when using the internal ID() function incorrectly or with unsupported arguments.

## Common Causes

- Passing string to ID() function instead of node/relationship
- Using ID() on deleted node
- Comparing internal IDs across databases
- ID() used on variable not in scope

## Common Error Messages

```
Neo.ClientError.Statement.TypeError: Expected a node but was Integer
```

## How to Fix It

### 1. Use ElementId Instead

```cypher
MATCH (n:User) RETURN elementId(n) AS uniqueId;
```

### 2. Use Natural Keys

```cypher
MATCH (n:User {email: 'alice@example.com'}) RETURN n;
```

### 3. Check Node Before Using ID

```cypher
MATCH (n:User)
WHERE id(n) = $nodeId
RETURN n IS NOT NULL AS exists;
```

## Examples

```cypher
MATCH (n:User)
RETURN elementId(n), n.name;
```
