---
title: "[Solution] Express Input Validation Error"
description: "Fix Express input validation errors when request data fails schema checks or type constraints."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

An input validation error in Express occurs when the request body, query parameters, or URL params do not match the expected schema, type, or format. This causes runtime errors when the application tries to use invalid data.

## Common Causes

- No validation middleware applied to routes
- Validation schema does not match the actual request structure
- Client sends string when number is expected
- Required fields missing from request body
- Validation runs but errors are not returned to the client

## How to Fix

1. Use `joi` or `zod` for schema validation:

```javascript
const { z } = require('zod');

const UserSchema = z.object({
  name: z.string().min(2).max(50),
  email: z.string().email(),
  age: z.number().int().min(18).max(120)
});

app.post('/api/users', (req, res, next) => {
  const result = UserSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({
      errors: result.error.flatten().fieldErrors
    });
  }
  // result.data is validated and typed
  createUser(result.data);
  res.status(201).json(result.data);
});
```

2. Create a reusable validation middleware:

```javascript
const validate = (schema) => (req, res, next) => {
  const result = schema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ errors: result.error.issues });
  }
  req.validated = result.data;
  next();
};

app.post('/api/orders', validate(OrderSchema), (req, res) => {
  createOrder(req.validated);
  res.status(201).json({ success: true });
});
```

3. Validate query parameters and URL params:

```javascript
const QuerySchema = z.object({
  page: z.coerce.number().int().min(1).default(1),
  limit: z.coerce.number().int().min(1).max(100).default(20),
  search: z.string().optional()
});

app.get('/api/users', (req, res, next) => {
  const result = QuerySchema.safeParse(req.query);
  if (!result.success) {
    return res.status(400).json({ errors: result.error.flatten().fieldErrors });
  }
  // result.data contains parsed and validated values
  fetchUsers(result.data);
});
```

## Examples

```javascript
// Without validation -- crashes on bad data
app.post('/api/transfer', (req, res) => {
  const amount = parseFloat(req.body.amount); // NaN if invalid
  const balance = account.balance - amount; // NaN propagation
  if (balance < 0) throw new Error('Insufficient funds');
});

// With validation
app.post('/api/transfer', (req, res, next) => {
  const schema = z.object({
    amount: z.number().positive(),
    toAccount: z.string().uuid()
  });
  const result = schema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ errors: result.error.flatten() });
  }
  // Safe to use result.data.amount
});
```

```text
TypeError: Cannot read properties of undefined (reading 'email')
```
