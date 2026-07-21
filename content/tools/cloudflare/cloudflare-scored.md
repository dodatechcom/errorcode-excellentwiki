---
title: "[Solution] Cloudflare Scored Request Error"
description: "Fix Cloudflare scored request errors. Resolve threat scoring issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Scored Request Error can prevent your application from working correctly.

## Common Causes

- Request pattern matches known attacks
- IP address has poor reputation
- Bot detection assigns high score
- Legitimate traffic misidentified

## How to Fix

### Whitelist Trusted IPs

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/access_rules/rules" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"mode":"whitelist","configuration":{"target":"ip","value":"1.2.3.4"},"notes":"Trusted IP"}'
```

### Adjust Security Level

