---
title: "[Solution] Netlify Certificate Provision Error"
description: "Fix Netlify certificate provision errors. Resolve initial certificate setup issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Certificate Provision Error can prevent your application from working correctly.

## Common Causes

- DNS not configured
- Domain not verified
- Certificate authority error
- Rate limit exceeded

## How to Fix

### Verify DNS

```bash
dig example.com A +short
dig example.com CNAME +short
```

### Check Domain Status

1. Go to Domain Settings
2. Verify domain is added

