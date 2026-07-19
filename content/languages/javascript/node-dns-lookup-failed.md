---
title: "[Solution] Node.js DNS Lookup Failed — getaddrinfo ENOTFOUND Fix"
description: "Fix getaddrinfo ENOTFOUND errors when DNS lookup fails in Node.js. Check DNS configuration and hostname."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# DNS Lookup Failed

```javascript
const dns = require('dns');

dns.lookup('nonexistent.example.com', (err, address) => {
  if (err) {
    // getaddrinfo ENOTFOUND nonexistent.example.com
    console.error('DNS lookup failed:', err.code);
  }
});
```

## Fix

```bash
# Check DNS
dig nonexistent.example.com

# Try different DNS server
dig @8.8.8.8 nonexistent.example.com
```
