---
title: "JWT Verification Failed in Express"
description: "Fix Express JWT errors when token verification fails due to expiration, invalid signature, or missing tokens."
frameworks: ["express.js"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jwt", "token", "auth", "verify", "express"]
weight: 5
---

## What This Error Means

When `express-jwt` or manual JWT verification fails, the middleware throws a `UnauthorizedError`. This happens when a client sends an expired, tampered, malformed, or missing JSON Web Token. Without proper error handling, this results in a generic 401 response with no useful information.

## Common Causes

- JWT has expired (token `exp` claim exceeded)
- Token signature does not match the signing secret
- Authorization header is missing or malformed (`Bearer` prefix missing)
- Wrong secret or public key used for verification
- Token was revoked but still being sent by the client

## How to Fix

### Handle JWT Errors Gracefully

```javascript
const jwt = require('express-jwt');

app.use('/api', jwt({ secret: 'your-secret', algorithms: ['HS256'] }));

app.use((err, req, res, next) => {
  if (err.name === 'UnauthorizedError') {
    return res.status(401).json({
      error: 'Authentication required',
      message: err.message
    });
  }
  next(err);
});
```

### Verify Token Manually with Better Error Messages

```javascript
const jwt = require('jsonwebtoken');

function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({ error: 'Access token required' });
  }

  jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
    if (err) {
      if (err.name === 'TokenExpiredError') {
        return res.status(401).json({ error: 'Token expired' });
      }
      return res.status(403).json({ error: 'Invalid token' });
    }
    req.user = decoded;
    next();
  });
}
```

### Use Algorithm Whitelist

```javascript
app.use('/api', jwt({
  secret: 'your-secret',
  algorithms: ['HS256'] // Restrict to known algorithms
}));
```

### Implement Token Refresh Flow

```javascript
app.post('/refresh', (req, res) => {
  const { refreshToken } = req.body;
  try {
    const decoded = jwt.verify(refreshToken, process.env.REFRESH_SECRET);
    const newAccessToken = jwt.sign(
      { userId: decoded.userId },
      process.env.JWT_SECRET,
      { expiresIn: '15m' }
    );
    res.json({ accessToken: newAccessToken });
  } catch (err) {
    res.status(401).json({ error: 'Invalid refresh token' });
  }
});
```

## Related Errors

- [Express Session Error]({{< relref "/frameworks/express/express-session-error-v2" >}}) — session store issues
- [Express CORS Error]({{< relref "/frameworks/express/express-cors-error-v2" >}}) — cross-origin auth headers blocked
