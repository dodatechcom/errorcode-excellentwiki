---
title: "[Solution] Neo4j Pattern Matcher Error — How to Fix"
description: "Fix Neo4j pattern matching errors including incorrect MATCH syntax, variable-length path issues, and pattern performance problems"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Pattern Matcher Error

Pattern matcher errors in Neo4j occur when Cypher MATCH patterns are syntactically incorrect, too broad, or cause performance issues with large graphs.

## Why It Happens

- The MATCH pattern uses incorrect arrow direction
- Variable-length paths are unbounded causing infinite traversal
- The pattern tries to match too many paths
- The pattern uses incorrect relationship types
- The pattern references undefined variables
- OPTIONAL MATCH is used where MATCH should be used

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: Invalid relationship pattern
```

```
Neo.ClientError.Statement.SyntaxError: Variable length relationship cannot be used in WHERE
```

```
Neo.TransientError.Resource.Exhausted: There is not enough memory
```

```
Neo.ClientError.Statement.ExecutionFailed: Pattern too complex
```

## How to Fix It

### 1. Fix MATCH Pattern Syntax

```cypher
// BAD: incorrect arrow direction
MATCH (a)-[:KNOWS]->(b)  // relationship from b to a

// GOOD: correct direction
MATCH (a)-[:KNOWS]->(b)  // a knows b

// BAD: missing relationship type
MATCH (a)-->(b)

// GOOD: explicit relationship type
MATCH (a)-[:KNOWS]->(b)
```

### 2. Fix Variable-Length Paths

```cypher
// BAD: unbounded path (dangerous on large graphs)
MATCH (a:Person)-[:KNOWS*]->(b:Person)
RETURN a, b;

// GOOD: bounded path with limits
MATCH (a:Person)-[:KNOWS*1..5]->(b:Person)
RETURN a, b LIMIT 100;

// GOOD: use shortest path
MATCH path = shortestPath((a:Person {name: 'John'})-[:KNOWS*]-(b:Person {name: 'Jane'}))
RETURN path;
```

### 3. Fix Pattern Performance

```cypher
// BAD: full graph scan
MATCH (a)-[r]-(b)
RETURN count(r);

// GOOD: use specific labels and properties
MATCH (a:Person)-[r:KNOWS]->(b:Person)
WHERE a.age > 30
RETURN count(r);

// Add indexes for frequently matched properties
CREATE INDEX FOR (n:Person) ON (n.age);
```

### 4. Fix OPTIONAL MATCH Issues

```cypher
// BAD: OPTIONAL MATCH when MATCH is required
MATCH (a:Person)
OPTIONAL MATCH (a)-[:KNOWS]->(b:Person)
RETURN a, b;  // b is always NULL if no relationship

// GOOD: use MATCH when relationship is required
MATCH (a:Person)-[:KNOWS]->(b:Person)
RETURN a, b;
```

## Common Scenarios

- **Variable-length path causes OOM**: Always set upper bound on path length.
- **Pattern match is too slow**: Add labels to narrow the search space and use indexes.
- **Incorrect arrow direction**: Review the relationship direction in the schema documentation.

## Prevent It

- Always use specific labels in MATCH patterns
- Set upper bounds on variable-length paths
- Use EXPLAIN to verify pattern matching performance

## Related Pages

- [Neo4j Query Error](/tools/neo4j/neo4j-query-error)
- [Neo4j Index Error](/tools/neo4j/neo4j-index-error)
- [Neo4j Cypher Syntax Error](/tools/neo4j/neo4j-cypher-syntax-error)
