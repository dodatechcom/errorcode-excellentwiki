---
title: "[Solution] Cloudflare Zero Trust Error"
description: "Fix Cloudflare Zero Trust errors. Resolve Access and Gateway issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Zero Trust Error can prevent your application from working correctly.

## Common Causes

- Access policy not configured
- Gateway rules blocking traffic
- WARP client not installed
- Team name incorrect

## How to Fix

### Install WARP

```bash
# macOS
brew install --cask cloudflare-warp
# Linux
curl -fsSL https://pkg.cloudflareclient.com/install.sh | sudo bash
```

### Check Status

```bash
warp-cli status
```

