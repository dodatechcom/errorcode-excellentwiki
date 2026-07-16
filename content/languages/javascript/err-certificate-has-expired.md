---
title: "[Solution] Node.js ERR_CERT_HAS_EXPIRED — Certificate Expired Fix"
description: "Fix Node.js ERR_CERT_HAS_EXPIRED when SSL/TLS certificates have expired. Update certificates or adjust validation settings."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-cert-has-expired", "certificate", "ssl", "tls", "nodejs", "security"]
weight: 5
---

# Node.js ERR_CERT_HAS_EXPIRED — Certificate Expired Fix

The `ERR_CERT_HAS_EXPIRED` error occurs when Node.js encounters an SSL/TLS certificate that has passed its expiration date. This prevents secure connections to servers with outdated certificates.

## Description

Common ERR_CERT_HAS_EXPIRED messages include:

- `CERT_HAS_EXPIRED: certificate has expired` — the certificate's validity period has ended.
- `unable to verify the first certificate` — certificate chain cannot be validated.

## Common Causes

```javascript
const https = require("node:https");

// Cause 1: Server certificate has expired
https.get("https://expired.badssl.com/", (res) => {
  // ERR_CERT_HAS_EXPIRED
});

// Cause 2: Self-signed certificate with wrong date
const agent = new https.Agent({
  cert: fs.readFileSync("expired-cert.pem"),
  key: fs.readFileSync("expired-key.pem"),
});

// Cause 3: Intermediate certificate expired
// The chain includes an expired intermediate CA cert

// Cause 4: System clock is incorrect
// If the system date is past the cert expiry, validation fails
```

## Solutions

### Fix 1: Update the expired certificate

```bash
# Generate a new certificate using Let's Encrypt
certbot certonly --standalone -d example.com

# Or generate a self-signed cert for development
openssl req -x509 -newkey rsa:2048 -nodes \
  -keyout key.pem -out cert.pem -days 365 \
  -subj "/CN=localhost"
```

### Fix 2: Disable certificate validation (development only)

```javascript
const https = require("node:https");
const fs = require("node:fs");

// WARNING: Only use in development, never in production
const agent = new https.Agent({
  rejectUnauthorized: false,
});

https.get("https://localhost:3000", { agent }, (res) => {
  let data = "";
  res.on("data", (chunk) => (data += chunk));
  res.on("end", () => console.log(data));
});
```

### Fix 3: Add custom CA certificate to trust store

```javascript
const https = require("node:https");
const fs = require("node:fs");

// Add your custom CA to the trusted certificates
const ca = fs.readFileSync("path/to/custom-ca.pem");

const agent = new https.Agent({
  ca: ca,
  rejectUnauthorized: true,
});

https.get("https://internal.example.com", { agent }, (res) => {
  // Connection succeeds with custom CA
});
```

### Fix 4: Use NODE_EXTRA_CA_CERTS environment variable

```bash
# Add custom CA certificates to Node.js trust store
export NODE_EXTRA_CA_CERTS="/path/to/custom-ca.pem"
node app.js
```

## Examples

```javascript
const https = require("node:https");

// ERR_CERT_HAS_EXPIRED when connecting to expired server
const options = {
  hostname: "expired.badssl.com",
  port: 443,
  path: "/",
  method: "GET",
};

const req = https.request(options, (res) => {
  console.log("Status:", res.statusCode);
});

req.on("error", (err) => {
  if (err.code === "ERR_CERT_HAS_EXPIRED") {
    console.error("Certificate has expired:", err.message);
    // Handle expired certificate error
  }
});

req.end();
```

## Related Errors

- [ERR_CONNECTION_REFUSED]({{< relref "/languages/javascript/err-connection-refused" >}}) — server refused connection.
- [ERR_CONNECTION_RESET]({{< relref "/languages/javascript/err-connection-reset" >}}) — connection was reset.
- [ERR_DNS_RESOLUTION_FAILED]({{< relref "/languages/javascript/err-dns-resolution-failed" >}}) — DNS lookup failed.
- [ERR_SOCKET_TIMEOUT]({{< relref "/languages/javascript/ERR_SOCKET_TIMEOUT" >}}) — socket timed out.
