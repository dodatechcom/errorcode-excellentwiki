---
title: "[Solution] Heroku ACM Error - Fix Automated Certificate Management Failed"
description: "Fix Heroku ACM certificate management failures. Resolve SSL certificate provisioning, renewal, and domain verification issues."
tools: ["heroku"]
error-types: ["acm-error"]
severities: ["error"]
weight: 5
---

This error means Heroku's Automated Certificate Management (ACM) failed to provision or renew an SSL certificate for your custom domain.

## What This Error Means

When ACM fails, your custom domain does not have a valid SSL certificate:

```
ACM: certificate issuance failed
# or
ACM: domain not verified
# or
ACM: private key mismatch
```

ACM automatically provisions and renews Let's Encrypt certificates for your Heroku apps. When it fails, HTTPS is unavailable on custom domains.

## Why It Happens

- The custom domain DNS is not pointing to Heroku correctly
- The domain verification check failed because DNS has not propagated
- The app does not have ACM enabled
- The SSL certificate renewal failed before expiration
- The domain uses CNAME records pointing to the wrong target
- Heroku's ACME provider is temporarily unavailable

## How to Fix It

### Check ACM status

```bash
heroku certs:auto -a my-app
```

This shows the current certificate status and any errors.

### Verify DNS configuration

```bash
host -t CNAME my-custom-domain.com
```

The CNAME must point to your app's Heroku DNS target:

```
my-custom-domain.com → my-app.herokuapp.com
```

### Enable ACM

```bash
heroku certs:auto:enable -a my-app
```

ACM is required for automatic SSL certificate management.

### Check domain verification

```bash
heroku domains -a my-app
```

Domains must be added and verified before ACM can issue certificates.

### Add a custom domain

```bash
heroku domains:add my-custom-domain.com -a my-app
```

### Force certificate renewal

```bash
heroku certs:auto:refresh -a my-app
```

This triggers a fresh certificate issuance attempt.

### Verify DNS has propagated

```bash
dig my-custom-domain.com CNAME +short
```

DNS propagation can take up to 48 hours.

### Check for expired certificates

```bash
echo | openssl s_client -connect my-custom-domain.com:443 2>/dev/null | openssl x509 -noout -dates
```

Expired certificates indicate ACM renewal failure.

## Common Mistakes

- Not waiting long enough for DNS propagation after adding a domain
- Using an A record instead of a CNAME for Heroku domains
- Forgetting to enable ACM after adding custom domains
- Not monitoring certificate expiration dates
- Assuming ACM works without proper DNS configuration first

## Related Pages

- [Heroku SSL Error]({{< relref "/tools/heroku/heroku-ssl-error" >}}) -- SSL configuration
- [Heroku Domain Error]({{< relref "/tools/heroku/heroku-domain-error" >}}) -- domain setup
- [Heroku Config Error]({{< relref "/tools/heroku/heroku-config-error" >}}) -- configuration issues
