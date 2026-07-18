---
title: "[Solution] Neo4j Memory Error — How to Fix"
description: "Fix Neo4j memory errors including heap space issues, page cache configuration, and out-of-memory conditions during query execution"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Memory Error

Memory errors in Neo4j occur when the JVM heap or page cache is insufficient for the workload. Neo4j uses off-heap memory for the page cache and on-heap memory for transactions and query execution.

## Why It Happens

- The JVM heap is too small for the working dataset
- The page cache is not configured for the database size
- A query allocates too much memory (unbounded pattern matching)
- Multiple concurrent queries exhaust available memory
- The transaction memory pool is too small
- The `dbms.memory.heap.initial_size` is not set

## Common Error Messages

```
Java.lang.OutOfMemoryError: Java heap space
```

```
Neo.TransientError.Resource.Exhausted:
There is not enough memory to perform the current task
```

```
Neo.ClientError.Statement.ExecutionFailed:
Cannot allocate memory for query execution
```

```
Java.lang.OutOfMemoryError: GC overhead limit exceeded
```

## How to Fix It

### 1. Configure JVM Heap Size

```bash
# In neo4j.conf
dbms.memory.heap.initial_size=4G
dbms.memory.heap.max_size=8G

# Or set via environment variable
NEO4J_dbms_memory_heap_initial__size=4G
NEO4J_dbms_memory_heap_max__size=8G
```

### 2. Configure Page Cache

```bash
# In neo4j.conf
dbms.memory.pagecache.size=16G

# For multiple databases, allocate per database
dbms.memory.pagecache.size=16G

# Check page cache usage
CALL dbms.listConfig() YIELD name, value
WHERE name = 'dbms.memory.pagecache.size'
RETURN value;
```

### 3. Fix Query Memory Issues

```cypher
// Add memory limit to query
CYPHER runtime=slotted memory=2147483648
MATCH (n:Person)-[:KNOWS*1..5]->(m:Person)
RETURN n, m;

// Use LIMIT to reduce memory usage
MATCH (n:Person)-[:KNOWS]->(m:Person)
RETURN n, m LIMIT 1000;
```

### 4. Monitor Memory Usage

```cypher
// Check JVM memory usage
CALL dbmsJvmActivePools();

// Check page cache usage
CALL dbms.listConfig() YIELD name, value
WHERE name CONTAINS 'memory'
RETURN name, value;
```

## Common Scenarios

- **OOM on large pattern matching**: Add `LIMIT` or use more specific MATCH patterns.
- **Page cache too small for database**: Set `dbms.memory.pagecache.size` to 1.2x the database size.
- **Concurrent queries exhaust heap**: Reduce `dbms.max_concurrent_transactions` or increase heap.

## Prevent It

- Set `dbms.memory.heap.max_size` and `dbms.memory.pagecache.size` explicitly based on available RAM
- Monitor JVM garbage collection logs for memory pressure
- Use `PROFILE` to identify memory-intensive queries

## Related Pages

- [Neo4j Query Error](/tools/neo4j/neo4j-query-error)
- [Neo4j Transaction Error](/tools/neo4j/neo4j-transaction-error)
- [Neo4j Page Cache Error](/tools/neo4j/neo4j-page-cache-error)
