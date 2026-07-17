---
title: "[Solution] Cloudflare 530 Origin DNS Error — Fix DNS Resolution on Origin"
description: "Fix Cloudflare 530 origin DNS error. Resolve DNS resolution failures between Cloudflare and your origin server."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 6
---

A Cloudflare 530 error means Cloudflare cannot resolve the DNS for your origin server. This error occurs when Cloudflare tries to connect to your origin but the hostname in your DNS configuration does not resolve to a valid IP address.

## What This Error Means

The 530 error is typically a companion to other errors like 502 or 522. It indicates that the origin server's hostname cannot be resolved by Cloudflare's DNS resolver. The error page shows "Error 1016: Origin DNS error" in the Ray ID details.

## Why It Happens

- The origin server hostname has no DNS record
- The origin DNS record points to a non-existent IP
- The A or CNAME record for the origin was recently changed and has not propagated
- The origin hostname's DNS has expired
- The origin server was migrated and DNS was not updated
- Cloudflare's cached DNS record is stale

## How to Fix It

### Verify Origin DNS

```bash
# Check if origin hostname resolves
dig origin.your-domain.com +short

# Check from multiple DNS servers
dig @8.8.8.8 origin.your-domain.com +short
dig @1.1.1.1 origin.your-domain.com +short

# Check if the IP exists
ping origin.your-domain.com
```

### Update Origin DNS Record

```bash
# If using a hosting provider, update the A record
# Point origin.your-domain.com to your server IP

# Verify the record
host origin.your-domain.com
```

### Check Cloudflare DNS Settings

```bash
# In Cloudflare Dashboard:
# 1. Go to DNS > Records
# 2. Find the A record or CNAME for your origin
# 3. Verify the target is correct
# 4. Make sure the record is NOT proxied (grey cloud)
```

### Test Origin Connectivity

```bash
# Test direct IP connection
curl -H "Host: your-domain.com" http://ORIGIN_IP

# Test with hostname
curl http://origin.your-domain.com
```

### Fix Stale DNS Cache

```bash
# Purge Cloudflare DNS cache
# Dashboard: Caching > Configuration > Purge

# Or use the API
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/ZONE_ID/purge_cache" \
  -H "Authorization: Bearer API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"purge_everything":true}'
```

## Common Mistakes

- Not updating origin DNS after server migration
- Using a hostname that does not exist in public DNS
- Leaving the origin DNS record unproxied but pointing to wrong IP
- Not waiting for DNS propagation after changes
- Confusing Cloudflare DNS with origin server DNS

## Related Pages

- [Cloudflare 502 Error]({{< relref "/tools/cloudflare/cloudflare-502" >}}) — Bad Gateway
- [Cloudflare DNS Error]({{< relref "/tools/cloudflare/cloudflare-dns-error" >}}) — DNS resolution failed
