---
title: "[Solution] Express req.params undefined Error Fix"
description: "Fix Express req.params being undefined. Define route parameters correctly, use named params, and handle missing parameters."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["express", "params", "route-parameters", "named-params", "undefined"]
weight: 5
---

# Express req.params — undefined

This error occurs when `req.params` is undefined or when accessing a route parameter that wasn't defined in the route pattern.

## What This Error Means

Common error messages:

- `TypeError: Cannot read properties of undefined (reading 'id')`
- `req.params is undefined`
- `Cannot destructure property 'id' of req.params`

`req.params` contains route parameters defined with `:paramName` in the route path.

## Common Causes

```javascript
// Cause 1: Route doesn't define parameters
app.get('/api/users', (req, res) => {
  console.log(req.params.id); // undefined - no :id in route
});

// Cause 2: Wrong parameter name
app.get('/api/users/:userId', (req, res) => {
  console.log(req.params.id); // undefined - param is 'userId' not 'id'
});

// Cause 3: Missing route entirely
// Route not defined, falls through to 404

// Cause 4: Router mounting issue
const router = express.Router();
router.get('/:id', handler);
app.use('/api', router);
// req.params.id works for /api/users/123
```

## How to Fix

### Fix 1: Define parameters in route

```javascript
// Wrong
app.get('/api/users', (req, res) => {
  const { id } = req.params; // undefined
});

// Correct
app.get('/api/users/:id', (req, res) => {
  const { id } = req.params; // "123"
  res.json({ userId: id });
});
```

### Fix 2: Match parameter names

```javascript
app.get('/api/users/:userId/posts/:postId', (req, res) => {
  const { userId, postId } = req.params; // both defined
  res.json({ userId, postId });
});
```

### Fix 3: Handle missing params

```javascript
app.get('/api/users/:id?', (req, res) => { // ? makes optional
  if (!req.params.id) {
    return res.json({ users: 'all' });
  }
  res.json({ user: req.params.id });
});
```

### Fix 4: Validate params

```javascript
app.get('/api/users/:id', (req, res) => {
  const { id } = req.params;

  if (!id || isNaN(id)) {
    return res.status(400).json({ error: 'Invalid user ID' });
  }

  // proceed with valid id
  res.json({ userId: parseInt(id) });
});
```

## Examples

```javascript
// This triggers undefined params
app.get('/api/products', (req, res) => {
  console.log(req.params.id); // undefined
});

// Fix
app.get('/api/products/:id', (req, res) => {
  console.log(req.params.id); // "456"
  res.json({ productId: req.params.id });
});
```

## Related Errors

- [Express Route 404]({{< relref "/languages/javascript/express-route" >}}) — route not found
- [Express Middleware]({{< relref "/languages/javascript/express-middleware" >}}) — middleware error
- [Express Session]({{< relref "/languages/javascript/express-session" >}}) — session error
