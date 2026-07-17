---
title: "E11000 duplicate key error collection"
description: "MongoDB rejects an insert or update because it violates a unique index constraint"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

This error occurs when you try to insert or update a document with a value that already exists in a unique index field. MongoDB enforces uniqueness constraints and rejects the operation.

## Common Causes

- Inserting a document with a `_id` or unique field that already exists
- Missing application-level checks for duplicates
- Race condition where two processes insert the same key simultaneously
- Unintended unique index on a field that should allow duplicates

## How to Fix

1. Use upsert to insert-or-update:

```javascript
db.users.updateOne(
  { email: "user@example.com" },
  { $setOnInsert: { name: "Alice" } },
  { upsert: true }
)
```

2. Check existing unique indexes:

```javascript
db.collection.getIndexes()
```

3. Remove an unintended unique index if needed:

```javascript
db.collection.dropIndex("fieldname_1")
```

4. Wrap inserts in a try-catch and handle duplicates gracefully:

```javascript
try {
  await db.users.insertOne({ _id: "user123", name: "Alice" });
} catch (e) {
  if (e.code === 11000) {
    console.log("Duplicate key, skipping insert");
  } else {
    throw e;
  }
}
```

## Examples

```javascript
// First insert succeeds
db.users.insertOne({ _id: "user1", name: "Alice" });

// Second insert fails with E11000
db.users.insertOne({ _id: "user1", name: "Bob" });
// E11000 duplicate key error collection: mydb.users dup key: { _id: "user1" }
```

## Related Errors

- [Connection Refused](/tools/mongodb/connection-refused)
