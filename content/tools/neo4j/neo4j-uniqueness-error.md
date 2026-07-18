---
title: "[Solution] Neo4j Uniqueness Constraint Error — How to Fix"
description: "Fix Neo4j uniqueness constraint errors including creation on duplicate data, constraint removal, and uniqueness enforcement issues"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Uniqueness Constraint Error

Uniqueness constraint errors occur when creating constraints on data that already has duplicates, or when the constraint interferes with normal operations.

## Why It Happens

- Creating a uniqueness constraint on a property that has duplicate values
- The constraint creation query is incorrect for the Neo4j version
- The constraint was dropped and recreated while data was being modified
- The unique constraint conflicts with an existing index on the same property

## Common Error Messages

```
Neo.ClientError.Schema.ConstraintValidationFailed:
Node(123) already exists with label `Person` and property `email` = 'test@test.com'
```

```
Neo.ClientError.Schema.EquivalentSchemaRuleAlreadyExists:
An equivalent uniqueness constraint already exists
```

```
Neo.ClientError.Statement.SyntaxError:
Invalid constraint syntax for this Neo4j version
```

```
Neo.ClientError.Schema.ConstraintViolation:
Multiple nodes with label 'Person' have property 'email' = 'test@test.com'
```

## How to Fix It

### 1. Find and Fix Duplicates

```cypher
// Find duplicate email addresses
MATCH (n:Person)
WITH n.email AS email, count(*) AS cnt, collect(n) AS nodes
WHERE cnt > 1
RETURN email, cnt, [n IN nodes | id(n)] AS nodeIds;

// Remove duplicates, keeping the newest
MATCH (n:Person)
WITH n.email AS email, n
ORDER BY n.createdAt DESC
WITH email, collect(n) AS nodes
WHERE size(nodes) > 1
UNWIND nodes[1..] AS duplicate
DETACH DELETE duplicate;
```

### 2. Create Uniqueness Constraint Safely

```cypher
// Neo4j 4.x+ syntax
CREATE CONSTRAINT person_email_unique FOR (n:Person) REQUIRE n.email IS UNIQUE;

// Neo4j 3.x syntax (deprecated)
// CREATE CONSTRAINT ON (n:Person) ASSERT n.email IS UNIQUE;

// Check existing constraints
SHOW CONSTRAINTS;
```

### 3. Drop and Recreate Constraint

```cypher
// Drop the constraint
DROP CONSTRAINT person_email_unique IF EXISTS;

// Recreate it
CREATE CONSTRAINT person_email_unique FOR (n:Person) REQUIRE n.email IS UNIQUE;
```

### 4. Handle Constraint During Migration

```cypher
// 1. Drop constraint before migration
DROP CONSTRAINT person_email_unique IF EXISTS;

// 2. Run migration (add/update data)
// ... migration queries ...

// 3. Remove duplicates
MATCH (n:Person)
WITH n.email AS email, collect(n) AS nodes
WHERE size(nodes) > 1
UNWIND nodes[1..] AS dup
DETACH DELETE dup;

// 4. Recreate constraint
CREATE CONSTRAINT person_email_unique FOR (n:Person) REQUIRE n.email IS UNIQUE;
```

## Common Scenarios

- **Adding constraint to production data with duplicates**: Clean duplicates first using the query above.
- **Constraint creation is slow**: Wait for the index build to complete (check with `SHOW INDEXES`).
- **Constraint dropped and recreated during migration**: Ensure all data is consistent before recreating.

## Prevent It

- Always check for duplicates before creating uniqueness constraints
- Use `DROP ... IF EXISTS` and `CREATE ... IF NOT EXISTS` in migration scripts
- Test constraint creation on staging with production data before deploying

## Related Pages

- [Neo4j Constraint Error](/tools/neo4j/neo4j-constraint-error)
- [Neo4j Index Error](/tools/neo4j/neo4j-index-error)
- [Neo4j MERGE Error](/tools/neo4j/neo4j-merge-error)
