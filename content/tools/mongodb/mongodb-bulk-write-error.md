---
title: "[Solution] MongoDB Bulk Write Error"
description: "Fix MongoDB bulkWrite operation errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Bulk Write Error

Bulk write operations can fail for various reasons:

```
BulkWriteError: write error at index 0
```

```
MongoBulkWriteError: E11000 duplicate key error
```

## Common Causes

- One or more operations in the batch violate a unique constraint
- A document in the batch is too large
- The batch exceeds the maximum bulk write size (100,000 operations)
- Write concern errors on one or more operations
- Mixed operation types cause conflicts

## How to Fix

### 1. Handle errors per-operation with ordered:false

```javascript
try {
  const result = await db.users.bulkWrite([
    { insertOne: { document: { _id: 1, name: "Alice" } } },
    { insertOne: { document: { _id: 1, name: "Duplicate" } } },
    { insertOne: { document: { _id: 2, name: "Bob" } } }
  ], { ordered: false });

  console.log("Inserted:", result.insertedCount);
  console.log("Errors:", result.writeErrors);
} catch (err) {
  console.error("Bulk write error:", err.message);
}
```

### 2. Process errors from the result object

```javascript
const result = await db.users.bulkWrite(operations, { ordered: false });
if (result.writeErrors && result.writeErrors.length > 0) {
  result.writeErrors.forEach(err => {
    console.error("Index:", err.index, "Error:", err.errmsg);
  });
}
```

### 3. Split large batches into smaller chunks

```javascript
const CHUNK_SIZE = 1000;
for (let i = 0; i < operations.length; i += CHUNK_SIZE) {
  const chunk = operations.slice(i, i + CHUNK_SIZE);
  await db.users.bulkWrite(chunk, { ordered: false });
}
```

### 4. Use upsert to avoid duplicate key errors

```javascript
await db.users.bulkWrite(
  users.map(user => ({
    updateOne: {
      filter: { email: user.email },
      update: { $set: user },
      upsert: true
    }
  })),
  { ordered: false }
);
```

## Examples

```bash
# Test bulk write with mixed operations
mongosh --eval '
  db.test.drop();
  let ops = [];
  for (let i = 0; i < 100; i++) {
    ops.push({insertOne: {document: {i, val: Math.random()}}});
  }
  let result = db.test.bulkWrite(ops, {ordered:false});
  printjson({inserted: result.insertedCount, errors: result.writeErrors?.length || 0});
'
```