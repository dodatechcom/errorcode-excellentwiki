---
title: "[Solution] Netlify DMARC Policy Error"
description: "Fix Netlify DMARC policy errors. Resolve email authentication issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify DMARC Policy Error can prevent your application from working correctly.

## Common Causes

- DMARC record missing
- Policy too strict
- Report email invalid
- Record syntax error

## How to Fix

### Add DMARC Record

```
_dmarc.example.com TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@example.com"
```

