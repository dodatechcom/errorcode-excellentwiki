---
title: "[Solution] Cloudflare 1023 Error — Could Not Find Host"
description: "Fix Cloudflare Error 1023 when the hostname is not found in the Cloudflare configuration. Verify domain setup, DNS records, and SSL/TLS coverage."
tools: ["cloudflare"]
error-types: ["dns-error"]
severities: ["error"]
weight: 5
---

Cloudflare Error 1023 occurs when Cloudflare cannot find the requested hostname in its configuration. The domain is either not on Cloudflare or is misconfigured.

## What This Error Means

Cloudflare receives a request for a hostname it does not recognize. This typically means the domain is not added to Cloudflare, or the DNS record does not have proxy enabled.

## Why It Happens

- The domain is not added to the Cloudflare account
- The DNS record for the hostname has proxy disabled (grey cloud)
- The domain was removed from Cloudflare but DNS still points to Cloudflare IPs
- The Cloudflare zone is paused or deleted
- The hostname is part of a multi-tenant setup but not configured as a custom hostname
- SSL/TLS coverage excludes the hostname

## How to Fix It

### Check the Domain in Cloudflare Dashboard

Go to Cloudflare dashboard and verify the domain is listed and active.

### Verify DNS Proxying

Ensure the DNS record has the proxy cloud (orange) enabled:

```
Type: A
Name: @
Content: <origin-ip>
Proxy status: Proxied (orange cloud)
```

### Check Zone Status

```bash
curl -X GET "https://api.cloudflare.com/client/v4/zones/<zone-id>" \
  -H "Authorization: Bearer <api-token>" | jq '.result.status'
```

### Add Domain Back If Removed

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones" \
  -H "Authorization: Bearer <api-token>" \
  -H "Content-Type: application/json" \
  --data '{"name": "your-domain.com", "account": {"id": "<account-id>"}}'
```

### Check for SSL/TLS Coverage

```bash
curl -X GET "https://api.cloudflare.com/client/v4/zones/<zone-id>/custom_hostnames" \
  -H "Authorization: Bearer <api-token>"
```

## Common Mistakes

- Removing a domain from Cloudflare but leaving DNS pointing to Cloudflare IPs
- Using grey cloud (DNS only) and expecting Cloudflare to route traffic
- Not checking zone status after a billing issue that paused the domain
- Forgetting to add new subdomains as custom hostnames in SSL for SaaS

## Related Pages

- [Cloudflare DNS Error]({{< relref "/tools/cloudflare/cloudflare-dns-error" >}}) -- DNS configuration
- [Cloudflare 1000 Error]({{< relref "/tools/cloudflare/cloudflare-1000" >}}) -- Prohibited IP
- [Cloudflare 1016 Error]({{< relref "/tools/cloudflare/cloudflare-1016" >}}) -- Origin DNS error
