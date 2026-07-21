---
title: "[Solution] Neo4j Heap Memory Error"
description: "Fix Neo4j heap memory errors when JVM garbage collector cannot reclaim enough memory"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Heap Memory Error

Heap memory errors occur when the JVM garbage collector cannot free enough memory for Neo4j operations.

## Common Causes

- Heap size configured too low for workload
- Memory leak in custom procedures
- Large graph traversals holding object references
- Too many concurrent transactions

## Common Error Messages

```
Java.lang.OutOfMemoryError: GC overhead limit exceeded
```

## How to Fix It

### 1. Increase Heap Size

```properties
# neo4j.conf
server.memory.heap.initial_size=4g
server.memory.heap.max_size=8g
```

### 2. Enable GC Logging

```properties
# neo4j.conf
server.jvm.additional=-verbose:gc
server.jvm.additional=-Xlog:gc*:file=gc.log
```

### 3. Analyze Heap Dump

```bash
jmap -dump:live,format=b,file=heapdump.hprof $(pgrep -f neo4j)
```

## Examples

```bash
jstat -gcutil $(pgrep -f neo4j) 1000 10
```
