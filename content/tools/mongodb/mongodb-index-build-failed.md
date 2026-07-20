---
title: "[Solution] MongoDB Index Build Failed"
description: "Fix MongoDB index build failures and build process errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Index Build Failed Error

Index builds can fail for several reasons:

```
MongoServerError: Index build failed: operation was interrupted
```

```
MongoServerError: Error persisting index spec...
```

## Common Causes

- The index build was interrupted (e.g., server restart, stepdown)
- Not enough memory for the in-memory index build
- The index specification is invalid (duplicate field, bad collation)
- The collection is too large and the build exceeds the timeout
- A conflicting index already exists
- The server is in read-only mode

## How to Fix

### 1. Build indexes during low-traffic periods

```javascript
db.users.createIndex({ email: 1 }, { background: true });
```

### 2. Use the 4.2+ non-blocking index build

MongoDB 4.2+ builds indexes without blocking reads/writes by default. Ensure you are on 4.2+.

### 3. Check for sufficient resources

```bash
# Check available memory
free -h

# Check disk space
df -h /var/lib/mongodb

# Check for I/O bottleneck
iostat -x 1 5
```

### 4. Build in rolling fashion for replica sets

```bash
# Step 1: Build on secondary (with rs.stepDown)
mongosh --host mongo2 --eval "db.users.createIndex({email:1})"

# Step 2: Build on the other secondary
mongosh --host mongo3 --eval "db.users.createIndex({email:1})"

# Step 3: Step down primary, build on new secondary
```

### 5. Verify the index specification

```javascript
// Check existing indexes to avoid conflicts
db.users.getIndexes();

// Drop the index and recreate
db.users.dropIndex("email_1");
db.users.createIndex({ email: 1 }, { unique: true });
```

## Examples

```bash
# Monitor ongoing index builds
mongosh --eval "db.currentOp({desc: /index build/})"

# Check index build progress (MongoDB 4.2+)
mongosh --eval "db.adminCommand({getCurrentIndexBuilds:1})"

# Kill a stuck index build
mongosh --eval "db.adminCommand({killOp: <opId>})"
```