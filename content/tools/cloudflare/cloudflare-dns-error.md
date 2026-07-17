---
title: "[Solution] Cloudflare DNS Resolution Failed Error — Fix DNS Configuration"
description: "Fix Cloudflare DNS resolution failed errors. Resolve DNS lookup failures, propagation issues, and record misconfigurations."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 10
---

A Cloudflare DNS resolution failed error occurs when visitors cannot resolve your domain name through Cloudflare's DNS servers. This means the DNS records configured in Cloudflare are either missing, incorrect, or have not propagated.

## What This Error Means

When a visitor tries to access your site, their browser sends a DNS query to resolve your domain. If Cloudflare cannot find the DNS record, the site appears unreachable. The error shows "DNS resolution failed" or the site simply does not load.

## Why It Happens

- DNS records are not configured in Cloudflare
- The nameservers have not been changed to Cloudflare at your registrar
- DNS records were accidentally deleted
- The domain has expired at the registrar
- DNS propagation is still in progress after recent changes
- The zone file is corrupted or has syntax errors
- The domain is not properly added to your Cloudflare account

## How to Fix It

### Verify Nameservers

```bash
# Check current nameservers
dig NS your-domain.com +short

# Expected result should show Cloudflare nameservers
# e.g., ns1.cloudflare.com and ns2.cloudflare.com

# Compare with what Cloudflare assigned
# Dashboard > Domain Overview > Nameservers
```

### Check DNS Records

```bash
# List all DNS records via API
curl -X GET "https://api.cloudflare.com/client/v4/zones/ZONE_ID/dns_records" \
  -H "Authorization: Bearer API_TOKEN" | jq '.result[] | {name, type, content}'

# Verify specific record exists
dig A your-domain.com +short
dig CNAME www.your-domain.com +short
```

### Update Nameservers at Registrar

```bash
# Login to your domain registrar
# Find the nameserver settings
# Replace current nameservers with Cloudflare's:
# - ns1.cloudflare.com
# - ns2.cloudflare.com

# Wait 24-48 hours for propagation
```

### Add Missing DNS Records

```bash
# Add A record via API
curl -X POST "https://api.cloudflare.com/client/v4/zones/ZONE_ID/dns_records" \
  -H "Authorization: Bearer API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "type": "A",
    "name": "your-domain.com",
    "content": "YOUR_SERVER_IP",
    "ttl": 1,
    "proxied": true
  }'
```

### Test DNS Resolution

```bash
# Test from different locations
dig @8.8.8.8 your-domain.com +short
dig @1.1.1.1 your-domain.com +short
dig @208.67.222.222 your-domain.com +short

# Check global propagation
# https://www.whatsmydns.net/#A/your-domain.com
```

### Purge DNS Cache

```bash
# Purge Cloudflare's DNS cache
# Dashboard > Caching > Configuration > Purge

# Flush local DNS cache
# macOS
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder

# Linux
sudo systemd-resolve --flush-caches

# Windows
ipconfig /flushdns
```

## Common Mistakes

- Forgetting to update nameservers at the registrar
- Not adding an A record for the root domain
- Using a CNAME for the root domain (use A record instead)
- Not waiting for DNS propagation before testing
- Mixing Cloudflare and registrar DNS records

## Related Pages

- [Cloudflare 530 Error]({{< relref "/tools/cloudflare/cloudflare-530" >}}) — Origin DNS Error
- [Cloudflare 1022 Error]({{< relref "/tools/cloudflare/cloudflare-1022" >}}) — Could not find host
