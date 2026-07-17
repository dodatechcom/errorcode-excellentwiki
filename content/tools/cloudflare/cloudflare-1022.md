---
title: "[Solution] Cloudflare 1022 Could Not Find Host Error — Fix Origin Configuration"
description: "Fix Cloudflare 1022 host not found errors. Resolve origin server hostname resolution and proxy configuration issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 9
---

A Cloudflare 1022 error means Cloudflare could not find the origin host specified in your DNS configuration. This error occurs when the hostname you have configured as the origin target does not exist or cannot be resolved.

## What This Error Means

The 1022 error is closely related to DNS resolution failures. Cloudflare tries to connect to the origin hostname specified in your DNS records, but it cannot resolve that hostname. The error page displays "Could not find host" with a Ray ID for debugging.

## Why It Happens

- The origin hostname in your DNS record does not exist
- The CNAME target has been deleted or changed
- The origin hostname has a DNS record but it points to nothing
- You entered the wrong hostname when configuring DNS
- The origin hostname's DNS expired
- Third-party DNS hosting is down or unreachable

## How to Fix It

### Check DNS Configuration

```bash
# In Cloudflare Dashboard:
# DNS > Records
# Find the CNAME or A record for your domain

# Verify the target hostname exists
dig origin.your-domain.com +short

# Check CNAME chain
dig origin.your-domain.com CNAME +short
```

### Verify Origin Hostname

```bash
# Check if the hostname resolves
nslookup origin-host.example.com

# Check with multiple DNS servers
dig @8.8.8.8 origin-host.example.com
dig @1.1.1.1 origin-host.example.com
```

### Fix CNAME Records

```bash
# If using CNAME to a hosting provider
# Make sure the target hostname is active

# Example: pointing to a cloud provider
# CNAME your-domain.com -> app.example-provider.com

# Verify the target is live
curl -I https://app.example-provider.com
```

### Update DNS Records

```bash
# If the origin IP changed, update the A record

# Via Cloudflare API
curl -X PUT \
  "https://api.cloudflare.com/client/v4/zones/ZONE_ID/dns_records/RECORD_ID" \
  -H "Authorization: Bearer API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "type": "A",
    "name": "@",
    "content": "NEW_ORIGIN_IP",
    "ttl": 1
  }'
```

### Check for DNS Propagation

```bash
# After making changes, check propagation
dig your-domain.com +short
dig @8.8.8.8 your-domain.com +short
dig @1.1.1.1 your-domain.com +short

# Check DNS propagation status
# https://www.whatsmydns.net/
```

## Common Mistakes

- Typo in the origin hostname DNS record
- Not updating DNS after migrating to a new server
- Using a CNAME target that has been decommissioned
- Not checking that the origin hostname actually resolves
- Assuming Cloudflare will fix DNS issues automatically

## Related Pages

- [Cloudflare DNS Error]({{< relref "/tools/cloudflare/cloudflare-dns-error" >}}) — DNS resolution failed
- [Cloudflare 530 Error]({{< relref "/tools/cloudflare/cloudflare-530" >}}) — Origin DNS Error
