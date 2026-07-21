---
title: "[Solution] Cloudflare Tunnel DNS Error"
description: "Fix Cloudflare tunnel DNS errors. Resolve DNS routing issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Tunnel DNS Error can prevent your application from working correctly.

## Common Causes

- DNS route not created
- Domain not configured
- DNS propagation delay
- Route conflicts with existing records

## How to Fix

### Route DNS

```bash
cloudflared tunnel route dns my-tunnel *.example.com
```

### Check DNS

```bash
dig *.example.com CNAME +short
```

