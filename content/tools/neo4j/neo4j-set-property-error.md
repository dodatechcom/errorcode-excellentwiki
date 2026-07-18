---
title: "[Solution] Neo4j SET Property Error — How to Fix"
description: "Fix Neo4j SET property errors including type mismatches, null handling, and property assignment issues in Cypher queries"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j SET Property Error

SET property errors in Neo4j occur when Cypher queries attempt to set node or relationship properties with incorrect types, missing values, or invalid expressions.

## Why It Happens

- Setting a property to a value of the wrong type
- Using SET with a null value (properties are removed when set to null)
- The SET expression references an undefined variable
- Setting a property on a relationship that does not exist
- The property name contains special characters without backticks
- Using SET on a path variable instead of individual nodes

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: Variable `n` not defined
```

```
Neo.ClientError.Statement.SyntaxError: Invalid property key
```

```
Neo.ClientError.Statement.ExecutionFailed:
Cannot set property on null value
```

```
Neo.ClientError.Statement.SyntaxError: Expected SET to follow WHERE
```

## How to Fix It

### 1. Fix Undefined Variable in SET

```cypher
// BAD: 'x' is not defined
MATCH (n:Person) SET x.name = 'test';

// GOOD: use the matched variable
MATCH (n:Person) SET n.name = 'test';
```

### 2. Handle NULL Values in SET

```cypher
// Setting to null removes the property
MATCH (n:Person) SET n.nickname = null;  // removes nickname

// GOOD: use coalesce for defaults
MATCH (n:Person) SET n.nickname = coalesce(n.nickname, 'unknown');
```

### 3. Fix Property Type Mismatches

```cypher
// BAD: setting a String to an Integer property
MATCH (n:Person) SET n.age = 'thirty';

// GOOD: use correct type
MATCH (n:Person) SET n.age = 30;

// Or use toInteger for conversions
MATCH (n:Person) SET n.age = toInteger(n.age_string);
```

### 4. Use SET with Multiple Properties

```cypher
// Set multiple properties at once
MATCH (n:Person {email: 'john@example.com'})
SET n.name = 'John', n.age = 30, n.updatedAt = datetime();

// Copy properties from one node to another
MATCH (source:Person {id: 1}), (target:Person {id: 2})
SET target += source;
```

### 5. Fix Property Key with Special Characters

```cypher
// BAD: property key with special characters
MATCH (n) SET n.first-name = 'John';

// GOOD: use backticks
MATCH (n) SET n.`first-name` = 'John';
```

## Common Scenarios

- **Property accidentally removed**: SET to null removes the property. Use coalesce to preserve existing values.
- **Wrong type causes query failure**: Validate data types before setting properties.
- **Setting properties on null node**: The MATCH returned no results. Check the MATCH pattern.

## Prevent It

- Always validate MATCH results before SET operations
- Use `RETURN` before `SET` to preview which nodes will be affected
- Use coalesce() to handle null values safely

## Related Pages

- [Neo4j Query Error](/tools/neo4j/neo4j-query-error)
- [Neo4j Cypher Syntax Error](/tools/neo4j/neo4j-cypher-syntax-error)
- [Neo4j Type Error](/tools/neo4j/neo4j-type-error)
