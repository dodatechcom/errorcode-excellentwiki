---
title: "[Solution] Neo4j Type Error — How to Fix"
description: "Fix Neo4j type errors including type mismatches in Cypher, property type issues, and type conversion problems"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Type Error

Type errors in Neo4j occur when Cypher operations encounter values of unexpected types. Neo4j supports INTEGER, FLOAT, STRING, BOOLEAN, DATE, TIME, DATETIME, DURATION, LIST, and MAP types.

## Why It Happens

- Comparing values of different types (e.g., INTEGER to STRING)
- Using a function that expects a specific type with a different type
- Property has mixed types across different nodes
- Implicit type conversion loses data
- The IN operator is used with wrong types

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: Type mismatch: expected Float but was Integer
```

```
Neo.ClientError.Statement.ExecutionFailed:
Cannot compare STRING and INTEGER
```

```
Neo.ClientError.Statement.SyntaxError: Expected a String but was Integer
```

```
Neo.ClientError.Statement.ExecutionFailed: Can't coerce Integer to Float
```

## How to Fix It

### 1. Fix Type Mismatch in Comparisons

```cypher
// BAD: comparing different types
MATCH (n:Person) WHERE n.age = '30' RETURN n;

// GOOD: ensure matching types
MATCH (n:Person) WHERE n.age = 30 RETURN n;

// Or cast to the correct type
MATCH (n:Person) WHERE toString(n.age) = '30' RETURN n;
```

### 2. Fix Type Mismatch in Functions

```cypher
// BAD: CONCAT expects strings
MATCH (n:Person) RETURN concat(n.name, n.age);

// GOOD: convert types explicitly
MATCH (n:Person) RETURN concat(n.name, ' ', toString(n.age));
```

### 3. Fix Mixed Property Types

```cypher
// Find nodes with different types on the same property
MATCH (n:Person)
WHERE NOT n.age IS INTEGER
RETURN n.name, n.age, toString(n.age) AS age_str;

// Standardize the type
MATCH (n:Person) WHERE NOT n.age IS INTEGER
SET n.age = toInteger(n.age);
```

### 4. Fix Type Conversion Issues

```cypher
// INTEGER to FLOAT (may lose precision)
RETURN toFloat(9007199254740993);  // loses precision

// STRING to INTEGER (may fail)
RETURN toInteger('abc');  // returns null

// SAFE conversion with default
RETURN coalesce(toInteger(n.age_string), 0);
```

## Common Scenarios

- **Imported data has wrong types**: Use SET with type conversion functions to standardize.
- **Function expects String but gets Integer**: Use toString() to convert.
- **Comparison fails with mixed types**: Ensure both sides of the comparison have matching types.

## Prevent It

- Define node schemas with consistent property types
- Use type conversion functions (toString, toInteger, toFloat) explicitly
- Test queries on staging with realistic data before deploying

## Related Pages

- [Neo4j Query Error](/tools/neo4j/neo4j-query-error)
- [Neo4j Cypher Syntax Error](/tools/neo4j/neo4j-cypher-syntax-error)
- [Neo4j Set Property Error](/tools/neo4j/neo4j-set-property-error)
