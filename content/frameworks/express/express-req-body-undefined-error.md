---
title: "[Solution] Express req.body is Undefined Error"
description: "Fix Express req.body undefined error by configuring body parser middleware correctly before route handlers."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when `req.body` is `undefined` in an Express route handler because the body parser middleware is not configured or is registered after the route definition. Express does not parse request bodies by default.

## Common Causes

- `express.json()` middleware not added to the app
- Body parser middleware registered after route definitions
- Client sends `multipart/form-data` but only `express.json()` is configured
- Content-Type header missing or incorrect in the client request
- Body parser middleware scoped to a different route path

## How to Fix

1. Register body parser middleware before defining routes:

```javascript
const express = require('express');
const app = express();

// Body parser MUST come before routes
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/api/users', (req, res) => {
  console.log(req.body); // Now contains parsed data
  res.json({ received: req.body });
});
```

2. Add route-specific body parser when needed:

```javascript
app.post('/api/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  console.log(req.body); // Raw buffer
  res.status(200).send('OK');
});

app.post('/api/form', express.urlencoded({ extended: true }), (req, res) => {
  console.log(req.body); // Parsed form data
  res.json(req.body);
});
```

3. Verify client sends the correct Content-Type header:

```javascript
// Client-side fix
fetch('/api/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ name: 'Alice', email: 'alice@example.com' })
});
```

## Examples

```javascript
// Wrong: body parser after routes
app.post('/api/data', (req, res) => {
  console.log(req.body); // undefined
  res.json(req.body);
});

app.use(express.json()); // Too late -- middleware order matters

// Correct order
app.use(express.json());
app.post('/api/data', (req, res) => {
  console.log(req.body); // { name: 'test' }
  res.json(req.body);
});
```

```text
TypeError: Cannot read properties of undefined (reading 'email')
```
