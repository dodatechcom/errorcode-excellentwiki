---
title: "[Solution] Cloudflare 526 Invalid SSL Certificate Error — Fix Origin Certificate"
description: "Fix Cloudflare 526 invalid SSL certificate errors. Resolve origin server certificate validation failures."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

A Cloudflare 526 error means Cloudflare cannot validate the SSL certificate presented by your origin server. This is different from a 525 error where the handshake fails entirely; here the certificate is presented but fails validation.

## What This Error Means

Cloudflare tried to verify the origin's SSL certificate and found it invalid. The certificate might be self-signed, expired, have a name mismatch, or have an incomplete trust chain. This error is common when SSL/TLS encryption mode is set to Full (Strict) in Cloudflare.

## Why It Happens

- The origin certificate is self-signed and Cloudflare requires a valid certificate
- The certificate has expired
- The domain name on the certificate does not match the request hostname
- The certificate chain is missing intermediate certificates
- SSL/TLS mode in Cloudflare is set to Full (Strict) but origin has an invalid cert
- The origin server is presenting a certificate for a different domain

## How to Fix It

### Option 1: Change SSL Mode to Flexible

```bash
# In Cloudflare dashboard:
# SSL/TLS > Overview > Set to "Flexible"
# This means Cloudflare connects to origin over HTTP
# Not recommended for security
```

### Option 2: Install Valid Certificate on Origin

```bash
# Using Let's Encrypt
sudo apt install certbot

# For nginx
sudo certbot --nginx -d your-domain.com

# For Apache
sudo certbot --apache -d your-domain.com

# Auto-renew
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

### Option 3: Use Cloudflare Origin Certificate

```bash
# Generate in Cloudflare Dashboard:
# SSL/TLS > Origin Server > Create Certificate

# Install the origin certificate
sudo cp origin-cert.pem /etc/ssl/certs/your-domain.pem
sudo cp origin-key.pem /etc/ssl/private/your-domain.key

# Restart web server
sudo systemctl restart nginx
```

### Verify Certificate Chain

```bash
# Check the complete certificate chain
openssl s_client -connect your-domain.com:443 -showcerts

# Verify certificate locally
openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt your-cert.pem
```

### Test Origin SSL

```bash
# Test directly to origin IP
curl -v https://your-origin-ip.com \
  --resolve your-domain.com:443:your-origin-ip

# Check certificate details
openssl x509 -in /etc/ssl/certs/your-domain.pem -text -noout
```

## Common Mistakes

- Using a self-signed certificate with Full (Strict) SSL mode
- Not installing the full certificate chain including intermediates
- Forgetting to restart the web server after certificate installation
- Using the wrong certificate for the domain
- Not setting up automatic certificate renewal

## Related Pages

- [Cloudflare 525 Error]({{< relref "/tools/cloudflare/cloudflare-525" >}}) — SSL Handshake Failed
- [Cloudflare 530 Error]({{< relref "/tools/cloudflare/cloudflare-530" >}}) — Origin DNS Error
