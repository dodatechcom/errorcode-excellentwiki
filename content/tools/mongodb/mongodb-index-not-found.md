---
title: "[Solution] MongoDB Index Not Found Error"
description: "Fix MongoDB index not found or missing index errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Index Not Found Error

Operations may fail when an expected index does not exist:

```
MongoServerError: error processing query: ... No query solutions
```

```
Error: plan executor error: Unknown error
```

## Common Causes

- The index was dropped or never created
- The index name was misspelled in a hint
- The collection was recreated without indexes
- The query references a field that has no index and no valid query plan
- Index builds failed silently

## How to Fix

### 1. List existing indexes

```javascript
db.users.getIndexes();
```

### 2. Create the missing index

```javascript
db.users.createIndex({ email: 1 }, { unique: true });
```

### 3. Use hint to specify the index

```javascript
db.users.find({ email: "test@example.com" }).hint("email_1");
```

### 4. Recreate indexes from index definitions

```javascript
const indexes = db.users.getIndexes();
indexes.forEach(idx => {
  if (idx.name !== "_id_") {
    const keys = {};
    for (let key in idx.key) {
      keys[key] = idx.key[key];
    }
    const opts = {};
    if (idx.unique) opts.unique = true;
    if (idx.sparse) opts.sparse = true;
    db.users.createIndex(keys, opts);
  }
});
```

## Examples

```bash
# Check indexes on a collection
mongosh --eval "db.users.getIndexes().forEach(i => printjson(i))"

# Verify a specific index exists
mongosh --eval "print(db.users.getIndexes().some(i => i.name === 'email_1'))"

# Create indexes from a template
mongosh --eval '
  [{email:1},{name:1},{createdAt:-1}].forEach(spec => {
    db.users.createIndex(spec);
    print("Created index:", JSON.stringify(spec));
  });
'
```