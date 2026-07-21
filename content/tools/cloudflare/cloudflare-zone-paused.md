---
title: "[Solution] Cloudflare Zone Paused"
description: "Fix Cloudflare zone paused errors. Resolve issues when domain is paused in Cloudflare."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Zone Paused can prevent your application from working correctly.

## Common Causes

- Zone was manually paused in the dashboard
- Billing issues caused automatic pause
- Administrative action by account owner
- Zone exceeded plan limits

## How to Fix

### Unpause the Zone

1. Go to Overview
2. Scroll to Advanced Actions
3. Click Resume Cloudflare Services

### Check Billing

```bash
curl -X GET "https://api.cloudflare.com/client/v4/user/billing/profile" \
  -H "Authorization: Bearer {api_token}"
```

