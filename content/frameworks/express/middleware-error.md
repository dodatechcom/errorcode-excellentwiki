---
title: "TypeError: X is not a function"
description: "Express raises this TypeError when a value used as middleware or a route handler is not a function."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["middleware", "routes", "typescript", "node"]
weight: 5
---

This error occurs when Express expects a function (for middleware or a route handler) but receives something else, such as `undefined`, a string, or an object. It is common when imports are incorrect or when wrapping a function unintentionally.

## Common Causes

- Importing a non-function export as middleware (e.g. `module.exports = { router }` instead of `module.exports = router`)
- Accidentally calling a function before passing it as middleware (e.g. `app.use(auth())` instead of `app.use(auth)`)
- TypeScript compilation outputting a different export shape than expected
- The middleware module file has a syntax error so the import resolves to `undefined`

## How to Fix

Verify the import is actually a function:

```javascript
const auth = require("./middleware/auth");
console.log(typeof auth); // should be "function"
```

If the middleware requires configuration, wrap it in a factory function:

```javascript
// middleware/auth.js
module.exports = function (options) {
  return function (req, res, next) {
    // use options
    next();
  };
};

// app.js
app.use(auth({ secret: "abc" }));
```

## Example

```javascript
// middleware/auth.js
module.exports = { checkAuth: (req, res, next) => next() };

// app.js
const auth = require("./middleware/auth");
app.use(auth); // TypeError: auth is not a function — it's an object
```

## Related Errors

- [Error: Cannot set headers after they are sent]({{< relref "/frameworks/express/cannot-set-headers" >}})
