---
title: "[Solution] MongoDB Authorization Failure"
description: "Fix MongoDB authorization failures on operations"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Authorization Failure

```
MongoServerError: not authorized on mydb to execute command { insert: "users" }
```

## Common Causes

- The user does not have the required role for the operation
- The role was granted on a different database
- The user's role was revoked
- The operation requires a more privileged role

## How to Fix

### 1. Check the user's current roles

```javascript
use admin
db.getUser("myuser")
```

### 2. Grant the appropriate role

```javascript
use admin
db.grantRolesToUser("myuser", [
  { role: "readWrite", db: "mydb" }
]);
```

### 3. Use dbAdmin for index operations

```javascript
use admin
db.grantRolesToUser("myuser", [
  { role: "dbAdmin", db: "mydb" }
]);
```

### 4. Grant cluster-level permissions for admin commands

```javascript
use admin
db.grantRolesToUser("myuser", [
  { role: "clusterAdmin", db: "admin" }
]);
```

## Examples

```bash
# Check user authorization
mongosh --eval "use admin; db.getUser('myuser')"

# Grant readWrite role
mongosh --eval 'use admin; db.grantRolesToUser("myuser", [{role:"readWrite",db:"mydb"}])'

# Test authorization
mongosh --username myuser --password password --authenticationDatabase admin \
  --eval "db.mydb.users.insertOne({name:'test'})"
```