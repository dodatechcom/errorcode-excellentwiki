---
title: "[Solution] Cloudflare DNS Record Not Found"
description: "Fix Cloudflare DNS record not found errors. Resolve missing DNS records in Cloudflare."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare DNS Record Not Found can prevent your application from working correctly.

## Common Causes

- DNS record was deleted or never created
- Record is proxied but origin server is not configured
- DNSSEC interfering with record resolution
- Record type does not match expected service

## How to Fix

### Verify DNS Record

```bash
dig your-domain.com A +short
dig your-domain.com CNAME +short
```

### Check Cloudflare DNS Settings

1. Log in to Cloudflare dashboard
2. Select your domain
3. Go to DNS > Records
4. Verify the record exists and is correct

### Create Missing Record

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"type":"A","name":"@","content":"192.0.2.1","ttl":1,"proxied":true}'
```

