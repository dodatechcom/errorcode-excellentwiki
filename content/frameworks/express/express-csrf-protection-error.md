---
title: "[Solution] Express CSRF Protection Error"
description: "Fix Express CSRF protection errors when forms or API requests are rejected due to missing or invalid tokens."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A CSRF protection error in Express occurs when a state-changing request is rejected because it lacks a valid CSRF token. This happens when the CSRF middleware is not configured correctly or the client fails to include the token in requests.

## Common Causes

- CSRF token not included in form submissions or AJAX headers
- Token generated for a different session or cookie
- SameSite cookie attribute set to None allowing cross-origin reads
- CSRF middleware applied to API routes that use token-based auth
- Token expiration before the form is submitted

## How to Fix

1. Use the `csurf` middleware with proper configuration:

```javascript
const csrf = require('csurf');
const cookieParser = require('cookie-parser');

app.use(cookieParser());
app.use(csrf({ cookie: { httpOnly: true, sameSite: 'strict' } }));

app.get('/form', (req, res) => {
  res.render('form', { csrfToken: req.csrfToken() });
});

app.post('/form', (req, res) => {
  // Token validated automatically
  res.json({ success: true });
});
```

2. Include the token in AJAX requests:

```javascript
// Client-side
const token = document.querySelector('meta[name="csrf-token"]').content;

fetch('/api/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRF-Token': token
  },
  body: JSON.stringify({ key: 'value' })
});
```

3. Skip CSRF for token-authenticated API routes:

```javascript
app.use(csrf({
  ignoreMethods: ['GET', 'HEAD', 'OPTIONS'],
  ignorePaths: ['/api/webhooks']
}));
```

## Examples

```javascript
// Token missing from request body
app.use(csrf());

app.post('/transfer', (req, res) => {
  // Fails if _csrf not in body or X-CSRF-Token header
  processTransfer(req.body);
});
```

```text
Error [ERR_CSRF_TOKEN_MISSING]: csurf token missing
```
