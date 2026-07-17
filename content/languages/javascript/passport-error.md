---
title: "[Solution] Passport Authentication Failed Error Fix"
description: "Fix Passport.js authentication failures. Handle strategy errors, callback issues, and session serialization in Passport."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["passport", "authentication", "strategy", "login", "session"]
weight: 5
---

# Passport Authentication Failed

This error occurs when Passport.js fails to authenticate a user due to invalid credentials, strategy misconfiguration, or callback errors.

## What This Error Means

Common error messages:

- `AuthenticationError: Unauthorized`
- `Error: Failed to authenticate`
- `PassportError: Invalid credentials`

Passport uses strategies (local, OAuth, JWT) to authenticate users. Failures in any strategy produce authentication errors.

## Common Causes

```javascript
// Cause 1: Strategy not configured
app.use(passport.initialize());
app.post('/login', passport.authenticate('local')); // strategy not registered

// Cause 2: Verify callback returns false
passport.use(new LocalStrategy((username, password, done) => {
  const user = findUser(username);
  if (!user || user.password !== password) {
    return done(null, false); // auth failed
  }
}));

// Cause 3: Missing session serialization
passport.serializeUser((user, done) => done(null, user.id));
passport.deserializeUser((id, done) => {
  const user = findUserById(id);
  done(null, user); // user not found = error
});

// Cause 4: Wrong callback signature
app.post('/login', passport.authenticate('local', (err, user) => {
  // wrong: should use redirect or custom callback
}));
```

## How to Fix

### Fix 1: Configure strategy properly

```javascript
const LocalStrategy = require('passport-local').Strategy;

passport.use(new LocalStrategy({
  usernameField: 'email',
  passwordField: 'password',
}, async (email, password, done) => {
  try {
    const user = await User.findOne({ email });
    if (!user) return done(null, false, { message: 'User not found' });
    if (!await user.comparePassword(password)) {
      return done(null, false, { message: 'Invalid password' });
    }
    return done(null, user);
  } catch (err) {
    return done(err);
  }
}));
```

### Fix 2: Add authentication failure handler

```javascript
app.post('/login', passport.authenticate('local', {
  successRedirect: '/dashboard',
  failureRedirect: '/login',
  failureFlash: true,
}));
```

### Fix 3: Handle custom callback

```javascript
app.post('/login', (req, res, next) => {
  passport.authenticate('local', (err, user, info) => {
    if (err) return next(err);
    if (!user) return res.status(401).json({ error: info.message });
    req.logIn(user, (err) => {
      if (err) return next(err);
      return res.json({ success: true });
    });
  })(req, res, next);
});
```

### Fix 4: Implement proper serialization

```javascript
passport.serializeUser((user, done) => {
  done(null, user.id);
});

passport.deserializeUser(async (id, done) => {
  try {
    const user = await User.findById(id);
    done(null, user);
  } catch (err) {
    done(err);
  }
});
```

## Examples

```javascript
// This triggers auth failure
app.post('/login', passport.authenticate('local'), (req, res) => {
  res.json({ user: req.user });
});
// If credentials wrong, redirects to /login
```

## Related Errors

- [JWT Error]({{< relref "/languages/javascript/jsonwebtoken-error" >}}) — token invalid
- [Express Session]({{< relref "/languages/javascript/express-session" >}}) — session error
- [CORS Error]({{< relref "/languages/javascript/cors-error" >}}) — CORS policy
