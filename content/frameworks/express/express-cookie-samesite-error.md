---
title: "[Solution] Express Cookie SameSite Error"
description: "Fix Express cookie SameSite attribute errors when cross-origin requests fail due to cookie restrictions."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A cookie SameSite error in Express occurs when cookies are not set with the correct `SameSite` attribute, causing browsers to block or reject cookies in cross-origin contexts.

## Common Causes

- `SameSite` attribute not set on cookies (defaults to `Lax` in modern browsers)
- `SameSite=None` used without `Secure` flag (rejected by browsers)
- Cross-origin API requests cannot send session cookies
- OAuth callbacks fail because auth cookies are not set
- Development environment uses HTTP but `Secure` flag requires HTTPS

## How to Fix

1. Configure cookies with appropriate SameSite attributes:

```javascript
app.use(session({
  secret: 'mysecret',
  cookie: {
    sameSite: process.env.NODE_ENV === 'production' ? 'none' : 'lax',
    secure: process.env.NODE_ENV === 'production',
    httpOnly: true,
    maxAge: 24 * 60 * 60 * 1000
  }
}));
```

2. Set SameSite per cookie:

```javascript
// Cross-origin cookies (requires HTTPS)
res.cookie('token', jwt, {
  sameSite: 'none',
  secure: true,
  httpOnly: true,
  maxAge: 3600000
});

// Same-origin cookies
res.cookie('preferences', prefs, {
  sameSite: 'lax',
  httpOnly: true
});
```

3. Handle development environment with secure false:

```javascript
const isProd = process.env.NODE_ENV === 'production';

app.use(session({
  secret: process.env.SESSION_SECRET,
  cookie: {
    sameSite: isProd ? 'none' : 'lax',
    secure: isProd,
    httpOnly: true,
    domain: isProd ? '.example.com' : undefined
  }
}));
```

## Examples

```javascript
// Bug: SameSite=none without Secure in development
res.cookie('session', id, {
  sameSite: 'none',
  secure: true, // Fails on localhost HTTP
});

// Fixed: environment-aware configuration
const cookieOptions = {
  sameSite: process.env.NODE_ENV === 'production' ? 'none' : 'lax',
  secure: process.env.NODE_ENV === 'production',
  httpOnly: true
};
res.cookie('session', id, cookieOptions);
```

```text
Cookie 'session' was rejected because its SameSite attribute is "none" without the "secure" flag
```
