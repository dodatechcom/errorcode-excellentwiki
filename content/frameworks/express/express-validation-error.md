---
title: "[Solution] Express Validation Error"
description: "Fix Express validation errors. Resolve request data validation failures."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["validation", "joi", "express-validator", "sanitize", "express"]
weight: 5
---

An Express validation error occurs when request data fails validation rules. This can be for body, query parameters, or route parameters.

## Common Causes

- Required fields are missing
- Data type mismatches
- String does not match expected pattern
- Value outside allowed range
- Custom validation logic failing

## How to Fix

### Use express-validator

```javascript
const { body, validationResult } = require('express-validator');

app.post('/user', [
  body('email').isEmail().normalizeEmail(),
  body('password').isLength({ min: 6 }),
  body('name').trim().notEmpty(),
], (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }
  // Process valid data
});
```

### Use Joi for Validation

```javascript
const Joi = require('joi');

const schema = Joi.object({
  email: Joi.string().email().required(),
  password: Joi.string().min(6).required(),
});

app.post('/user', (req, res) => {
  const { error } = schema.validate(req.body);
  if (error) {
    return res.status(400).json({ error: error.details[0].message });
  }
});
```

### Validate URL Parameters

```javascript
app.get('/user/:id', [
  param('id').isInt().withMessage('ID must be an integer'),
], (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }
});
```

## Examples

```javascript
// Example 1: Missing required field
// POST /user with { "email": "" }
// 400: "email" is not allowed to be empty
// Fix: provide valid email

// Example 2: Type mismatch
// GET /user/abc (expected integer)
// 400: "id" must be an integer
// Fix: use numeric ID
```

## Related Errors

- [Express BodyParser Error]({{< relref "/frameworks/express/express-body-parser-error" >}}) — body parsing error
- [Express 404 Error]({{< relref "/frameworks/express/express-404-error" >}}) — route not found
