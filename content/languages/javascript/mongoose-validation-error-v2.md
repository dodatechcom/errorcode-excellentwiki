---
title: "[Solution] Mongoose: Validation Error Fix"
description: "Fix Mongoose ValidationError when saving documents with invalid data. Handle schema validation, custom validators, and error formatting."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Mongoose: Validation Error

This error occurs when `document.save()` or `Model.create()` is called with data that fails schema validation. Mongoose validates all fields before writing to MongoDB and throws a `ValidationError` with details for each failing field.

## What This Error Means

Common error messages:

- `ValidationError: User validation failed: email: Path 'email' is required.`
- `ValidationError: Product validation failed: price: Path 'price' (5) is less than minimum allowed value (0.01).`
- `ValidatorError: Path 'username' is required.`
- `CastError: Cast to String failed for value "123" at path "name"`

Mongoose validates against the schema definition, custom validators, and required fields. Errors include which field failed and the validation rule.

## Common Causes

```javascript
// Cause 1: Missing required field
const userSchema = new Schema({
  name: { type: String, required: true },
  email: { type: String, required: true },
});
const User = mongoose.model('User', userSchema);

await User.create({ name: 'Alice' }); // email is required

// Cause 2: Custom validator failure
const productSchema = new Schema({
  price: {
    type: Number,
    validate: {
      validator: (v) => v > 0,
      message: 'Price must be positive',
    },
  },
});

await Product.create({ price: -10 }); // validation fails

// Cause 3: Enum validation
const statusSchema = new Schema({
  status: { type: String, enum: ['active', 'inactive', 'pending'] },
});

await Status.create({ status: 'deleted' }); // not in enum

// Cause 4: Min/Max length
const userSchema = new Schema({
  username: { type: String, minlength: 3, maxlength: 50 },
});

await User.create({ username: 'ab' }); // too short
```

## How to Fix

### Fix 1: Handle validation errors properly

```javascript
try {
  await User.create({ name: 'Alice' });
} catch (err) {
  if (err.name === 'ValidationError') {
    const messages = Object.values(err.errors).map(e => e.message);
    console.error('Validation failed:', messages);
    // ["User validation failed: email: Path 'email' is required."]
  }
}
```

### Fix 2: Use runValidators option on updates

```javascript
// By default, update operations skip validation
await User.updateOne(
  { _id: userId },
  { $set: { email: 'invalid' } },
  { runValidators: true } // validate before updating
);
```

### Fix 3: Add custom error messages

```javascript
const userSchema = new Schema({
  email: {
    type: String,
    required: [true, 'Email address is required'],
    match: [/^\S+@\S+\.\S+$/, 'Please provide a valid email address'],
  },
  age: {
    type: Number,
    min: [0, 'Age cannot be negative'],
    max: [150, 'Age seems unrealistic'],
  },
});
```

### Fix 4: Use trim and lowercase for normalization

```javascript
const userSchema = new Schema({
  email: {
    type: String,
    required: true,
    lowercase: true,
    trim: true,
  },
  username: {
    type: String,
    required: true,
    trim: true,
    minlength: 3,
  },
});
```

## Examples

```
ValidationError: User validation failed:
  email: Path 'email' is required.
  age: Path 'age' (-1) is less than minimum allowed value (0).
```

```javascript
// Fix: format validation errors for API responses
function formatValidationError(err) {
  if (err.name === 'ValidationError') {
    const errors = {};
    Object.keys(err.errors).forEach(key => {
      errors[key] = err.errors[key].message;
    });
    return { status: 400, errors };
  }
  throw err;
}
```

## Related Errors

- [Mongoose Validation]({{< relref "/languages/javascript/mongoose-validation" >}}) — basic validation error
- [Mongoose CastError V2]({{< relref "/languages/javascript/mongoose-cast-error-v2" >}}) — CastError to ObjectId
- [Prisma Error V2]({{< relref "/languages/javascript/prisma-error-v2" >}}) — PrismaClientKnownRequestError
