---
title: "[Solution] MongoDB Rename Collection Error"
description: "Fix MongoDB renameCollection errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Rename Collection Error

```
MongoServerError: can't rename to different database
```

```
MongoServerError: collection name already exists
```

## Common Causes

- Renaming to a different database is not allowed with renameCollection
- The target collection name already exists
- The collection name is invalid
- The user does not have the required privileges

## How to Fix

### 1. Use renameCollection on the same database

```javascript
db.adminCommand({
  renameCollection: "mydb.oldName",
  to: "mydb.newName"
});
```

### 2. Drop the target collection first if it exists

```javascript
db.targetCollection.drop();
db.adminCommand({
  renameCollection: "mydb.source",
  to: "mydb.target"
});
```

### 3. For cross-database renames, use copy and drop

```javascript
// Copy to new database
db.source.find().forEach(doc => {
  db.getSiblingDB("targetDB").target.insert(doc);
});

// Verify the copy
print("Source count:", db.source.countDocuments());
print("Target count:", db.getSiblingDB("targetDB").target.countDocuments());

// Drop the source
db.source.drop();
```

### 4. Ensure proper privileges

```javascript
// The user needs dbAdmin or restore role
use admin
db.grantRolesToUser("myuser", [{ role: "dbAdmin", db: "mydb" }]);
```

## Examples

```bash
# Rename a collection
mongosh --eval 'db.adminCommand({renameCollection:"mydb.old", to:"mydb.new"})'

# Cross-database copy and rename
mongosh --eval '
  db.source.find().forEach(doc => {
    db.getSiblingDB("targetDB").target.insert(doc);
  });
  db.source.drop();
  print("Collection moved successfully");
'
```