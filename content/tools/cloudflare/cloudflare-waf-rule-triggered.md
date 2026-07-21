---
title: "[Solution] Cloudflare WAF Rule Triggered"
description: "Fix Cloudflare WAF rule triggered errors. Resolve false positives from WAF rules."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare WAF Rule Triggered can prevent your application from working correctly.

## Common Causes

- Rule too aggressive for your application
- Legitimate requests match attack signatures
- Custom rule needs tuning
- OWASP rule triggered by form submission

## How to Fix

### Identify Rule

Check response headers for cf-ray and firewall info.

### Create Exception

1. Go to Security > WAF
2. Find the triggered rule
3. Add exception for your IP or path

### Disable Rule

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules/{rule_id}" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"paused":true}'
```

