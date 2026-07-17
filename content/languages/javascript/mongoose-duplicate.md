---
title: "[Solution] Mongoose Duplicate Key Error Fix"
description: "Fix Mongoose duplicate key errors when inserting documents with unique field conflicts. Handle E11000 errors and unique indexes."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["mongoose", "mongodb", "duplicate-key", "e11000", "unique-index"]
weight: 5
---

# Mongoose Duplicate Key Error

This error occurs when trying to insert a document that violates a unique index constraint. MongoDB returns error code E11000.

## What This Error Means

Common error messages:

- `MongoServerError: E11000 duplicate key error collection: db.users index: email_1 dup key: { email: "test@example.com" }`
- `MongoError: E11000 duplicate key error`
- `ValidationError: Path 'email' (test@example.com) is not unique`

Unique indexes prevent duplicate values in a field.

## Common Causes

```javascript
// Cause 1: Inserting duplicate unique field
const userSchema = new Schema({
  email: { type: String, unique: true },
});
await User.create({ email: 'test@example.com' });
await User.create({ email: 'test@example.com' }); // duplicate key

// Cause 2: Race condition
// Two requests try to create same user simultaneously

// Cause 3: Updating to duplicate value
await User.findByIdAndUpdate(id, { email: 'existing@example.com' });

// Cause 4: Bulk insert with duplicates
await User.insertMany([
  { email: 'a@test.com' },
  { email: 'a@test.com' }, // duplicate
]);
```

## How to Fix

### Fix 1: Handle duplicate key errors

```javascript
try {
  await User.create({ email: 'test@example.com' });
} catch (err) {
  if (err.code === 11000) {
    return res.status(409).json({ error: 'Email already exists' });
  }
  throw err;
}
```

### Fix 2: Use upsert

```javascript
await User.findOneAndUpdate(
  { email: 'test@example.com' },
  { $setOnInsert: { email: 'test@example.com', name: 'User' } },
  { upsert: true, new: true }
);
```

### Fix 3: Check before insert

```javascript
const existing = await User.findOne({ email: 'test@example.com' });
if (existing) {
  return res.status(409).json({ error: 'Email already in use' });
}
await User.create({ email: 'test@example.com' });
```

### Fix 4: Use try-catch in bulk operations

```javascript
const results = await Promise.allSettled(
  users.map(user => User.create(user))
);

const failures = results.filter(r => r.status === 'rejected');
const successes = results.filter(r => r.status === 'fulfilled');
```

## Examples

```javascript
// This triggers duplicate key error
const userSchema = new Schema({ email: { type: String, unique: true } });
const User = mongoose.model('User', userSchema);

try {
  await User.create({ email: 'duplicate@test.com' });
  await User.create({ email: 'duplicate@test.com' }); // E11000
} catch (err) {
  console.error(err.code); // 11000
}
```

## Related Errors

- [Mongoose Validation]({{< relref "/languages/javascript/mongoose-validation" >}}) — validation error
- [Mongoose CastError]({{< relref "/languages/javascript/mongoose-casterror" >}}) — cast to ObjectId
- [Sequelize Error]({{< relref "/languages/javascript/sequelize-error" >}}) — database error
