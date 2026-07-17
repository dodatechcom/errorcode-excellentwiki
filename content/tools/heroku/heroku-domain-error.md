---
title: "[Solution] Heroku App Not Found by Hostname Error — Fix Custom Domain"
description: "Fix Heroku app not found by hostname errors. Resolve custom domain configuration, DNS issues, and SNI problems."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
weight: 7
---

A Heroku app not found by hostname error occurs when a request to a custom domain cannot be routed to your Heroku app. This typically manifests as an H10 error in the logs and a generic error page for visitors.

## What This Error Means

```
H10 - App crash
at=error code=H10 desc="App crashed" ...
```

The custom domain is not properly configured or Heroku cannot map the hostname to your application. This is different from a 404 where the app is found but the route does not exist.

## Why It Happens

- The custom domain is not added to the Heroku app
- DNS records point to the wrong target
- The SSL certificate does not cover the domain
- The domain uses a wildcard that Heroku does not support
- DNS has not propagated after adding the domain
- The domain is set up for a different app

## How to Fix It

### Add Custom Domain

```bash
# Add the domain to your app
heroku domains:add www.your-domain.com

# Add apex domain
heroku domains:add your-domain.com

# List configured domains
heroku domains
```

### Configure DNS

```bash
# For subdomains (www.your-domain.com)
# CNAME your-domain.com -> your-app.herokuapp.com

# For apex domains (your-domain.com)
# A record -> 75.2.63.163 (Heroku's IP)
# Or use a DNS provider that supports ALIAS/ANAME records
```

### Check DNS Configuration

```bash
# Verify DNS is pointing correctly
dig www.your-domain.com +short
# Should return: your-app.herokuapp.com

dig your-domain.com +short
# Should return: 75.2.63.163
```

### Enable SNI SSL

```bash
# Heroku uses SNI for custom domain SSL
# Enable in Dashboard:
# Settings > Domains > Enable Heroku SSL

# Or via CLI
heroku certs:auto:enable
```

### Verify SSL Certificate

```bash
# Check SSL status
heroku certs:info

# If not provisioned, wait or contact support
```

### Use Heroku CI for DNS Check

```bash
# Check if domain resolves to Heroku
curl -I https://www.your-domain.com

# Should return Heroku headers
# Look for: via: 1.1 vegur
```

### Common DNS Providers

```bash
# Cloudflare: Set proxy to OFF (grey cloud)
# GoDaddy: Point CNAME to your-app.herokuapp.com
# Route53: Create CNAME or A record
# Namecheap: Advanced DNS > CNAME record
```

## Common Mistakes

- Forgetting to add the domain in Heroku Dashboard
- Using CNAME for apex domain (not supported by all DNS providers)
- Enabling proxy/CDN that interferes with Heroku routing
- Not waiting for DNS propagation after changes
- Not enabling SSL for the custom domain

## Related Pages

- [Heroku SSL Error]({{< relref "/tools/heroku/heroku-ssl-error" >}}) — SSL certificate error
- [Heroku Deploy Error]({{< relref "/tools/heroku/heroku-deploy-error" >}}) — Push rejected to Heroku
