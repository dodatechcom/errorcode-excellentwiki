---
title: "[Solution] Neo4j Page Cache Error"
description: "Fix Neo4j page cache errors when memory-mapped page cache encounters IO failures"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Page Cache Error

Page cache errors occur when Neo4j cannot memory-map database files due to OS limitations.

## Common Causes

- Page cache size smaller than database
- Filesystem does not support memory mapping
- Too many open file descriptors
- Disk IO errors preventing page reads

## Common Error Messages

```
Neo.TransientError.General.OutOfMemoryError: There is not enough memory
```

## How to Fix It

### 1. Increase Page Cache

```properties
# neo4j.conf
server.memory.pagecache.size=4g
```

### 2. Check File Descriptor Limit

```bash
cat /proc/$(pgrep -f neo4j)/limits | grep "open files"
```

### 3. Increase File Descriptor Limit

```bash
ulimit -n 65535
```

## Examples

```bash
grep -r "pagecache" /var/log/neo4j/
```
