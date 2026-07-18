---
title: "[Solution] Neo4j Cypher Syntax Error — How to Fix"
description: "Fix Neo4j Cypher syntax errors including common syntax mistakes, missing clauses, and version-specific syntax differences"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Cypher Syntax Error

Cypher syntax errors occur when the query language parser cannot understand the statement. These are usually straightforward to fix once the error location is identified.

## Why It Happens

- Missing commas, parentheses, or keywords
- Wrong keyword order (e.g., RETURN before MATCH)
- Using deprecated syntax from an older Neo4j version
- Incorrect use of quotes (single vs double)
- Missing AS alias for expressions
- Wrong use of UNWIND or WITH clauses

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: Invalid input 'xxx' (line 1, column 15)
```

```
Neo.ClientError.Statement.SyntaxError: Expected one of: MATCH, OPTIONAL MATCH, UNWIND, WITH, ...
```

```
Neo.ClientError.Statement.SyntaxError: Invalid value 'xxx' for property key
```

```
Neo.ClientError.Statement.SyntaxError: Unknown function 'xxx'
```

## How to Fix It

### 1. Check Error Location

```
Neo.ClientError.Statement.SyntaxError: Invalid input 'WHERE'
(line 1, column 25)
```
The error is at line 1, column 25. Check that position in the query.

### 2. Fix Common Syntax Mistakes

```cypher
// BAD: missing comma between properties
MATCH (n:Person {name: 'John' age: 30}) RETURN n;

// GOOD
MATCH (n:Person {name: 'John', age: 30}) RETURN n;

// BAD: wrong keyword order
RETURN n MATCH (n:Person);

// GOOD
MATCH (n:Person) RETURN n;
```

### 3. Fix Quote Usage

```cypher
// BAD: using single quotes for strings (invalid in Cypher)
MATCH (n:Person) WHERE n.name = 'John' RETURN n;

// GOOD: use single quotes (actually correct in Cypher)
MATCH (n:Person) WHERE n.name = 'John' RETURN n;

// For property keys with special chars, use backticks
MATCH (n) WHERE n.`first-name` = 'John' RETURN n;
```

### 4. Fix UNWIND Syntax

```cypher
// BAD
UNWIND [1,2,3] AS x RETURN x;

// GOOD
UNWIND [1, 2, 3] AS x RETURN x;

// BAD: UNWIND with wrong variable
MATCH (n:Person) UNWIND n.tags AS tag RETURN tag;

// GOOD: use UNWIND after WITH
MATCH (n:Person)
WITH n, split(n.tags, ',') AS tags
UNWIND tags AS tag
RETURN tag;
```

## Common Scenarios

- **Copy-pasted query from MySQL**: Cypher has different syntax. Adapt the query for Neo4j.
- **Upgrade changes syntax**: Some deprecated syntax is removed. Check Neo4j release notes.
- **Missing comma in pattern**: A missing comma between node patterns causes a syntax error.

## Prevent It

- Use Neo4j Browser or Bloom to validate queries before deploying
- Enable query syntax checking in the IDE or driver
- Keep a Cypher cheat sheet for reference

## Related Pages

- [Neo4j Query Error](/tools/neo4j/neo4j-query-error)
- [Neo4j Matcher Error](/tools/neo4j/neo4j-matcher-error)
- [Neo4j Set Property Error](/tools/neo4j/neo4j-set-property-error)
