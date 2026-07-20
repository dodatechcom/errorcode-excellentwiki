---
title: "[Solution] MongoDB collMod Failed Error"
description: "Fix MongoDB collMod (collection modification) errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB collMod Failed Error

```
MongoServerError: can't have two validation documents for the same collection
```

```
MongoServerError: collection already has index with that name
```

## Common Causes

- The collMod command is malformed
- The collection does not exist
- The index or validator to modify does not exist
- Conflicting options are provided

## How to Fix

### 1. Verify the collection exists

```javascript
db.getCollectionInfos({ name: "myCollection" })
```

### 2. Use collMod correctly

```javascript
// Change validation level
db.runCommand({
  collMod: "myCollection",
  validationLevel: "moderate"
});

// Change validation action
db.runCommand({
  collMod: "myCollection",
  validationAction: "warn"
});

// Update validator
db.runCommand({
  collMod: "myCollection",
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name"],
      properties: {
        name: { bsonType: "string" }
      }
    }
  }
});
```

### 3. Hide an index with collMod

```javascript
db.runCommand({
  collMod: "myCollection",
  index: {
    name: "email_1",
    hidden: true
  }
});
```

## Examples

```bash
# Change validation level
mongosh --eval 'db.runCommand({collMod:"users", validationLevel:"moderate"})'

# Change validation action
mongosh --eval 'db.runCommand({collMod:"users", validationAction:"warn"})'

# Hide an index
mongosh --eval 'db.runCommand({collMod:"users", index:{name:"email_1", hidden:true}})'
```