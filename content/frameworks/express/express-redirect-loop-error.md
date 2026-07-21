---
title: "[Solution] Express Redirect Loop Error"
description: "Fix Express redirect loop errors when the server continuously redirects the client between two or more URLs."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A redirect loop error in Express occurs when a route redirects to another route that redirects back, creating an infinite loop. The browser eventually displays a "too many redirects" error.

## Common Causes

- Two routes redirect to each other based on authentication state
- Middleware redirects unauthenticated users to a login page that itself requires auth
- Redirect condition always evaluates to true
- Trailing slash normalization creates a redirect chain
- Cookie or session not persisted, causing repeated auth failures

## How to Fix

1. Add a redirect counter to detect loops:

```javascript
app.use((req, res, next) => {
  req.redirectCount = parseInt(req.headers['x-redirect-count'] || '0', 10);
  if (req.redirectCount > 5) {
    return res.status(508).json({ error: 'Redirect loop detected' });
  }
  next();
});

app.get('/dashboard', (req, res, next) => {
  if (!req.session.user) {
    res.setHeader('X-Redirect-Count', (req.redirectCount + 1).toString());
    return res.redirect('/login');
  }
  res.render('dashboard');
});
```

2. Use absolute paths and verify redirect targets:

```javascript
app.get('/admin', (req, res) => {
  if (!req.session.isAdmin) {
    return res.redirect('/login?reason=admin_required');
  }
  res.render('admin');
});

app.get('/login', (req, res) => {
  if (req.session.user) {
    return res.redirect('/dashboard'); // Not back to /admin
  }
  res.render('login');
});
```

3. Implement a redirect chain tracker in middleware:

```javascript
function trackRedirects(req, res, next) {
  const chain = req.session?.redirectChain || [];
  const current = req.originalUrl;

  if (chain.includes(current)) {
    delete req.session.redirectChain;
    return res.status(508).json({ error: 'Redirect loop detected' });
  }

  chain.push(current);
  if (!req.session) req.session = {};
  req.session.redirectChain = chain;

  const originalRedirect = res.redirect.bind(res);
  res.redirect = (url) => {
    req.session.redirectChain = chain;
    originalRedirect(url);
  };

  next();
}

app.use(trackRedirects);
```

## Examples

```javascript
// Bug: /login redirects to /admin which redirects to /login
app.get('/admin', (req, res) => {
  if (!req.user) return res.redirect('/login');
  res.render('admin');
});

app.get('/login', (req, res) => {
  if (req.user) return res.redirect('/admin');
  res.render('login');
});
// If session is not saved, req.user is always null on /login
```

```text
ERR_TOO_MANY_REDIRECTS
```
