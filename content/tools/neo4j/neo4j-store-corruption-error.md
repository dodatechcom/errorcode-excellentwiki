---
title: "[Solution] Neo4j Store Corruption Error"
description: "Fix Neo4j store corruption errors when database files are damaged"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Store Corruption Error

Store corruption errors occur when Neo4j detects damage to its internal database files.

## Common Causes

- Unexpected shutdown during write
- Disk hardware failure
- Filesystem corruption
- Version upgrade without proper backup

## Common Error Messages

```
Neo.DatabaseError.Statement.ExecutionFailed: Store file has been corrupted
```

## How to Fix It

### 1. Run Store Check

```bash
neo4j-admin database check /var/lib/neo4j/data/databases/neo4j
```

### 2. Restore from Backup

```bash
neo4j-admin database restore --from-path=/backups/neo4j/ --to-path=/var/lib/neo4j/data/databases/neo4j
```

### 3. Recover Corrupted Store

```bash
neo4j-admin database recover /var/lib/neo4j/data/databases/neo4j
```

## Examples

```bash
neo4j-admin database check --verbose /var/lib/neo4j/data/databases/neo4j
```
