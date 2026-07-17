---
title: "MongoDB - E11000 duplicate key error"
description: "MongoDB insert or update fails because a document violates a unique index constraint with a duplicate key value"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["mongodb", "duplicate-key", "unique", "index", "e11000", "insert"]
weight: 5
---

An E11000 duplicate key error occurs when MongoDB attempts to insert or update a document that violates a unique index constraint. The error includes the collection name, index name, and the duplicate key value.

## Common Causes

- Inserting a document with a value that already exists in a unique field
- Race condition with concurrent inserts on the same unique key
- Unique index on `_id` field with manual ID assignment
- Bulk insert with duplicate values in the batch
- Missing unique index causing unexpected duplicates

## How to Fix

1. Use `insertOne` with error handling for duplicates:

```javascript
try {
  await db.collection('users').insertOne({ email: 'user@example.com' });
} catch (error) {
  if (error.code === 11000) {
    console.log('Duplicate key error:', error.keyValue);
  }
}
```

2. Use upsert to handle duplicates gracefully:

```javascript
await db.collection('users').updateOne(
  { email: 'user@example.com' },
  { $set: { name: 'John', updatedAt: new Date() } },
  { upsert: true }
);
```

3. Check existing unique indexes:

```javascript
const indexes = await db.collection('users').indexes();
console.log(indexes.filter(i => i.unique));
```

4. Remove or relax conflicting unique indexes:

```javascript
await db.collection('users').dropIndex('email_1');
```

5. Use `bulkWrite` with ordered operations and handle duplicates:

```javascript
const ops = documents.map(doc => ({
  updateOne: {
    filter: { email: doc.email },
    update: { $set: doc },
    upsert: true,
  }
}));
await db.collection('users').bulkWrite(ops, { ordered: false });
```

## Examples

```javascript
// Error: E11000 duplicate key error collection: mydb.users index: email_1 dup key: { email: "test@example.com" }
await db.collection('users').insertOne({ email: 'test@example.com' });
// If email index is unique and test@example.com already exists

// Fix: handle the duplicate case
try {
  await db.collection('users').insertOne({ email: 'test@example.com' });
} catch (err) {
  if (err.code === 11000) {
    console.log('User already exists');
  }
}
```

## Related Errors

- [Write error]({{< relref "/tools/mongodb/mongodb-write-error" >}})
- [Index error]({{< relref "/tools/mongodb/mongodb-index-error" >}})
