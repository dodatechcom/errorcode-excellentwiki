---
title: "[Solution] Mongoose Validation Error Fix"
description: "Fix Mongoose validation errors when saving documents. Handle required fields, custom validators, and schema validation in MongoDB."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Mongoose Validation Error

This error occurs when a Mongoose document fails schema validation during `save()` or `create()`. Mongoose validates fields against the schema rules.

## What This Error Means

Common error messages:

- `ValidationError: Path 'email' is required`
- `ValidationError: Path 'age' (15) is below minimum (18)`
- `CastError: Cast to string failed for value "123"`

Mongoose validates before saving. Invalid data triggers ValidationError.

## Common Causes

```javascript
// Cause 1: Missing required field
const userSchema = new Schema({
  name: { type: String, required: true },
});
const User = mongoose.model('User', userSchema);
await User.create({}); // ValidationError: name required

// Cause 2: Value doesn't match enum
const schema = new Schema({
  role: { type: String, enum: ['admin', 'user'] },
});
await User.create({ role: 'superadmin' }); // not in enum

// Cause 3: Number below minimum
const schema = new Schema({
  age: { type: Number, min: 18 },
});
await User.create({ age: 10 }); // ValidationError: min

// Cause 4: Custom validator fails
const schema = new Schema({
  email: {
    type: String,
    validate: {
      validator: (v) => v.includes('@'),
      message: 'Invalid email',
    },
  },
});
await User.create({ email: 'bad' }); // validation fails
```

## How to Fix

### Fix 1: Validate before save

```javascript
try {
  await user.save();
} catch (err) {
  if (err.name === 'ValidationError') {
    const messages = Object.values(err.errors).map(e => e.message);
    return res.status(400).json({ errors: messages });
  }
  throw err;
}
```

### Fix 2: Use runValidators option

```javascript
await User.findByIdAndUpdate(id, update, {
  runValidators: true, // validate before update
  new: true,
});
```

### Fix 3: Handle validation errors in middleware

```javascript
userSchema.pre('save', function (next) {
  if (this.age < 0) {
    this.invalidate('age', 'Age must be positive');
  }
  next();
});
```

### Fix 4: Use default values

```javascript
const userSchema = new Schema({
  name: { type: String, required: true },
  role: { type: String, default: 'user' },
  status: { type: String, enum: ['active', 'inactive'], default: 'active' },
});
```

## Examples

```javascript
const userSchema = new Schema({
  email: { type: String, required: true },
  age: { type: Number, min: 18, max: 120 },
});

// This triggers validation error
try {
  await User.create({ age: 5 });
} catch (err) {
  console.error(err.errors.age.message);
  // "Path 'age' (5) is below minimum (18)"
}
```

## Related Errors

- [Mongoose CastError]({{< relref "/languages/javascript/mongoose-casterror" >}}) — cast to ObjectId
- [Mongoose Duplicate]({{< relref "/languages/javascript/mongoose-duplicate" >}}) — duplicate key
- [Prisma Error]({{< relref "/languages/javascript/prisma-error" >}}) — Prisma error
