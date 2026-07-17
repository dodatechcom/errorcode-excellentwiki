---
title: "[Solution] Heroku SSL Certificate Error — Fix SSL Configuration"
description: "Fix Heroku SSL certificate errors. Resolve custom domain SSL, SNI issues, and certificate provisioning failures."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
weight: 9
---

A Heroku SSL certificate error occurs when SSL cannot be provisioned or validated for your custom domain. Heroku uses SNI-based SSL which auto-provisions certificates, but configuration issues can cause failures.

## What This Error Means

```
!    Certificate URL is undefined
!    No certificate is active for this domain
```

Or browsers show SSL warnings when accessing your site. The SSL certificate for your custom domain is either not provisioned, expired, or misconfigured.

## Why It Happens

- Custom domain is not properly configured
- DNS is not pointing to Heroku correctly
- SNI SSL is not enabled for the app
- The domain has DNSSEC issues
- Heroku's Let's Encrypt integration failed
- The domain was recently added and cert is still provisioning

## How to Fix It

### Enable SNI SSL

```bash
# Check SSL status
heroku certs:auto

# Enable auto-SSL
heroku certs:auto:enable

# Check specific domain
heroku certs:info
```

### Verify DNS Configuration

```bash
# Check DNS records
dig www.your-domain.com +short
dig your-domain.com +short

# Ensure DNS points to Heroku
# Subdomain: CNAME -> app-name.herokuapp.com
# Apex: A record -> 75.2.63.163
```

### Use Heroku-managed Certificate

```bash
# Heroku auto-provisions via Let's Encrypt
# Wait for provisioning after adding domain

# Check provisioning status
curl -X GET "https://api.heroku.com/apps/my-app/ssl" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Accept: application/vnd.heroku+json; version=3"
```

### Upload Custom Certificate (Paid Plans)

```bash
# For paid plans, you can upload your own cert
heroku certs:add server.crt server.key

# Check cert info
heroku certs:info

# Remove auto-provisioned cert
heroku certs:auto:enable --disable
```

### Fix SSL Warning in Browser

```bash
# Check certificate details
echo | openssl s_client -connect www.your-domain.com:443 -servername www.your-domain.com 2>/dev/null | openssl x509 -noout -dates

# Check certificate chain
openssl s_client -connect www.your-domain.com:443 -showcerts
```

### Wait for Let's Encrypt Provisioning

```bash
# Let's Encrypt certificates take a few minutes
# After adding domain and DNS propagation

# Monitor provisioning
watch heroku certs:auto

# Force renewal
heroku certs:auto:refresh
```

### Fix DNSSEC Issues

```bash
# If using DNSSEC, ensure it does not conflict
# with Heroku's certificate provisioning

# Check DNSSEC status
dig your-domain.com +dnssec +short
```

## Common Mistakes

- Not waiting for DNS propagation before checking SSL
- Enabling DNSSEC which conflicts with Let's Encrypt
- Not adding the domain in Heroku before expecting SSL
- Using Cloudflare proxy mode which can interfere
- Not checking that SNI is enabled on the account

## Related Pages

- [Heroku Domain Error]({{< relref "/tools/heroku/heroku-domain-error" >}}) — App not found by hostname
- [Heroku Deploy Error]({{< relref "/tools/heroku/heroku-deploy-error" >}}) — Push rejected to Heroku
