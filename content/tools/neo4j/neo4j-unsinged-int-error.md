---
title: "[Solution] Neo4j Unsigned Integer Error — How to Fix"
description: "Fix Neo4j unsigned integer errors including Neo4j 4.x type changes, integer overflow, and type conversion issues"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Unsigned Integer Error

Unsigned integer errors in Neo4j occur when using integer values that exceed the valid range or when migrating from Neo4j 3.x where unsigned integers were supported differently.

## Why It Happens

- Neo4j 4.x removed unsigned integer types (INTEGER only, -2^63 to 2^63-1)
- A value exceeds the valid range for Neo4j INTEGER
- Type conversion between INTEGER and FLOAT causes precision loss
- Property values overflow during arithmetic operations
- The query tries to use unsigned integer literals

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: Invalid input 'UL' for unsigned long
```

```
Neo.ClientError.Statement.SyntaxError: Type mismatch: expected Integer but was Float
```

```
Java.lang.ArithmeticException: integer overflow
```

```
Neo.ClientError.Statement.SyntaxError: Invalid numeric literal
```

## How to Fix It

### 1. Remove Unsigned Integer Syntax

```cypher
// BAD: Neo4j 3.x unsigned integer syntax (not valid in 4.x)
CREATE (n:Counter {value: 42UL});

// GOOD: use regular integer
CREATE (n:Counter {value: 42});
```

### 2. Handle Integer Overflow

```cypher
// Check if value will overflow
WITH toInteger(2147483648) AS val
RETURN val, CASE WHEN val > 2147483647 THEN 'overflow' ELSE 'ok' END AS status;

// Use larger values safely
CREATE (n:BigCounter {value: 9223372036854775807});  // max LONG
```

### 3. Fix Type Conversion Issues

```cypher
// BAD: implicit conversion loses precision
CREATE (n:Metric {value: 3.141592653589793});
// FLOAT has limited precision for large values

// GOOD: store as INTEGER if exact precision is needed
CREATE (n:Metric {value: 3141592653589793});  // store as scaled integer
```

### 4. Update Code for Neo4j 4.x Migration

```java
// Before (Neo4j 3.x)
Value value = Values.value(42L);  // was unsigned

// After (Neo4j 4.x)
Value value = Values.value(42L);  // signed long
```

## Common Scenarios

- **Migration from 3.x to 4.x fails**: Remove `UL` suffixes from all Cypher queries.
- **Property value too large**: Use `toInteger()` carefully and check ranges.
- **Float precision loss**: Store exact values as scaled integers instead of floats.

## Prevent It

- Remove all `UL` suffixes from Cypher queries during Neo4j version upgrades
- Validate integer ranges before inserting into Neo4j
- Use STRING type for values that may exceed INTEGER range

## Related Pages

- [Neo4j Type Error](/tools/neo4j/neo4j-type-error)
- [Neo4j Upgrade Error](/tools/neo4j/neo4j-upgrade-error)
- [Neo4j Query Error](/tools/neo4j/neo4j-query-error)
