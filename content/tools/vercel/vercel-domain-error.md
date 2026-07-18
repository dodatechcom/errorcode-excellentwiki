---
title: "[Solution] Vercel Domain Verification Failed Error — How to Fix"
description: "Fix Vercel domain verification failures. Resolve DNS configuration issues, nameserver updates, and SSL certificate provisioning errors."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Vercel domain verification failed error occurs when Vercel cannot verify that you own the domain you are trying to add. This prevents custom domain configuration, SSL certificate issuance, and deployment routing.

## What This Error Means

Vercel verifies domain ownership by checking DNS records (TXT, CNAME, or A records) that must be configured at your domain registrar. When these records are missing, incorrect, or have not propagated, verification fails and the domain cannot be used. Vercel periodically re-verifies domains and may de-configure them if verification fails.

## Why It Happens

- DNS records required for verification have not been added
- DNS records exist but have not propagated yet
- The TXT verification record is missing the required value
- CNAME or A record points to the wrong Vercel target
- Domain is using a nameserver that does not support required record types
- A conflicting DNS record is overriding the verification record
- Cloudflare proxy mode is interfering with the verification
- DNSSEC is enabled but DS records are incorrect

## Common Error Messages

- `Domain verification failed` — Required DNS records not found
- `Unable to verify domain ownership` — Verification record missing
- `DNS configuration error` — DNS records do not match Vercel's requirements
- `Domain is not ready for verification` — DNS has not propagated
- `SSL certificate could not be issued` — Domain verification required for SSL

## How to Fix It

### Check Required DNS Records

```bash
# For apex domains (example.com), you need an A record:
dig example.com A +short
# Should return: 76.76.21.21

# For subdomains (app.example.com), you need a CNAME:
dig app.example.com CNAME +short
# Should return: cname.vercel-dns.com.

# Check TXT verification record
dig _vercel.example.com TXT +short
# Should return: "vc-domain-verify=your-project-id"
```

### Add DNS Records at Registrar

```bash
# In your domain registrar's DNS panel, add:

# For apex domain (example.com):
# Type: A
# Name: @ (or leave blank)
# Value: 76.76.21.21
# TTL: 300

# For subdomain (app.example.com):
# Type: CNAME
# Name: app
# Value: cname.vercel-dns.com
# TTL: 300

# For domain verification (required):
# Type: TXT
# Name: _vercel
# Value: vc-domain-verify=your-project-id-here
# TTL: 300
```

### Verify DNS Propagation

```bash
# Check from multiple DNS resolvers
dig @1.1.1.1 example.com +short
dig @8.8.8.8 example.com +short
dig @9.9.9.9 example.com +short

# Check the TXT record specifically
dig @1.1.1.1 _vercel.example.com TXT +short
dig @8.8.8.8 _vercel.example.com TXT +short

# If records are not propagated, wait or check registrar settings
```

### Use Vercel CLI to Verify

```bash
# Add domain via CLI for better error messages
vercel domains add example.com

# Check domain status
vercel domains ls

# If verification fails, the CLI will show which records are missing
```

### Handle Domain Migration

```bash
# When moving from another provider:
# 1. Add domain in Vercel dashboard
# 2. Note the required DNS records
# 3. Update nameservers at registrar (if using Vercel DNS)
#    OR add individual DNS records (if keeping current DNS)
# 4. Wait for propagation (up to 48 hours for NS changes)
# 5. Click "Verify" in Vercel dashboard

# Verify the domain is working
curl -I https://your-domain.com
# Should return HTTP 200 with Vercel headers
```

### Handle SSL Certificate Issues

```bash
# If domain verification passes but SSL fails
# Check certificate status via API
curl -X GET "https://api.vercel.com/v4/certificates/CERT_ID" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Common SSL issues after verification:
# - DNS not fully propagated (wait 24-48 hours)
# - Conflicting CAA records blocking Let's Encrypt
# - Cloudflare proxy interfering with certificate validation

# Fix CAA records if needed
# In your DNS panel, add:
# 0 issue "letsencrypt.org"
# 0 issue "digicert.com"
```

### Handle Wildcard Domains

```bash
# For wildcard domains (*.example.com)
# You must use Vercel DNS (nameserver delegation)

# In Vercel Dashboard:
# 1. Add the domain: *.example.com
# 2. Vercel will provide nameserver records
# 3. Update your registrar to use Vercel's nameservers

# Verify wildcard DNS
dig *.example.com A +short
# Should return: 76.76.21.21
```

## Common Scenarios

- **Cloudflare proxied records:** If your domain uses Cloudflare and the proxy is enabled (orange cloud), the CNAME record is replaced with a Cloudflare IP, preventing Vercel from verifying the domain.
- **DNSSEC conflict:** DNSSEC is enabled at the registrar but the DS records do not include the correct keys, causing verification to fail for some resolvers.
- **Propagation delay:** You added the required DNS records but Vercel's verification check runs before the records have propagated globally.

## Prevent It

1. Add all required DNS records at least 24 hours before adding the domain to Vercel to ensure full propagation
2. Use Vercel DNS (nameserver migration) for the simplest setup and fastest verification
3. Keep the TXT verification record in place permanently — removing it can cause re-verification failures during certificate renewal

## Related Pages

- [Vercel Deployment Not Found]({{< relref "/tools/vercel/vercel-deployment-not-found" >}}) — Deployment not found
- [Vercel Env Variable Error]({{< relref "/tools/vercel/vercel-env-variable-error" >}}) — Environment variable issues
