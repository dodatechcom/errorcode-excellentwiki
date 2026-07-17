---
title: "[Solution] Express SSL/TLS Error"
description: "Fix Express SSL/TLS errors. Resolve HTTPS and certificate issues."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["ssl", "tls", "https", "certificate", "express"]
weight: 5
---

An Express SSL/TLS error occurs when the application cannot establish a secure connection. This can be caused by missing certificates, incorrect configuration, or protocol issues.

## Common Causes

- SSL certificate files missing or misconfigured
- Private key does not match certificate
- Certificate is expired or self-signed
- HTTPS redirect not configured
- Mixed content (HTTP assets on HTTPS page)

## How to Fix

### Create HTTPS Server

```javascript
const https = require('https');
const fs = require('fs');

const options = {
  key: fs.readFileSync('private-key.pem'),
  cert: fs.readFileSync('certificate.pem'),
};

const server = https.createServer(options, app);
server.listen(443);
```

### Generate Self-Signed Certificate

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout private-key.pem -out certificate.pem
```

### Redirect HTTP to HTTPS

```javascript
app.use((req, res, next) => {
  if (req.headers['x-forwarded-proto'] !== 'https') {
    return res.redirect(301, `https://${req.hostname}${req.url}`);
  }
  next();
});
```

### Use Let's Encrypt

```bash
sudo certbot certonly --standalone -d example.com
```

## Examples

```javascript
// Example 1: Missing certificate
// Error: ENOENT: no such file or directory
// Fix: generate or download SSL certificate

// Example 2: Self-signed certificate warning
// Fix: use trusted CA certificate in production
```

## Related Errors

- [Express Proxy Error]({{< relref "/frameworks/express/express-proxy-error" >}}) — proxy error
- [Express Compression Error]({{< relref "/frameworks/express/express-compression-error" >}}) — compression error
