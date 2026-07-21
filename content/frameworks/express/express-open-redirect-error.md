---
title: "[Solution] Express Open Redirect Error"
description: "Fix Express open redirect errors when user-controlled URLs redirect users to malicious external sites."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

An open redirect error in Express occurs when the `res.redirect()` function uses a user-supplied URL without validation, allowing attackers to redirect users to malicious websites.

## Common Causes

- `res.redirect()` uses `req.query.returnUrl` without validation
- Login flow redirects to an unvalidated URL parameter
- No allowlist of permitted redirect destinations
- Relative URL validation is bypassed with protocol-relative paths like `//evil.com`
- Logout or OAuth callback redirects based on user input

## How to Fix

1. Validate redirect URLs against an allowlist of trusted domains:

```javascript
function safeRedirect(req, res) {
  const returnUrl = req.query.returnUrl || '/dashboard';
  const parsed = new URL(returnUrl, `http://${req.headers.host}`);

  // Only allow relative paths
  if (parsed.origin !== `http://${req.headers.host}` &&
      parsed.origin !== `https://${req.headers.host}`) {
    return res.redirect('/dashboard');
  }

  res.redirect(parsed.pathname + parsed.search);
}

app.get('/logout', safeRedirect);
```

2. Use only relative paths and reject absolute URLs:

```javascript
app.get('/redirect', (req, res) => {
  const target = req.query.target;

  // Reject absolute URLs and protocol-relative paths
  if (target.startsWith('http') || target.startsWith('//')) {
    return res.redirect('/dashboard');
  }

  // Only allow paths starting with /
  if (!target.startsWith('/')) {
    return res.redirect('/dashboard');
  }

  res.redirect(target);
});
```

3. Encode and verify the redirect destination:

```javascript
app.get('/continue', (req, res) => {
  const next = req.query.next;

  try {
    const url = new URL(next, 'https://mysite.com');
    if (url.hostname !== 'mysite.com') {
      throw new Error('External URL');
    }
    res.redirect(url.pathname);
  } catch {
    res.redirect('/dashboard');
  }
});
```

## Examples

```javascript
// Vulnerable open redirect
app.get('/login', (req, res) => {
  res.render('login', { returnUrl: req.query.returnUrl });
});

app.post('/login', (req, res) => {
  authenticate(req.body);
  res.redirect(req.body.returnUrl || '/dashboard');
});

// Attack: /login?returnUrl=https://evil.com/steal
// After login, user is redirected to attacker's site
```

```text
GET /login?returnUrl=https://phishing-site.com/login
```
