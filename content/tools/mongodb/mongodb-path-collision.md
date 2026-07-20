---
title: "[Solution] MongoDB Path Collision Error"
description: "Fix path collision errors when creating index or update"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Path Collision Error

Path collision occurs when an update operation tries to create both a field and a subfield:

```
ServerError: Cannot create field 'a' in element {a: {b: 1}} : Path collision
```

```
The field 'a.b' cannot be mixed with a field of the same name in a dot path
```

## Common Causes

- An update tries to set both `a` and `a.b` simultaneously
- A `$set` operation conflicts with an existing field path
- Creating an index where one path is a prefix of another (e.g., `a` and `a.b`)
- Merging documents with conflicting field structures

## How to Fix

### 1. Restructure your update operations

```javascript
// Wrong: path collision
await db.users.updateOne(
  { _id: 1 },
  { $set: { address: { street: "Main St" }, "address.city": "NYC" } }
);

// Correct: set the full subdocument
await db.users.updateOne(
  { _id: 1 },
  { $set: { address: { street: "Main St", city: "NYC" } } }
);
```

### 2. Restructure index fields

```javascript
// Wrong: path collision in index
db.users.createIndex({ "address": 1, "address.city": 1 });

// Correct: use only the more specific path
db.users.createIndex({ "address.city": 1 });
```

### 3. Use separate update operations

```javascript
// If you need to set multiple levels, do it sequentially
await db.users.updateOne({ _id: 1 }, { $set: { address: { street: "Main St" } } });
await db.users.updateOne({ _id: 1 }, { $set: { "address.city": "NYC" } });
```

### 4. Review the document structure

```javascript
// Use $mergeObjects for merging subdocuments
await db.users.updateOne(
  { _id: 1 },
  { $set: { address: { $mergeObjects: ["$address", { city: "NYC" }] } } }
);
```

## Examples

```bash
# Demonstrate path collision
mongosh --eval '
  db.test.drop();
  db.test.insertOne({a: {b: 1}});
  try {
    db.test.updateOne({}, {$set: {a:1, "a.b":2}});
  } catch(e) { print(e.message); }
'

# Fix: restructure the update
mongosh --eval '
  db.test.updateOne({}, {$set: {a: {b: 2, c: 3}}});
  printjson(db.test.findOne());
'
```