---
title: "[Solution] Node.js TLS Certificate Verify Error — UNABLE_TO_VERIFY_LEAF_SIGNATURE Fix"
description: "Fix UNABLE_TO_VERIFY_LEAF_SIGNATURE when Node.js cannot verify the server's TLS certificate chain."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# TLS Certificate Verify Error

```javascript
const https = require('https');

// Option 1: Add CA certificate
const agent = new https.Agent({
  ca: fs.readFileSync('./ca-certificate.pem'),
});

// Option 2: Set NODE_EXTRA_CA_CERTS
// NODE_EXTRA_CA_CERTS=/path/to/ca.pem node app.js

// Option 3: Skip verification (DEVELOPMENT ONLY)
const agent = new https.Agent({ rejectUnauthorized: false });
```
