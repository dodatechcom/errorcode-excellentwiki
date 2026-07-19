---
title: "[Solution] ERR_TLS_HANDSHAKE_TIMEOUT — TLS Negotiation Timeout Fix"
description: "Fix ERR_TLS_HANDSHAKE_TIMEOUT when TLS negotiation takes too long. Increase timeout and check network."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_TLS_HANDSHAKE_TIMEOUT

TLS handshake did not complete in time.

## Fix

```javascript
const https = require('https');
const agent = new https.Agent({
  timeout: 30000,
  handshakeTimeout: 30000
});
```

## Network Check

```bash
openssl s_client -connect host:443 -servername host
```
