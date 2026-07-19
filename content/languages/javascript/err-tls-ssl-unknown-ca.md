---
title: "[Solution] ERR_TLS_SSL_UNKNOWN_CA_ERROR — Unknown Certificate Authority Fix"
description: "Fix ERR_TLS_SSL_UNKNOWN_CA_ERROR when Node.js doesn't trust the server's CA. Add CA to trust store or use rejectUnauthorized."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_TLS_SSL_UNKNOWN_CA_ERROR

The server's certificate is signed by an unknown Certificate Authority.

## Fix

```javascript
// Add custom CA
const fs = require('fs');
const https = require('https');

const agent = new https.Agent({
  ca: fs.readFileSync('./custom-ca.pem'),
});
```

Or for development:

```javascript
process.env.NODE_EXTRA_CA_CERTS = '/path/to/ca.pem';
```
