---
title: "[Solution] Netlify SPF Record Error"
description: "Fix Netlify SPF record errors. Resolve Sender Policy Framework issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify SPF Record Error can prevent your application from working correctly.

## Common Causes

- SPF record missing
- Too many DNS lookups
- Netlify IP not included
- Record syntax error

## How to Fix

### Add SPF Record

```
example.com TXT "v=spf1 include:netlify.com ~all"
```

