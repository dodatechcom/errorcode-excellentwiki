---
title: "[Solution] MongoDB findAndModify Error"
description: "Fix findAndModify errors including upsert and returnDocument issues"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB findAndModify Error

The `findAndModify` command can fail with several errors:

```
MongoServerError: After applying the update, the (immutable) field '_id' was found to have been altered
```

```
MongoServerError: findAndModify failed: write conflict
```

## Common Causes

- Attempting to modify the `_id` field
- The query matches multiple documents (only one is modified)
- Write conflict in a multi-statement transaction
- The update returns a value that conflicts with a unique index
- `new: true` (or `returnDocument: "AFTER"`) not specified when needed

## How to Fix

### 1. Never modify the _id field

```javascript
// Wrong
await db.users.findOneAndUpdate(
  { _id: 1 },
  { $set: { _id: 2, name: "Bob" } }  // Error: cannot modify _id
);

// Correct
await db.users.findOneAndUpdate(
  { _id: 1 },
  { $set: { name: "Bob" } }
);
```

### 2. Use returnDocument option

```javascript
const result = await db.users.findOneAndUpdate(
  { name: "Alice" },
  { $inc: { score: 10 } },
  { returnDocument: "after" }  // Returns the modified document
);
console.log(result.value);
```

### 3. Handle upsert with findAndModify

```javascript
const result = await db.counters.findOneAndUpdate(
  { _id: "orderId" },
  { $inc: { seq: 1 } },
  { upsert: true, returnDocument: "after" }
);
```

### 4. Avoid write conflicts in transactions

```javascript
const session = client.startSession();
try {
  session.startTransaction({ readConcern: { level: "snapshot" } });
  await db.users.findOneAndUpdate({ _id: 1 }, { $inc: { balance: -10 } }, { session });
  await session.commitTransaction();
} catch (err) {
  await session.abortTransaction();
} finally {
  session.endSession();
}
```

## Examples

```bash
# Atomic increment with findAndModify
mongosh --eval '
  let result = db.counters.findOneAndUpdate(
    {_id: "seq"},
    {$inc: {value: 1}},
    {upsert: true, returnDocument: "after"}
  );
  print("New value:", result.value);
'

# Delete and return a document
mongosh --eval '
  let removed = db.queue.findOneAndDelete(
    {status: "pending"},
    {sort: {created: 1}}
  );
  printjson(removed);
'
```