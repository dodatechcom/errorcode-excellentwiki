---
title: "[Solution] Express Host Header Error"
description: "Fix Express host header errors when the request Host header is spoofed or missing, causing incorrect URL generation."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A host header error in Express occurs when the application relies on the `Host` request header for URL generation, redirects, or origin validation, and the header is missing, malformed, or spoofed by an attacker.

## Common Causes

- `req.hostname` returns unexpected value due to proxy misconfiguration
- `Host` header contains port numbers or IP addresses instead of domain
- Missing `trust proxy` setting when behind a load balancer
- URL generation in templates uses spoofed host header
- Origin validation relies on vulnerable host header checks

## How to Fix

1. Configure `trust proxy` when behind a reverse proxy:

```javascript
app.set('trust proxy', 1); // Trust first proxy
app.set('trust proxy', 'loopback'); // Trust loopback interfaces
app.set('trust proxy', ['10.0.0.0/8', '172.16.0.0/12']); // Trust specific subnets
```

2. Use an explicit allowlist of valid hostnames:

```javascript
const allowedHosts = ['example.com', 'www.example.com', 'api.example.com'];

app.use((req, res, next) => {
  const host = req.hostname;
  if (!allowedHosts.includes(host)) {
    return res.status(421).json({ error: 'Invalid host header' });
  }
  next();
});
```

3. Generate URLs from configuration instead of request headers:

```javascript
const BASE_URL = process.env.BASE_URL || 'https://example.com';

app.get('/email/verify', (req, res) => {
  const token = generateToken();
  const link = `${BASE_URL}/verify?token=${token}`;
  sendVerificationEmail(req.body.email, link);
});
```

## Examples

```javascript
// Vulnerable: uses Host header for URL generation
app.get('/reset-password', (req, res) => {
  const token = generateResetToken();
  const link = `https://${req.headers.host}/reset?token=${token}`;
  // Attacker sends Host: evil.com
  // Link becomes: https://evil.com/reset?token=abc123
});

// Safe: uses configured base URL
app.get('/reset-password', (req, res) => {
  const token = generateResetToken();
  const link = `${process.env.BASE_URL}/reset?token=${token}`;
});
```

```text
Error: getaddrinfo ENOTFOUND evil.com
```
