---
title: "[Solution] Express Helmet CSP Error"
description: "Fix Express Helmet Content Security Policy errors when scripts or styles are blocked by the browser."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A Helmet CSP error in Express occurs when the Content Security Policy set by the `helmet` middleware blocks legitimate scripts, styles, images, or other resources loaded by the application.

## Common Causes

- Inline scripts blocked by default CSP policy
- External CDN resources not added to allowed sources
- `unsafe-eval` required for frameworks like React but not whitelisted
- Fonts or images from external domains blocked
- Nonce or hash not provided for inline styles

## How to Fix

1. Configure Helmet CSP with specific source allowlists:

```javascript
const helmet = require('helmet');

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "https://cdn.jsdelivr.net"],
      styleSrc: ["'self'", "'unsafe-inline'", "https://fonts.googleapis.com"],
      imgSrc: ["'self'", "data:", "https://images.example.com"],
      fontSrc: ["'self'", "https://fonts.gstatic.com"],
      connectSrc: ["'self'", "https://api.example.com"]
    }
  }
}));
```

2. Use nonces for inline scripts and styles:

```javascript
const crypto = require('crypto');

app.use((req, res, next) => {
  res.locals.nonce = crypto.randomBytes(16).toString('hex');
  next();
});

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      scriptSrc: ["'self'", (req, res) => `'nonce-${res.locals.nonce}'`],
      styleSrc: ["'self'", (req, res) => `'nonce-${res.locals.nonce}'`]
    }
  }
}));

app.get('/', (req, res) => {
  res.render('index', { nonce: res.locals.nonce });
});
```

3. Disable CSP for development:

```javascript
app.use(helmet({
  contentSecurityPolicy: process.env.NODE_ENV === 'production' ? undefined : false
}));
```

## Examples

```javascript
// Blocked: inline script without nonce
app.get('/', (req, res) => {
  res.send('<script>console.log("hello")</script>');
});

// CSP: script-src 'self' -- blocks inline scripts
// Fix: add nonce
app.use((req, res, next) => {
  res.locals.nonce = crypto.randomBytes(16).toString('hex');
  next();
});

app.get('/', (req, res) => {
  res.send(`<script nonce="${res.locals.nonce}">console.log("hello")</script>`);
});
```

```text
Refused to load the script 'https://cdn.example.com/lib.js' because it violates the following Content Security Policy directive: "script-src 'self'"
```
