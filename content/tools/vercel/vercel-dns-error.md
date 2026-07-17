---
title: "[Solution] Vercel DNS Verification Failed Error — Fix Domain DNS"
description: "Fix Vercel DNS verification failed errors. Resolve domain verification issues and DNS record configuration problems."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
weight: 9
---

A Vercel DNS verification failed error occurs when Vercel cannot verify that your domain's DNS records point to the correct destination. Vercel periodically checks DNS to ensure domains remain properly configured.

## What This Error Means

Vercel verifies domain configuration by checking DNS records. When the records do not match what Vercel expects, the domain is marked as "Verification Failed" and your site may become unreachable on that domain.

## Why It Happens

- The A record or CNAME does not point to Vercel's servers
- DNS records were changed at the registrar
- Another service (like Cloudflare) is overriding DNS
- The DNS provider changed nameservers
- DNS records expired
- You switched DNS providers without updating Vercel

## How to Fix It

### Check Current DNS

```bash
# Verify your DNS records
dig your-domain.com A +short
dig your-domain.com CNAME +short
dig www.your-domain.com CNAME +short

# Expected values:
# A: 76.76.21.21
# CNAME: cname.vercel-dns.com
```

### Fix DNS at Registrar

```bash
# For apex domain (your-domain.com)
# Type: A
# Name: @
# Value: 76.76.21.21
# TTL: Auto

# For subdomain (www.your-domain.com)
# Type: CNAME
# Name: www
# Value: cname.vercel-dns.com
# TTL: Auto
```

### Check if Cloudflare is Interfering

```bash
# If using Cloudflare, ensure:
# 1. Proxy is OFF (grey cloud, not orange)
# 2. DNS record points to Vercel's IP/CNAME
# 3. SSL mode is set appropriately

# Verify with:
dig your-domain.com +trace
```

### Re-add Domain in Vercel

```bash
# Remove and re-add the domain
vercel domains rm your-domain.com
vercel domains add your-domain.com
```

### Check DNS Propagation

```bash
# Test from multiple DNS servers
dig @8.8.8.8 your-domain.com +short
dig @1.1.1.1 your-domain.com +short
dig @208.67.222.222 your-domain.com +short

# Full propagation check
# https://www.whatsmydns.net/#A/your-domain.com
```

### Fix Conflicting Records

```bash
# Remove any old DNS records that point elsewhere
# Delete stale A or CNAME records at your registrar

# After cleaning up, wait for propagation
# Then verify in Vercel Dashboard
```

### Use Vercel DNS as Alternative

```bash
# If third-party DNS keeps causing issues,
# switch to Vercel's DNS

# 1. Enable Vercel DNS in Dashboard
# 2. Update nameservers at registrar:
#    ns1.vercel-dns.com
#    ns2.vercel-dns.com
# 3. Wait for propagation (24-48 hours)
```

## Common Mistakes

- Having multiple A records for the same domain
- Not disabling Cloudflare proxy when pointing to Vercel
- Changing DNS without waiting for verification
- Not checking all nameservers during propagation
- Forgetting that DNS changes can take up to 48 hours

## Related Pages

- [Vercel Domain Error]({{< relref "/tools/vercel/vercel-domain-error" >}}) — Domain configuration failed
- [Vercel Project Error]({{< relref "/tools/vercel/vercel-project-error" >}}) — Project not found
