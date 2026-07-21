---
title: "[Solution] Express Route Parameter Missing Error"
description: "Fix Express route parameter errors when required URL parameters are undefined or contain invalid values."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A route parameter missing error in Express occurs when a route handler tries to use `req.params` values that are `undefined` because the route was not matched with the expected parameter pattern.

## Common Causes

- Route path does not include the expected parameter
- Parameter pattern does not match the actual URL format
- Client sends request to a different route that lacks the param
- Regex constraint in route path rejects valid values
- Optional parameters not handled with `?` suffix

## How to Fix

1. Validate route parameters before using them:

```javascript
app.get('/api/users/:id', (req, res) => {
  const { id } = req.params;
  if (!id || isNaN(parseInt(id))) {
    return res.status(400).json({ error: 'Invalid user ID' });
  }
  const user = User.findById(parseInt(id));
  if (!user) return res.status(404).json({ error: 'User not found' });
  res.json(user);
});
```

2. Use regex constraints on route parameters:

```javascript
// Only match numeric IDs
app.get('/api/orders/:id(\\d+)', (req, res) => {
  const order = Order.findById(parseInt(req.params.id));
  res.json(order);
});

// Match UUID format
app.get('/api/items/:id([a-f0-9-]{36})', (req, res) => {
  const item = Item.findById(req.params.id);
  res.json(item);
});
```

3. Create a middleware to validate required params:

```javascript
function requireParams(...params) {
  return (req, res, next) => {
    const missing = params.filter(p => !req.params[p]);
    if (missing.length > 0) {
      return res.status(400).json({ error: `Missing parameters: ${missing.join(', ')}` });
    }
    next();
  };
}

app.get('/api/users/:id/posts/:postId', requireParams('id', 'postId'), (req, res) => {
  const posts = getPostsByUser(req.params.id, req.params.postId);
  res.json(posts);
});
```

## Examples

```javascript
// Bug: route does not capture the ID
app.get('/api/users/', (req, res) => {
  console.log(req.params.id); // undefined -- route has no :id
});

// Fixed: add parameter to route
app.get('/api/users/:id', (req, res) => {
  console.log(req.params.id); // "42"
});
```

```text
TypeError: Cannot destructure property 'id' of undefined
```
