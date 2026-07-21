---
title: "[Solution] Cloudflare Access Policy Error"
description: "Fix Cloudflare Access policy errors. Resolve Zero Trust access policy issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Access Policy Error can prevent your application from working correctly.

## Common Causes

- Policy not assigned to application
- Identity provider not configured
- Policy rules too broad
- Exclude rules too restrictive

## How to Fix

### Create Policy

1. Go to Zero Trust > Access > Policies
2. Click Add a policy
3. Configure rules

### Check

```bash
curl -X GET "https://api.cloudflare.com/client/v4/accounts/{account_id}/access/policies" \
  -H "Authorization: Bearer {api_token}" | jq '.result'
```

