---
title: "[Solution] Express JWT Verification Error"
description: "Fix Express JWT verification errors. Resolve JSON Web Token authentication issues."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An Express JWT verification error occurs when the JSON Web Token provided by the client is invalid, expired, or malformed.

## Common Causes

- Token is expired (exp claim)
- Token signature does not match
- Secret key does not match the signing key
- Token format is invalid (not Bearer scheme)
- Token was tampered with

## How to Fix

### Verify Token Manually

```javascript
const jwt = require('jsonwebtoken');

try {
  const decoded = jwt.verify(token, process.env.JWT_SECRET);
  console.log(decoded);
} catch (err) {
  console.error(err.message);
}
```

### Use express-jwt Middleware

```javascript
const { expressjwt: jwt } = require('express-jwt');

app.use(jwt({ secret: process.env.JWT_SECRET, algorithms: ['HS256'] }));
```

### Handle JWT Errors

```javascript
app.use((err, req, res, next) => {
  if (err.name === 'UnauthorizedError') {
    return res.status(401).json({ error: 'Invalid token' });
  }
  next(err);
});
```

### Check Token Format

```javascript
// Expected: "Bearer <token>"
const authHeader = req.headers.authorization;
const token = authHeader && authHeader.split(' ')[1];
```

## Examples

```javascript
// Example 1: Expired token
jwt.verify(expiredToken, secret);
// TokenExpiredError: jwt expired
// Fix: refresh the token

// Example 2: Wrong secret
jwt.verify(token, 'wrong-secret');
// JsonWebError: invalid signature
// Fix: use correct JWT_SECRET
```

## Related Errors

- [Express Session Error]({{< relref "/frameworks/express/express-session-error" >}}) — session error
- [Express CORS Error]({{< relref "/frameworks/express/express-cors-error" >}}) — CORS error
