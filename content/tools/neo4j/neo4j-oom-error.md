---
title: "[Solution] Neo4j Out of Memory Error"
description: "Fix Neo4j out of memory errors when queries exceed available heap or native memory"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Out of Memory Error

Out of memory errors occur when a query requires more memory than is allocated to Neo4j.

## Common Causes

- Query processing large graph traversal without limits
- Insufficient heap memory for concurrent transactions
- Native memory pool exhausted by page cache
- Uncommitted transaction state consuming memory

## Common Error Messages

```
Java.lang.OutOfMemoryError: Java heap space
```

```
Neo.TransientError.Statement.OutOfMemoryError: There is not enough memory
```

## How to Fix It

### 1. Increase Heap Memory

```properties
# neo4j.conf
server.memory.heap.initial_size=4g
server.memory.heap.max_size=8g
```

### 2. Profile the Query

```cypher
PROFILE MATCH (n:User)-[:FRIEND]->(m)-[:FRIEND]->(k)
WHERE n.name = 'Alice'
RETURN count(DISTINCT k);
```

### 3. Limit Traversal Depth

```cypher
MATCH (n:User)-[:KNOWS*1..3]->(m)
RETURN n, m LIMIT 100;
```

## Examples

```bash
grep -E "memory\.(heap|pagecache)" /etc/neo4j/neo4j.conf
```
