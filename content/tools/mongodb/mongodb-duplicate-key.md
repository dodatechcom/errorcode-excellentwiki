---
title: "MongoDB Duplicate Key Error"
description: "MongoDB insert or update fails due to duplicate unique key violation."
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["mongodb", "duplicate", "key", "unique-index", "constraint"]
weight: 5
---

# MongoDB Duplicate Key Error

A MongoDB duplicate key error occurs when an insert or update operation tries to create a document with a value that already exists in a unique index or the `_id` field.

## Common Causes

- Inserting a document with an existing `_id`
- Violating a unique index constraint
- Race condition with concurrent inserts
- Using upsert without proper filter

## How to Fix

### Check Existing Indexes

```javascript
db.collection.getIndexes()
```

### Use insertOne with Error Handling

```javascript
try {
  await db.collection('users').insertOne({ email: 'user@example.com' });
} catch (e) {
  if (e.code === 11000) {
    console.log('Duplicate key error');
  }
}
```

### Use updateOne with upsert

```javascript
await db.collection('users').updateOne(
  { email: 'user@example.com' },
  { $set: { name: 'John' } },
  { upsert: true }
);
```

### Use findAndModify for Atomic Operations

```javascript
await db.collection('counters').findOneAndUpdate(
  { _id: 'order' },
  { $inc: { seq: 1 } },
  { upsert: true, returnDocument: 'after' }
);
```

### Drop Problematic Index

```javascript
db.collection.dropIndex('email_1');
```

## Examples

```javascript
// Duplicate _id
E11000 duplicate key error collection: mydb.users
  dup key: { _id: ObjectId('...') }

// Duplicate unique index
E11000 duplicate key error collection: mydb.users
  dup key: { email: "user@example.com" }
```

## Related Errors

- [Write Error]({{< relref "/tools/mongodb/write-concern" >}}) — write concern error
- [Index Error]({{< relref "/tools/mongodb/index-error" >}}) — index error
