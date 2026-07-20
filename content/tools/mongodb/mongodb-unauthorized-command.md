---
title: "[Solution] MongoDB Unauthorized to Execute Command"
description: "Fix MongoDB unauthorized command execution errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Unauthorized to Execute Command

```
MongoServerError: not authorized on admin to execute command { serverStatus: 1 }
```

```
MongoServerError: command <command> not allowed
```

## Common Causes

- The user does not have the required role to execute the command
- The command requires admin-level privileges
- The user's role does not include the necessary action
- The command was executed on the wrong database

## How to Fix

### 1. Grant the required role

```javascript
use admin
db.grantRolesToUser("myuser", [
  { role: "read", db: "admin" },
  { role: "clusterMonitor", db: "admin" }
]);
```

### 2. Create a user with proper privileges

```javascript
use admin
db.createUser({
  user: "monitor",
  pwd: "password",
  roles: [
    { role: "clusterMonitor", db: "admin" },
    { role: "read", db: "mydb" }
  ]
});
```

### 3. Use built-in roles for common tasks

```javascript
// clusterMonitor: for serverStatus, connPoolStats, etc.
// read: for querying data
// readWrite: for insert, update, delete operations
// dbAdmin: for index creation, validate, etc.
// userAdmin: for user management
```

### 4. Check the user's current roles

```javascript
use admin
db.getUser("myuser")
```

## Examples

```bash
# Check user roles
mongosh --eval "use admin; db.getUser('myuser')"

# Grant a role
mongosh --eval 'use admin; db.grantRolesToUser("myuser", [{role:"clusterMonitor",db:"admin"}])'

# Test a command
mongosh --username myuser --password password --authenticationDatabase admin --eval "db.adminCommand({serverStatus:1})"
```