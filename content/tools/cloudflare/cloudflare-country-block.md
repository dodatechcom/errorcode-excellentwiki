---
title: "[Solution] Cloudflare Country Block Error"
description: "Fix Cloudflare country block errors. Resolve geo-based traffic blocking issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Country Block Error can prevent your application from working correctly.

## Common Causes

- Block list includes unintended countries
- VPN traffic appears from blocked country
- Legitimate international users blocked
- IP geolocation inaccuracy

## How to Fix

### Configure

1. Go to Security > WAF > Tools
2. Add countries to Block list

### Firewall Rule

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '[{"filter":{"expression":"ip.geoip.country in {\"XX\"}"},"action":"block"}]'
```

