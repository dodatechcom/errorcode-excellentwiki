---
title: "[Solution] bcrypt: data and hash required Error Fix"
description: "Fix bcrypt errors including data and hash required, salt rounds, and password hashing issues in Node.js."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# bcrypt — data and hash required

This error occurs when bcrypt comparison or hashing receives invalid arguments such as undefined data or malformed hashes.

## What This Error Means

Common error messages:

- `Error: data and hash required`
- `Error: Not a string, buffer, or ArrayBuffer`
- `Error: Invalid hash format`

bcrypt.compare() expects both the plaintext password and the stored hash as strings.

## Common Causes

```javascript
// Cause 1: undefined password
bcrypt.compare(undefined, user.password); // data and hash required

// Cause 2: null password
bcrypt.compare(null, user.password);

// Cause 3: Hash is not a valid bcrypt hash
bcrypt.compare('password', 'not-a-bcrypt-hash');

// Cause 4: Password from request body is missing
const { password } = req.body;
bcrypt.compare(password, user.password); // password undefined
```

## How to Fix

### Fix 1: Validate inputs before comparing

```javascript
async function verifyPassword(plainPassword, hashedPassword) {
  if (!plainPassword || !hashedPassword) {
    return false;
  }
  return bcrypt.compare(plainPassword, hashedPassword);
}
```

### Fix 2: Hash passwords with salt

```javascript
async function hashPassword(password) {
  const saltRounds = 12;
  return bcrypt.hash(password, saltRounds);
}
```

### Fix 3: Handle bcrypt errors in route

```javascript
app.post('/login', async (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ error: 'Email and password required' });
  }

  const user = await User.findOne({ email });
  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  const valid = await bcrypt.compare(password, user.passwordHash);
  if (!valid) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  res.json({ success: true });
});
```

### Fix 4: Validate hash format

```javascript
function isValidBcryptHash(hash) {
  return /^\$2[aby]?\$\d{1,2}\$/.test(hash);
}

async function safeCompare(password, storedHash) {
  if (!isValidBcryptHash(storedHash)) {
    throw new Error('Invalid hash format');
  }
  return bcrypt.compare(password, storedHash);
}
```

## Examples

```javascript
const bcrypt = require('bcrypt');

// This triggers error
bcrypt.compare(undefined, '$2b$10$...'); // Error: data and hash required

// Fix: validate first
if (password && user.passwordHash) {
  const match = await bcrypt.compare(password, user.passwordHash);
}
```

## Related Errors

- [Passport Error]({{< relref "/languages/javascript/passport-error" >}}) — authentication failed
- [JWT Error]({{< relref "/languages/javascript/jsonwebtoken-error" >}}) — token invalid
- [Mongoose Validation]({{< relref "/languages/javascript/mongoose-validation" >}}) — validation error
