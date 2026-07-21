---
title: "[Solution] Express Deprecation Warning Error"
description: "Fix Express deprecation warnings when using outdated APIs that will be removed in future versions."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

An Express deprecation warning occurs when the application uses APIs marked as deprecated in newer Express versions, producing console warnings that may become breaking errors in future releases.

## Common Causes

- Using `app.del()` instead of `app.delete()`
- `res.sendfile()` instead of `res.sendFile()`
- `req.param()` instead of explicit `req.params`, `req.body`, or `req.query`
- `app.configure()` which was removed in Express 4
- Using `res.json(status, obj)` instead of `res.status(x).json()`

## How to Fix

1. Replace deprecated methods with their modern equivalents:

```javascript
// Deprecated
app.del('/api/users/:id', handler);
app.configure('production', () => { ... });

// Fixed
app.delete('/api/users/:id', handler);
if (app.get('env') === 'production') { ... }
```

2. Update response methods to use chained status:

```javascript
// Deprecated
res.send(404, { error: 'Not found' });
res.json(500, { error: 'Server error' });

// Fixed
res.status(404).json({ error: 'Not found' });
res.status(500).json({ error: 'Server error' });
```

3. Replace `req.param()` with explicit source:

```javascript
// Deprecated
const id = req.param('id');

// Fixed -- be explicit about the source
const id = req.params.id || req.query.id || req.body.id;
```

## Examples

```javascript
// Deprecated API usage produces warnings
app.del('/api/items/:id', (req, res) => {
  deleteItem(req.params.id);
  res.send(200); // Also deprecated
});

// Fixed
app.delete('/api/items/:id', (req, res) => {
  deleteItem(req.params.id);
  res.sendStatus(200);
});
```

```text
(node:12345) [DEP0066] DeprecationWarning: res.send(status) is deprecated.
Use res.sendStatus(status) instead
```
