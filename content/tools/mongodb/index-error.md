---
title: "Index build failed: command failed"
description: "MongoDB fails to build an index due to conflicts, insufficient resources, or invalid index specification"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["index", "build", "index-build", "performance"]
weight: 5
---

This error occurs when MongoDB cannot complete an index build. The operation may fail due to resource constraints, invalid index definitions, or conflicts with existing indexes.

## Common Causes

- Duplicate index name on the same collection
- Index build interrupted by stepdown or primary failover
- Insufficient disk space or memory for the index
- Invalid index key specification (e.g. negative size for TTL index)

## How to Fix

1. Drop duplicate or unnecessary indexes before rebuilding:

```javascript
db.collection.getIndexes()
db.collection.dropIndex("index_name_1")
```

2. Build indexes in background to avoid blocking writes (MongoDB < 4.2):

```javascript
db.collection.createIndex({ email: 1 }, { background: true })
```

3. Check available disk space and memory:

```bash
df -h
```

4. Use `commitIndexBuild` for in-progress builds on sharded clusters:

```javascript
db.adminCommand({ commitIndexBuild: "mydb", "mycollection", "myindex" })
```

## Examples

```javascript
// Attempting to create an index that already exists
db.users.createIndex({ email: 1 }, { name: "email_idx" })
db.users.createIndex({ email: 1 }, { name: "email_idx" })
// MongoServerError: Index with name [email_idx] already exists
```

## Related Errors

- [E11000 duplicate key error collection](/tools/mongodb/duplicate-key)
