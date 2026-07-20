---
title: "[Solution] MongoDB Role Not Found Error"
description: "Fix MongoDB role not found errors when granting privileges"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Role Not Found Error

```
MongoServerError: role "customRole" not found
```

## Common Causes

- The role name is misspelled
- The role does not exist in the specified database
- A built-in role was referenced in the wrong database
- Custom roles must be created before being assigned

## How to Fix

### 1. List available roles

```javascript
db.getRoles({ showBuiltinRoles: true })
```

### 2. List roles in a specific database

```javascript
use mydb
db.getRoles()
```

### 3. Create a custom role

```javascript
use admin
db.createRole({
  role: "customReadRole",
  privileges: [
    { resource: { db: "mydb", collection: "" }, actions: ["find"] }
  ],
  roles: []
});
```

### 4. Use built-in roles correctly

```javascript
// Built-in roles: read, readWrite, dbAdmin, userAdmin, clusterAdmin, etc.
db.createUser({
  user: "myuser",
  pwd: "password",
  roles: [
    { role: "readWrite", db: "mydb" },
    { role: "dbAdmin", db: "mydb" }
  ]
});
```

## Examples

```bash
# List all roles
mongosh --eval "db.getRoles({showBuiltinRoles: true})"

# List roles in a database
mongosh --eval "use mydb; db.getRoles()"

# Create a custom role
mongosh --eval '
  use admin;
  db.createRole({
    role: "customMonitor",
    privileges: [{resource:{db:"",collection:""},actions:["serverStatus","connPoolStats"]}],
    roles: []
  });
'
```