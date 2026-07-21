---
title: "[Solution] Express Trailing Slash Error"
description: "Fix Express trailing slash errors when routes behave differently with or without a trailing slash."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A trailing slash error in Express occurs when a route responds differently depending on whether the URL has a trailing slash. This causes 404 errors or duplicate content issues when clients access the wrong form.

## Common Causes

- Express treats `/users` and `/users/` as different routes by default
- Static file serving behaves differently with and without trailing slashes
- Redirect from `/users` to `/users/` creates unexpected behavior
- Mixed route definitions with inconsistent trailing slash usage
- SEO issues from duplicate content at both paths

## How to Fix

1. Enable strict routing to treat slashes consistently:

```javascript
app.set('strict routing', true);

// Both must match exactly
app.get('/users', handler);    // Only matches /users
app.get('/users/', handler);   // Only matches /users/
```

2. Redirect all requests to a canonical form:

```javascript
app.use((req, res, next) => {
  // Redirect /users to /users/
  if (req.path !== '/' && !req.path.endsWith('/')) {
    return res.redirect(301, req.path + '/' + req.url.split('?')[1]
      ? '?' + req.url.split('?')[1]
      : '');
  }
  next();
});

app.get('/users/', (req, res) => {
  res.json({ users: [] });
});
```

3. Use a middleware to strip or add trailing slashes:

```javascript
const trim_slash = require('trim-slash');

app.use((req, res, next) => {
  if (req.path.length > 1 && req.path.endsWith('/')) {
    const trimmed = req.path.slice(0, -1);
    const query = req.url.includes('?') ? '?' + req.url.split('?')[1] : '';
    return res.redirect(301, trimmed + query);
  }
  next();
});
```

## Examples

```javascript
// Bug: only one form works
app.get('/api/items', (req, res) => {
  res.json(getItems());
});
// GET /api/items -- works
// GET /api/items/ -- 404

// Fixed: handle both
app.get('/api/items', (req, res) => {
  res.json(getItems());
});

app.get('/api/items/', (req, res) => {
  res.redirect(301, '/api/items');
});
```

```text
Cannot GET /api/items/
```
