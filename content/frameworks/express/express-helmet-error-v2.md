---
title: "Helmet Security Header Error in Express"
description: "Fix Express Helmet errors when security headers conflict with application requirements or block legitimate resources."
frameworks: ["express.js"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

`helmet` sets various HTTP security headers. Misconfiguration can block your own resources, break frontend functionality, or cause Content Security Policy (CSP) violations. These errors manifest as blocked scripts, images, or styles in the browser console — not as server-side errors.

## Common Causes

- Content Security Policy (CSP) blocks inline scripts or external resources
- `X-Frame-Options` prevents embedding in iframes your app uses
- `Strict-Transport-Security` forces HTTPS before it's properly configured
- Mixed content warnings when CSP blocks HTTP resources on HTTPS
- Third-party scripts (analytics, fonts) not whitelisted in CSP

## How to Fix

### Configure Helmet with Proper CSP

```javascript
const helmet = require('helmet');

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "'unsafe-inline'", "https://cdn.example.com"],
      styleSrc: ["'self'", "'unsafe-inline'", "https://fonts.googleapis.com"],
      imgSrc: ["'self'", "data:", "https:"],
      fontSrc: ["'self'", "https://fonts.gstatic.com"]
    }
  }
}));
```

### Allow Specific Origins and Frames

```javascript
app.use(helmet({
  crossOriginEmbedderPolicy: false,
  crossOriginResourcePolicy: { policy: "cross-origin" },
  frameguard: { action: 'sameorigin' }
}));
```

### Disable Specific Headers in Development

```javascript
if (process.env.NODE_ENV === 'development') {
  app.use(helmet({
    contentSecurityPolicy: false,
    crossOriginEmbedderPolicy: false
  }));
} else {
  app.use(helmet());
}
```

### Handle CSP Violation Reports

```javascript
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      reportUri: '/csp-report'
    }
  }
}));

app.post('/csp-report', express.json({ type: 'application/csp-report' }), (req, res) => {
  console.error('CSP Violation:', req.body);
  res.sendStatus(204);
});
```

### Debug Blocked Resources

```javascript
// Temporary: log all CSP violations to identify needed changes
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      reportOnly: true // Log violations without blocking
    },
    reportUri: '/csp-report'
  }
}));
```

## Related Errors

- [Express CORS Error]({{< relref "/frameworks/express/express-cors-error-v2" >}}) — cross-origin policy conflicts
- [Express SSL Error]({{< relref "/frameworks/express/express-ssl-error-v2" >}}) — HTTPS certificate issues
