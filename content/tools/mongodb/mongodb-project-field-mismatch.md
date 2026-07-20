---
title: "[Solution] MongoDB $project Field Mismatch Error"
description: "Fix MongoDB $project aggregation stage field errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB $project Field Mismatch Error

The `$project` stage can produce unexpected errors:

```
MongoServerError: $project with inclusion and exclusion cannot coexist
```

```
Cannot create field 'x' in element {_id: ...}
```

## Common Causes

- Mixing inclusion (1) and exclusion (0) in the same $project stage
- Referencing a field that does not exist
- Trying to project `_id` as 0 without explicit exclusion
- Using a field path that conflicts with an existing field

## How to Fix

### 1. Use only inclusion OR exclusion, not both

```javascript
// Wrong: mixing inclusion and exclusion
db.users.aggregate([
  { $project: { name: 1, email: 0 } }  // Error!
]);

// Correct: inclusion only
db.users.aggregate([
  { $project: { name: 1, email: 1 } }
]);
```

### 2. Exclude _id explicitly when using inclusion

```javascript
db.users.aggregate([
  { $project: { _id: 0, name: 1, email: 1 } }
]);
```

### 3. Use $addFields instead of $project for computed fields

```javascript
db.users.aggregate([
  { $addFields: { fullName: { $concat: ["$firstName", " ", "$lastName"] } } }
]);
```

### 4. Use $replaceRoot or $replaceWith for complete restructuring

```javascript
db.users.aggregate([
  { $replaceRoot: { newRoot: { name: "$name", email: "$email" } } }
]);
```

## Examples

```bash
# Demonstrate inclusion/exclusion error
mongosh --eval '
  db.test.drop();
  db.test.insertOne({name:"Alice",age:30,email:"a@test.com"});
  try {
    db.test.aggregate([{$project:{name:1,email:0}}]);
  } catch(e) { print("Error:", e.message); }
'

# Fix: use only inclusion
mongosh --eval '
  let result = db.test.aggregate([{$project:{_id:0,name:1,age:1}}]).toArray();
  printjson(result);
'
```