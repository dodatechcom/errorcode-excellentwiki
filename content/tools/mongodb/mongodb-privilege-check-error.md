---
title: "[Solution] MongoDB Privilege Check Error"
description: "Fix MongoDB insufficient privileges errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Privilege Check Error

```
MongoServerError: not enough privileges for <action>
```

## Common Causes

- The user's role does not include the required privilege
- The privilege scope is too narrow (wrong database or collection)
- Custom privileges were not properly configured
- Built-in roles do not include the specific action required

## How to Fix

### 1. Check role privileges

```javascript
db.getRoles({ showPrivileges: true })
// or for a specific role
db.getRole("customRole", { showPrivileges: true })
```

### 2. Create a role with specific privileges

```javascript
use admin
db.createRole({
  role: "dataPipeline",
  privileges: [
    {
      resource: { db: "mydb", collection: "logs" },
      actions: ["find", "insert", "update"]
    },
    {
      resource: { db: "mydb", collection: "archive" },
      actions: ["find", "insert"]
    }
  ],
  roles: []
});
```

### 3. Grant the role to a user

```javascript
db.grantRolesToUser("myuser", [
  { role: "dataPipeline", db: "admin" }
]);
```

### 4. Verify privileges

```javascript
db.getUser("myuser", { showPrivileges: true })
```

## Examples

```bash
# Check custom role privileges
mongosh --eval "use admin; db.getRole('dataPipeline', {showPrivileges:true})"

# List all privileges for a user
mongosh --eval "use admin; db.getUser('myuser', {showPrivileges:true})"

# Create a role with specific collection access
mongosh --eval '
  use admin;
  db.createRole({
    role: "readOnlyAudit",
    privileges: [{
      resource: {db:"audit", collection:""},
      actions: ["find","listCollections","listIndexes"]
    }],
    roles: []
  });
'
```