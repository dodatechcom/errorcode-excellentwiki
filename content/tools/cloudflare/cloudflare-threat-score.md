---
title: "[Solution] Cloudflare Threat Score Error"
description: "Fix Cloudflare threat score errors. Resolve IP reputation scoring issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Threat Score Error can prevent your application from working correctly.

## Common Causes

- IP associated with malicious activity
- Shared IP from cloud provider flagged
- VPN exit nodes have high scores
- Score threshold set too low

## How to Fix

### Whitelist IPs

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/access_rules/rules" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"mode":"whitelist","configuration":{"target":"ip","value":"1.2.3.4"},"notes":"Trusted cloud IP"}'
```

### Adjust Challenge Threshold

