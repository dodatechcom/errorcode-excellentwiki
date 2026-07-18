---
title: "[Solution] Neo4j DETACH DELETE Error — How to Fix"
description: "Fix Neo4j DETACH DELETE errors including accidental bulk deletion, missing DETACH keyword, and cascade delete issues"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j DETACH DELETE Error

DETACH DELETE errors in Neo4j occur when trying to delete nodes without properly handling their relationships. Neo4j requires DETACH to remove a node and all its relationships.

## Why It Happens

- Trying to DELETE a node that has relationships without using DETACH
- The MATCH pattern in DELETE matches more nodes than intended
- The DETACH DELETE is too broad and removes unintended data
- The delete operation exceeds transaction timeout on large datasets
- The query is missing a WHERE clause causing full graph deletion

## Common Error Messages

```
Neo.ClientError.Schema.ConstraintValidationFailed:
Cannot delete node because it still has relationships
```

```
Neo.ClientError.Statement.ExecutionFailed:
Node is still connected to other nodes
```

```
Neo.TransientError.Transaction.TransactionTimedOut:
Transaction terminated while performing DELETE
```

```
Neo.ClientError.Statement.SyntaxError:
DELETE cannot be used to delete relationships
```

## How to Fix It

### 1. Use DETACH DELETE for Nodes

```cypher
// BAD: will fail if node has relationships
MATCH (n:Person {name: 'John'})
DELETE n;

// GOOD: removes node and all relationships
MATCH (n:Person {name: 'John'})
DETACH DELETE n;
```

### 2. Safely Delete Large Amounts of Data

```cypher
// Delete in batches to avoid timeout
MATCH (n:OldNodes)
WITH n LIMIT 10000
DETACH DELETE n;

// Repeat until 0 nodes deleted
```

### 3. Delete Only Specific Relationships

```cypher
// Delete specific relationships
MATCH (a:Person)-[r:KNOWS]->(b:Person)
WHERE a.name = 'John'
DELETE r;

// Delete all relationships of a type
MATCH ()-[r:OLD_REL_TYPE]-()
DELETE r;
```

### 4. Preview Before Deleting

```cypher
// Always check what will be deleted first
MATCH (n:OldLabel) RETURN count(n) AS nodesToDelete;

MATCH (n:OldLabel)-[r]-() RETURN count(r) AS relationshipsToDelete;

// Then delete
MATCH (n:OldLabel) DETACH DELETE n;
```

## Common Scenarios

- **Migration removes old labels**: Use batch DETACH DELETE to avoid timeout on millions of nodes.
- **Accidental broad DELETE without WHERE**: Always preview with RETURN before DELETE.
- **Delete all nodes**: `MATCH (n) DETACH DELETE n` deletes everything in the database.

## Prevent It

- Always preview DELETE queries with RETURN before executing DETACH DELETE
- Use batch deletion for large datasets to avoid transaction timeout
- Create database backups before running destructive DELETE operations

## Related Pages

- [Neo4j Query Error](/tools/neo4j/neo4j-query-error)
- [Neo4j Transaction Error](/tools/neo4j/neo4j-transaction-error)
- [Neo4j Backup Error](/tools/neo4j/neo4j-backup-error)
