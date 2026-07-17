---
title: "HTTPS/SSL Certificate Error in Express"
description: "Fix Express HTTPS errors when SSL certificates are invalid, expired, or misconfigured for secure connections."
frameworks: ["express.js"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

When Express serves over HTTPS, certificate errors occur if the SSL/TLS certificate is expired, self-signed, uses an invalid domain name, or has missing intermediate certificates. In development, self-signed certificates trigger browser warnings. In production, expired certificates cause complete service outages.

## Common Causes

- SSL certificate has expired
- Certificate domain does not match the server hostname
- Self-signed certificate not trusted by clients
- Missing intermediate certificates in the certificate chain
- Private key does not match the certificate

## How to Fix

### Set Up HTTPS in Express

```javascript
const https = require('https');
const fs = require('fs');

const options = {
  key: fs.readFileSync('./certs/private-key.pem'),
  cert: fs.readFileSync('./certs/certificate.pem')
};

const app = express();

https.createServer(options, app).listen(443, () => {
  console.log('HTTPS server running on port 443');
});
```

### Handle Certificate Errors in Development

```javascript
// For development with self-signed certificates
const options = {
  key: fs.readFileSync('./certs/dev-key.pem'),
  cert: fs.readFileSync('./certs/dev-cert.pem'),
  rejectUnauthorized: false // Don't use in production
};

https.createServer(options, app).listen(3443);
```

### Auto-Renew Certificates with Let's Encrypt

```javascript
const https = require('https');
constLetsEncrypt = require('letsencrypt-express');

const lex = LetsEncrypt.create({
  configDir: '/etc/letsencrypt',
  letsencrypt: {
    email: 'admin@example.com',
    agreedToTermsOfService: true
  }
});

lex.onRequest = app;

lex.listen(80, 443, () => {
  console.log('Server running on 80 and 443 with auto-renewal');
});
```

### Verify Certificate Chain

```bash
# Check certificate expiration
openssl x509 -in certificate.pem -noout -dates

# Verify certificate chain
openssl verify -CAfile chain.pem certificate.pem

# Check private key matches certificate
openssl x509 -noout -modulus -in certificate.pem | md5sum
openssl rsa -noout -modulus -in private-key.pem | md5sum
```

### Redirect HTTP to HTTPS

```javascript
app.use((req, res, next) => {
  if (req.headers['x-forwarded-proto'] !== 'https' && process.env.NODE_ENV === 'production') {
    return res.redirect(301, `https://${req.headers.host}${req.url}`);
  }
  next();
});
```

## Related Errors

- [Express Compression Error]({{< relref "/frameworks/express/express-compression-error-v2" >}}) — encoding issues
- [Express CORS Error]({{< relref "/frameworks/express/express-cors-error-v2" >}}) — cross-origin HTTPS issues
