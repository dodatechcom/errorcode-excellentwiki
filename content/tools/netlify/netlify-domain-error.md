---
title: "[Solution] Netlify Custom Domain Not Provisioning Error — Fix Domain Setup"
description: "Fix Netlify custom domain provisioning errors. Resolve domain setup failures, SSL issues, and DNS configuration problems."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
weight: 8
---

A Netlify custom domain not provisioning error occurs when Netlify cannot set up SSL or configure your custom domain properly. The domain may be added but shows as "unverified" or SSL certificate provisioning fails.

## What This Error Means

Netlify auto-provisions SSL certificates via Let's Encrypt for custom domains. When provisioning fails, the domain shows errors in the dashboard and visitors see SSL warnings. The domain setup itself may appear incomplete.

## Why It Happens

- DNS records are not configured correctly
- The domain is not pointing to Netlify's load balancers
- DNS propagation is still in progress
- The domain is registered with a registrar that does not support required records
- The domain has an existing SSL certificate causing conflicts
- Too many DNS lookups causing provisioning timeout

## How to Fix It

### Configure DNS Records

```bash
# For apex domain (your-domain.com)
# Type: A
# Name: @
# Value: 75.2.60.5

# For subdomain (www.your-domain.com)
# Type: CNAME
# Name: www
# Value: your-site.netlify.app
```

### Add Domain in Dashboard

```bash
# In Netlify Dashboard:
# Site Settings > Domain Management > Add custom domain

# Enter your domain name
# Follow DNS verification steps
```

### Verify DNS Configuration

```bash
# Check DNS records
dig your-domain.com +short
dig www.your-domain.com +short

# Verify pointing to Netlify
# A record should resolve to 75.2.60.5
# CNAME should resolve to your-site.netlify.app
```

### Provision SSL Certificate

```bash
# In Netlify Dashboard:
# Site Settings > Domain Management > HTTPS
# Click "Verify DNS configuration"

# If stuck, try:
# 1. Remove the domain
# 2. Re-add it
# 3. Wait for DNS propagation
# 4. Provision certificate again
```

### Use Netlify DNS (Recommended)

```bash
# Switch to Netlify DNS for easier management
# 1. In Dashboard: Domain Management > Netlify DNS
# 2. Add your domain
# 3. Update nameservers at registrar to:
#    dns1.p01.nsone.net
#    dns2.p01.nsone.net
#    dns3.p01.nsone.net
#    dns4.p01.nsone.net
```

### Check Provisioning Status

```bash
# Via API
curl -X GET "https://api.netlify.com/api/v1/domains/YOUR_DOMAIN" \
  -H "Authorization: Bearer YOUR_TOKEN" | jq '.ssl'

# Check certificate status
curl -X GET "https://api.netlify.com/api/v1/sites/SITE_ID/ssl" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Wait for DNS Propagation

```bash
# DNS changes can take 24-48 hours
# Check propagation:
# https://www.whatsmydns.net/#A/your-domain.com

# Test from multiple locations
dig @8.8.8.8 your-domain.com +short
dig @1.1.1.1 your-domain.com +short
```

## Common Mistakes

- Not waiting for DNS propagation before checking provisioning
- Using both A and CNAME records for the same domain
- Not removing old DNS records from previous hosting
- Changing DNS and immediately removing the old hosting
- Not checking that registrar supports the required record types

## Related Pages

- [Netlify Domain Error]({{< relref "/tools/netlify/netlify-domain-error" >}}) — Custom domain not provisioning
- [Netlify Deploy Error]({{< relref "/tools/netlify/netlify-deploy-error" >}}) — Deploy failed
