---
title: "[Solution] EAI_AGAIN — DNS Lookup Temporarily Failed"
description: "Fix EAI_AGAIN DNS resolution errors. Retry DNS lookups, check DNS servers, and handle transient failures."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# EAI_AGAIN — DNS Temporary Failure

DNS lookup failed temporarily. This is usually transient.

## Fix

```javascript
// Retry DNS-dependent operations
async function withRetry(fn, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      return await fn();
    } catch (err) {
      if (i === retries - 1 || err.code !== 'EAI_AGAIN') throw err;
      await new Promise(r => setTimeout(r, 1000 * (i + 1)));
    }
  }
}
```

```bash
# Check DNS configuration
cat /etc/resolv.conf
```
