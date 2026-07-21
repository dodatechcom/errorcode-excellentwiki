---
title: "[Solution] Vercel DNS Propagation Error"
description: "Fix Vercel DNS propagation errors. Resolve DNS update delay issues."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

Vercel DNS Propagation Error can prevent your application from working correctly.

## Common Causes

- DNS not propagated
- ISP caching old records
- TTL too high
- Nameserver not updated

## How to Fix

### Check Propagation

```bash
dig @1.1.1.1 your-domain.com +short
dig @8.8.8.8 your-domain.com +short
```

### Wait

Standard propagation: 24-48 hours.

