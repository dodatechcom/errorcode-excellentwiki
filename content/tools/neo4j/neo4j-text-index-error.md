---
title: "[Solution] Neo4j Full-Text Index Error"
description: "Fix Neo4j full-text index errors when Lucene-based text search queries fail"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Full-Text Index Error

Full-text index errors occur when the Lucene-based text search engine encounters issues.

## Common Causes

- Full-text index not yet online
- Analyzer not available for the language
- Query syntax incompatible with Lucene
- Index segment corruption

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: Fulltext index is not available
```

## How to Fix It

### 1. Create Full-Text Index

```cypher
CREATE FULLTEXT INDEX productSearch IF NOT EXISTS
FOR (p:Product) ON EACH [p.name, p.description];
```

### 2. Wait for Index to Come Online

```cypher
SHOW FULLTEXT INDEXES YIELD name, state;
```

### 3. Use Correct Query Syntax

```cypher
CALL db.index.fulltext.queryNodes('productSearch', 'wireless bluetooth')
YIELD node, score
RETURN node.name, score
ORDER BY score DESC LIMIT 10;
```

## Examples

```cypher
CALL db.index.fulltext.queryNodes('productSearch', 'waterproof OR resistant')
YIELD node, score
RETURN node.name, score;
```
