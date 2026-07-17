---
title: "[Solution] JsonWebTokenError: invalid signature Fix"
description: "Fix JWT (JsonWebToken) errors including invalid signature, expired tokens, and malformed tokens in Node.js applications."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jwt", "jsonwebtoken", "token", "auth", "signature", "expired"]
weight: 5
---

# JsonWebTokenError — invalid signature

This error occurs when JWT token verification fails due to signature mismatch, expired token, or malformed token format.

## What This Error Means

Common error messages:

- `JsonWebTokenError: invalid signature`
- `TokenExpiredError: jwt expired`
- `JsonWebTokenError: jwt malformed`

JWT tokens have three parts: header, payload, and signature. Verification fails when the signature doesn't match the payload using the provided secret.

## Common Causes

```javascript
// Cause 1: Wrong secret/key
const token = jwt.sign({ id: 1 }, 'secret-key');
jwt.verify(token, 'wrong-key'); // invalid signature

// Cause 2: Token expired
const token = jwt.sign({ id: 1 }, 'secret', { expiresIn: '1h' });
// Wait 1+ hours
jwt.verify(token, 'secret'); // TokenExpiredError

// Cause 3: Token modified after signing
const token = jwt.sign({ id: 1 }, 'secret');
// Manually change payload → invalid signature

// Cause 4: Different algorithm used
const token = jwt.sign({ id: 1 }, 'secret', { algorithm: 'HS256' });
jwt.verify(token, 'secret', { algorithms: ['RS256'] }); // algorithm mismatch
```

## How to Fix

### Fix 1: Verify with correct secret

```javascript
const jwt = require('jsonwebtoken');

const SECRET = process.env.JWT_SECRET;

const token = jwt.sign({ id: user.id }, SECRET, { expiresIn: '24h' });

// Later
try {
  const decoded = jwt.verify(token, SECRET);
} catch (err) {
  if (err.name === 'JsonWebTokenError') {
    return res.status(401).json({ error: 'Invalid token' });
  }
}
```

### Fix 2: Handle token expiry

```javascript
try {
  const decoded = jwt.verify(token, SECRET);
  req.user = decoded;
} catch (err) {
  if (err.name === 'TokenExpiredError') {
    return res.status(401).json({ error: 'Token expired' });
  }
  return res.status(401).json({ error: 'Invalid token' });
}
```

### Fix 3: Implement token refresh

```javascript
app.post('/refresh', (req, res) => {
  const { refreshToken } = req.body;
  try {
    const decoded = jwt.verify(refreshToken, REFRESH_SECRET);
    const newToken = jwt.sign({ id: decoded.id }, SECRET, { expiresIn: '1h' });
    res.json({ token: newToken });
  } catch (err) {
    res.status(401).json({ error: 'Invalid refresh token' });
  }
});
```

### Fix 4: Specify allowed algorithms

```javascript
jwt.verify(token, SECRET, { algorithms: ['HS256'] });
```

## Examples

```javascript
const jwt = require('jsonwebtoken');

// This triggers invalid signature
const token = jwt.sign({ id: 1 }, 'secret-a');
const decoded = jwt.verify(token, 'secret-b'); // JsonWebTokenError

// Fix: use same secret
const decoded = jwt.verify(token, 'secret-a'); // works
```

## Related Errors

- [Passport Error]({{< relref "/languages/javascript/passport-error" >}}) — authentication failed
- [Express Session]({{< relref "/languages/javascript/express-session" >}}) — session error
- [CORS Error]({{< relref "/languages/javascript/cors-error" >}}) — CORS policy
