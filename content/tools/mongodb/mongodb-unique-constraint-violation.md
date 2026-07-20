---
title: "[Solution] MongoDB Unique Constraint Violation"
description: "Fix MongoDB unique constraint violations on index fields"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Unique Constraint Violation

A unique constraint violation occurs when an insert or update creates duplicate values:

```
WriteError: E11000 duplicate key error collection: db.users index: username_1 dup key: { username: "admin" }
```

## Common Causes

- Inserting a document with a duplicate value in a unique-indexed field
- Updating a field to match an existing value in another document
- Compound unique index allows duplicate partial values but not full combination
- Race conditions in concurrent inserts
- The unique index was created on a collection with existing duplicates

## How to Fix

### 1. Check for existing duplicates before inserting

```javascript
const existing = await db.users.findOne({ username: "admin" });
if (existing) {
  console.log("User already exists:", existing._id);
} else {
  await db.users.insertOne({ username: "admin", name: "Administrator" });
}
```

### 2. Use upsert with $setOnInsert

```javascript
await db.users.updateOne(
  { username: "admin" },
  { $setOnInsert: { name: "Administrator", createdAt: new Date() } },
  { upsert: true }
);
```

### 3. Create a partial unique index for soft-deleted documents

```javascript
db.users.createIndex(
  { email: 1 },
  {
    unique: true,
    partialFilterExpression: { deleted: { $ne: true } }
  }
);
```

### 4. Handle compound unique constraints

```javascript
// Compound unique: the combination of fields must be unique
db.bookings.createIndex(
  { resourceId: 1, date: 1 },
  { unique: true }
);
```

## Examples

```bash
# Find all duplicate values
mongosh --eval '
  db.users.aggregate([
    {$group: {_id: "$email", count: {$sum: 1}, ids: {$addToSet: "$_id"}}},
    {$match: {count: {$gt: 1}}}
  ]).toArray();
'

# Create a unique index with sparse option
mongosh --eval '
  db.users.createIndex({email:1}, {unique: true, sparse: true});
'
```