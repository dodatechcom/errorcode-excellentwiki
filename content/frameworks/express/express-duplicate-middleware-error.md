---
title: "[Solution] Express Duplicate Middleware Error"
description: "Fix Express duplicate middleware errors when the same middleware runs multiple times on a single request."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A duplicate middleware error in Express occurs when the same middleware function is registered more than once, causing it to execute multiple times per request. This leads to double headers, duplicate logging, or unexpected behavior.

## Common Causes

- Same middleware imported and used multiple times
- Middleware registered at both app and router level
- Hot module reloading registers middleware again
- Library internally adds middleware that is also added manually
- `app.use()` called in multiple files without deduplication

## How to Fix

1. Track registered middleware to prevent duplicates:

```javascript
const registered = new Set();

function uniqueMiddleware(middleware, name) {
  if (registered.has(name)) {
    console.warn(`Middleware '${name}' already registered, skipping`);
    return (req, res, next) => next();
  }
  registered.add(name);
  return middleware;
}

app.use(uniqueMiddleware(cors(), 'cors'));
app.use(uniqueMiddleware(helmet(), 'helmet'));
app.use(uniqueMiddleware(compression(), 'compression'));
```

2. Centralize middleware registration:

```javascript
// middleware/index.js
const cors = require('cors');
const helmet = require('helmet');

module.exports = (app) => {
  app.use(cors());
  app.use(helmet());
  app.use(express.json());
};

// server.js
const setupMiddleware = require('./middleware');
setupMiddleware(app);
```

3. Check if middleware is already applied:

```javascript
function safeUse(app, path, middleware) {
  if (!app._router) return app.use(path, middleware);

  const stack = app._router.stack;
  const alreadyExists = stack.some(layer => layer.handle === middleware);

  if (alreadyExists) {
    return app; // Skip -- already registered
  }

  return app.use(path, middleware);
}

safeUse(app, cors());
```

## Examples

```javascript
// Bug: CORS headers sent twice
const cors = require('cors');
app.use(cors());
app.use(cors()); // Duplicate -- Access-Control-Allow-Origin appears twice

// Fixed: register once
app.use(cors());
```

```text
Access-Control-Allow-Origin header is sent twice in the response
```
