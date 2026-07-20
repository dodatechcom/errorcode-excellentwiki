---
title: "[Solution] MongoDB Duplicate Key Error E11000"
description: "Fix MongoDB E11000 duplicate key error on insert or update"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Duplicate Key Error (E11000)

The E11000 error occurs when an insert or update attempts to create a duplicate value for a unique index:

```
MongoServerError: E11000 duplicate key error collection: mydb.users index: email_1 dup key: { email: "test@example.com" }
```

## Common Causes

- Inserting a document with a value that already exists in a unique-indexed field
- Updating a field to a value that violates a unique constraint
- Race condition: two concurrent inserts with the same unique value
- The unique index was created after duplicate documents already existed
- The `_id` field is being set manually and conflicts with an existing document

## How to Fix

### 1. Use upsert to handle duplicates gracefully

```javascript
// Instead of insertOne, use updateOne with upsert
await db.users.updateOne(
  { email: "test@example.com" },
  { $setOnInsert: { name: "John", createdAt: new Date() } },
  { upsert: true }
);
```

### 2. Use try-catch with error code

```javascript
try {
  await db.users.insertOne({ email: "test@example.com", name: "John" });
} catch (err) {
  if (err.code === 11000) {
    console.log("Duplicate key - document may already exist");
    // Update instead
    await db.users.updateOne(
      { email: "test@example.com" },
      { $set: { name: "John" } }
    );
  } else {
    throw err;
  }
}
```

### 3. Drop duplicates before creating unique index

```javascript
// Find duplicates
db.users.aggregate([
  { $group: { _id: "$email", dups: { $addToSet: "$_id" }, count: { $sum: 1 } } },
  { $match: { count: { $gt: 1 } } }
]);

// Remove duplicates (keep the first one)
db.users.aggregate([
  { $group: { _id: "$email", dups: { $addToSet: "$_id" }, count: { $sum: 1 } } },
  { $match: { count: { $gt: 1 } } }
]).forEach(doc => {
  doc.dups.shift();
  db.users.deleteMany({ _id: { $in: doc.dups } });
});

// Now create the unique index
db.users.createIndex({ email: 1 }, { unique: true });
```

### 4. Use bulkWrite with ordered:false

```javascript
const ops = documents.map(doc => ({
  updateOne: {
    filter: { email: doc.email },
    update: { $setOnInsert: doc },
    upsert: true
  }
}));
await db.users.bulkWrite(ops, { ordered: false });
```

## Examples

```bash
# Check existing unique indexes
mongosh --eval "db.users.getIndexes().filter(i => i.unique)"

# Insert a document and then try a duplicate
mongosh --eval '
  db.test.drop();
  db.test.createIndex({email:1},{unique:true});
  db.test.insertOne({email:"a@b.com"});
  try { db.test.insertOne({email:"a@b.com"}); } catch(e) { print(e); }
'

# Use findAndModify for atomic upsert
mongosh --eval '
  db.test.findAndModify({
    query: {email:"a@b.com"},
    update: {$setOnInsert:{name:"Alice"}},
    upsert: true
  });
'
```