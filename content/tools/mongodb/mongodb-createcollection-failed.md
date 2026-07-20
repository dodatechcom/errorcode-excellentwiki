---
title: "[Solution] MongoDB createCollection Failed Error"
description: "Fix MongoDB createCollection errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB createCollection Failed Error

```
MongoServerError: a collection 'mydb.users' already exists
```

```
MongoServerError: invalid collection name
```

## Common Causes

- The collection already exists
- The collection name contains invalid characters
- The collection name is too long
- The capped collection options are invalid
- The validator schema is malformed

## How to Fix

### 1. Check if the collection exists

```javascript
db.getCollectionInfos({ name: "users" })
```

### 2. Use createCollection with options

```javascript
// Create a capped collection
db.createCollection("logs", {
  capped: true,
  size: 1024 * 1024 * 100,  // 100 MB
  max: 100000
});

// Create with validator
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "email"],
      properties: {
        name: { bsonType: "string" },
        email: { bsonType: "string" }
      }
    }
  }
});
```

### 3. Drop and recreate if needed

```javascript
db.users.drop();
db.createCollection("users");
```

### 4. Use a valid collection name

```javascript
// Valid: alphanumeric, underscores, dots (not starting with system.)
db.createCollection("my_collection");
db.createCollection("logs.2024");

// Invalid
db.createCollection("$invalid");
db.createCollection("system.users");  // Reserved
```

## Examples

```bash
# Check existing collections
mongosh --eval "db.getCollectionInfos().map(c => c.name)"

# Create a capped collection
mongosh --eval '
  db.createCollection("logs", {
    capped: true,
    size: 1024*1024*100,
    max: 100000
  });
  print("Capped collection created");
'
```