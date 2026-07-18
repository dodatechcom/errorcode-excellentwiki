---
title: "[Solution] Neo4j Page Cache Error — How to Fix"
description: "Fix Neo4j page cache errors including cache misses, memory configuration, and page cache performance issues"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Page Cache Error

Page cache errors in Neo4j occur when the page cache is misconfigured, too small, or experiencing performance issues. The page cache is used to cache database files in memory.

## Why It Happens

- The page cache size is too small for the database
- The page cache is competing with the JVM heap for memory
- Memory-mapped files are not supported on the file system
- The page cache is fragmented due to frequent evictions
- Multiple databases share a page cache that is too small

## Common Error Messages

```
Neo.TransientError.Resource.Exhausted:
Cannot allocate memory for page cache
```

```
Neo4j Page cache hit ratio is below 90%
```

```
ERROR: Page cache eviction rate is too high
```

```
WARNING: Page cache is using more than 80% of available memory
```

## How to Fix It

### 1. Configure Page Cache Size

```bash
# In neo4j.conf
dbms.memory.pagecache.size=16G

# For multiple databases
dbms.memory.pagecache.size=16G

# Calculate appropriate size (1.2x the total database size)
du -sh /var/lib/neo4j/data/databases/
```

### 2. Monitor Page Cache Performance

```cypher
// Check page cache hit ratio
CALL dbms.listMetrics()
YIELD name, value
WHERE name CONTAINS 'page_cache'
RETURN name, value;

// Check page cache usage
CALL dbms.debug.refreshPageCacheStats();
```

### 3. Fix Page Cache Configuration

```bash
# Ensure page cache has enough memory
# Total RAM = JVM heap + Page cache + OS + other services
# Example: 32GB server
# JVM heap: 8G
# Page cache: 16G
# OS and other: 8G

# In neo4j.conf
dbms.memory.heap.initial_size=4G
dbms.memory.heap.max_size=8G
dbms.memory.pagecache.size=16G
```

### 4. Fix File System Issues

```bash
# Ensure file system supports memory mapping
# Use ext4 or XFS (not NFS or CIFS)

# Check mount options
mount | grep /var/lib/neo4j

# Ensure noatime for better performance
# In /etc/fstab
# /dev/sda1 /var/lib/neo4j ext4 noatime 0 2
```

## Common Scenarios

- **Page cache hit ratio is low**: Increase `dbms.memory.pagecache.size`.
- **Page cache competes with heap**: Reduce heap size and increase page cache.
- **Slow I/O after page cache miss**: Ensure page cache is large enough for the working set.

## Prevent It

- Set page cache size to at least 1.2x the total database size
- Monitor page cache hit ratio and adjust size accordingly
- Use fast SSD storage for the database directory

## Related Pages

- [Neo4j Memory Error](/tools/neo4j/neo4j-memory-error)
- [Neo4j Kernel Error](/tools/neo4j/neo4j-kernel-error)
- [Neo4j Query Error](/tools/neo4j/neo4j-query-error)
