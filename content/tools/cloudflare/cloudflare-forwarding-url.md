---
title: "[Solution] Cloudflare Forwarding URL Error"
description: "Fix Cloudflare forwarding URL errors. Resolve 301/302 redirect issues in page rules."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Forwarding URL Error can prevent your application from working correctly.

## Common Causes

- Redirect creates a loop
- Target URL is invalid
- Forwarding URL conflicts with other rules
- Status code is incorrect

## How to Fix

### Create Forwarding Rule

1. Go to Rules > Page Rules
2. Click Create Page Rule
3. Enter URL pattern
4. Select Forwarding URL
5. Choose 301 or 302
6. Enter destination URL

### Check for Loops

```bash
curl -v http://your-domain.com 2>&1 | grep -E "< HTTP|Location:"
```

