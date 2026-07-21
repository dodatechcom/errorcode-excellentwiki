---
title: "[Solution] Cloudflare Gateway DNS Error"
description: "Fix Cloudflare Gateway DNS errors. Resolve DNS filtering issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Gateway DNS Error can prevent your application from working correctly.

## Common Causes

- DNS policy blocking legitimate domains
- Split tunnel not configured
- DNS resolver not reachable
- Policy categories too broad

## How to Fix

### Configure DNS Policy

1. Go to Zero Trust > Gateway > DNS policies
2. Create policy for allowed domains

### Check DNS

```bash
dig example.com @1.1.1.1
```

