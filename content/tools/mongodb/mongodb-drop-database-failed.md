---
title: "[Solution] MongoDB Drop Database Failed Error"
description: "Fix MongoDB dropDatabase errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Drop Database Failed Error

```
MongoServerError: not authorized to drop database
```

```
MongoServerError: cannot drop database while session is active
```

## Common Causes

- The user does not have the required privileges to drop a database
- There are active sessions using the database
- The database does not exist
- The database is a system database (admin, local, config)

## How to Fix

### 1. Grant the required role

```javascript
use admin
db.grantRolesToUser("myuser", [
  { role: "dbOwner", db: "mydb" }
]);
```

### 2. Drop the database correctly

```javascript
use mydb
db.dropDatabase()
```

### 3. Ensure no active sessions

```javascript
// Check for active operations
db.currentOp({ ns: /mydb/ })

// Kill operations if needed
db.killOp(<opId>)
```

### 4. Never drop system databases

```javascript
// These databases should never be dropped:
// - admin
// - local
// - config
```

## Examples

```bash
# Check current databases
mongosh --eval "db.adminCommand({listDatabases:1}).databases.map(d => d.name)"

# Drop a database
mongosh --eval 'use mydb; db.dropDatabase();'

# Verify the database is dropped
mongosh --eval "db.adminCommand({listDatabases:1}).databases.map(d => d.name)"
```