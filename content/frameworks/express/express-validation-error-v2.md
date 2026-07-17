---
title: "express-validator Validation Error"
description: "Fix Express-validator errors when request data fails validation rules for type, format, or required fields."
frameworks: ["express.js"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["validation", "sanitization", "input", "sanitize", "express"]
weight: 5
---

## What This Error Means

`express-validator` middleware checks incoming request data against defined rules. When validation fails, the `validationResult()` function returns error objects. If these errors are not checked and handled, invalid data passes through to your route handlers, causing downstream bugs or security vulnerabilities.

## Common Causes

- Validation errors are not checked with `validationResult(req)`
- Required fields are missing from the request body or params
- Data type mismatch (string sent where number expected)
- Regex or format validation fails (email, UUID, etc.)
- Validation middleware is not applied to the correct route

## How to Fix

### Use Validation Chains with Error Handling

```javascript
const { body, validationResult } = require('express-validator');

app.post('/users',
  [
    body('email').isEmail().normalizeEmail(),
    body('password').isLength({ min: 8 }),
    body('name').trim().notEmpty()
  ],
  (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({
        error: 'Validation failed',
        details: errors.array()
      });
    }
    // Validated data in req.body
    res.json({ user: req.body });
  }
);
```

### Create a Reusable Validation Middleware

```javascript
const { validationResult } = require('express-validator');

function validate(req, res, next) {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({
      error: 'Validation failed',
      fields: errors.array().map(e => ({
        field: e.path,
        message: e.msg,
        value: e.value
      }))
    });
  }
  next();
}

// Use with validation chains
app.post('/register', [
  body('email').isEmail(),
  body('password').isLength({ min: 8 }),
  body('age').isInt({ min: 18 })
], validate, (req, res) => {
  res.json({ registered: true });
});
```

### Validate URL Parameters and Query Strings

```javascript
const { param, query } = require('express-validator');

app.get('/users/:id',
  [param('id').isUUID()],
  validate,
  (req, res) => {
    res.json({ userId: req.params.id });
  }
);

app.get('/search',
  [query('q').trim().notEmpty(), query('page').isInt({ min: 1 }).optional()],
  validate,
  (req, res) => {
    res.json({ query: req.query.q });
  }
);
```

## Related Errors

- [Express BodyParser Error]({{< relref "/frameworks/express/express-body-parser-error-v2" >}}) — JSON parse failure
- [Express File Upload Error]({{< relref "/frameworks/express/express-file-upload-error-v2" >}}) — multer upload failure
