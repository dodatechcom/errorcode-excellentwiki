---
title: "[Solution] Vercel Domain Configuration Error — Fix Custom Domain Setup"
description: "Fix Vercel domain configuration errors. Resolve custom domain setup failures, DNS verification, and SSL issues."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
weight: 4
---

A Vercel domain configuration error occurs when a custom domain cannot be properly configured, verified, or connected to your Vercel project. DNS misconfiguration or SSL issues are the most common causes.

## What This Error Means

Vercel requires specific DNS records to connect your domain to your project. When these records are missing, incorrect, or have not propagated, the domain shows as "Invalid Configuration" or "Verification Failed" in the dashboard.

## Why It Happens

- DNS records are not configured at your registrar
- The nameserver change has not propagated
- The A record points to the wrong IP address
- CNAME record is misconfigured
- SSL certificate has not been issued yet
- The domain is already connected to another project
- DNS propagation is still in progress

## How to Fix It

### Configure DNS Records

```bash
# Option 1: CNAME record (recommended for subdomains)
# Name: www
# Type: CNAME
# Value: cname.vercel-dns.com
# TTL: Auto

# Option 2: A record (for apex domain)
# Name: @
# Type: A
# Value: 76.76.21.21
# TTL: Auto
```

### Add Domain via CLI

```bash
# Add domain to project
vercel domains add your-domain.com

# Add to specific project
vercel domains add your-domain.com --scope your-team
```

### Verify DNS Configuration

```bash
# Check DNS records
dig your-domain.com +short
dig www.your-domain.com +short

# Should return:
# A record: 76.76.21.21
# CNAME: cname.vercel-dns.com
```

### Check Domain Status

```bash
# List domains for project
vercel domains ls

# Check specific domain
curl -X GET "https://api.vercel.com/v6/domains/your-domain.com" \
  -H "Authorization: Bearer YOUR_TOKEN" | jq .
```

### Fix SSL Certificate Issues

```bash
# SSL is auto-provisioned by Vercel
# If not working, try removing and re-adding the domain

# Remove domain
vercel domains rm your-domain.com

# Re-add domain
vercel domains add your-domain.com
```

### Use Vercel Nameservers (Alternative)

```bash
# If DNS verification is stuck, you can use Vercel's nameservers
# 1. Go to Project Settings > Domains
# 2. Click "Use Vercel DNS"
# 3. Update nameservers at your registrar:
#    ns1.vercel-dns.com
#    ns2.vercel-dns.com
```

### Transfer Subdomains

```bash
# Add subdomain to Vercel
vercel domains add api.your-domain.com

# DNS record needed
# Type: CNAME
# Name: api
# Value: cname.vercel-dns.com
```

## Common Mistakes

- Using an IP address for CNAME records (must be hostname)
- Forgetting to update nameservers after adding domain
- Not waiting 24-48 hours for DNS propagation
- Adding both A and CNAME records for the same hostname
- Not checking that the domain is not already in use elsewhere

## Related Pages

- [Vercel DNS Error]({{< relref "/tools/vercel/vercel-dns-error" >}}) — DNS verification failed
- [Vercel Project Error]({{< relref "/tools/vercel/vercel-project-error" >}}) — Project not found
