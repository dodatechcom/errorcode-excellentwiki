---
title: "[Solution] Cloudflare 525 SSL Handshake Failed Error — Fix SSL Connection"
description: "Fix Cloudflare 525 SSL handshake failed errors. Resolve SSL/TLS connection issues between Cloudflare and origin."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
weight: 4
---

A Cloudflare 525 error means the SSL/TLS handshake between Cloudflare and your origin server failed. Cloudflare cannot establish a secure connection to your server, which typically means the origin SSL certificate is invalid or misconfigured.

## What This Error Means

When Cloudflare tries to connect to your origin over HTTPS, it performs an SSL handshake to verify the server's certificate. If the certificate is invalid, expired, or misconfigured, the handshake fails and you get a 525 error.

## Why It Happens

- The origin server has an expired SSL certificate
- The SSL certificate does not match the domain name
- The origin server does not support SNI (Server Name Indication)
- Self-signed certificates on the origin are not trusted by Cloudflare
- The origin SSL certificate chain is incomplete
- TLS version mismatch between Cloudflare and origin
- The origin server is not configured for HTTPS at all

## How to Fix It

### Check Origin SSL Certificate

```bash
# Check certificate details
openssl s_client -connect your-origin-ip:443 -servername your-domain.com

# Check expiration date
echo | openssl s_client -connect your-origin-ip:443 2>/dev/null | \
  openssl x509 -noout -dates
```

### Fix Certificate Chain

```bash
# Ensure full certificate chain is installed
# Include intermediate certificates in your cert file

# For nginx
ssl_certificate /etc/ssl/fullchain.pem;  # Not just cert.pem
ssl_certificate_key /etc/ssl/privkey.pem;
```

### Enable SNI on Origin

```nginx
# nginx must have SNI enabled and server_name set
server {
    listen 443 ssl;
    server_name your-domain.com;

    ssl_certificate /etc/ssl/fullchain.pem;
    ssl_certificate_key /etc/ssl/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
}
```

### Use Origin Certificates from Cloudflare

```bash
# Generate a Cloudflare Origin Certificate
# 1. Go to SSL/TLS > Origin Server
# 2. Click "Create Certificate"
# 3. Download the certificate and key

# Install on origin
cat origin-cert.pem > /etc/ssl/certs/your-domain.pem
cat origin-key.pem > /etc/ssl/private/your-domain.key
```

### Test SSL Configuration

```bash
# Test SSL connection to origin
curl -v https://your-origin-ip.com \
  --resolve your-domain.com:443:your-origin-ip

# Check certificate validity
openssl x509 -in /etc/ssl/certs/your-domain.pem -text -noout
```

## Common Mistakes

- Using self-signed certificates on the origin
- Not including intermediate certificates in the chain
- Using the Cloudflare certificate on the origin instead of an origin certificate
- Forgetting to renew certificates before they expire
- Not configuring the origin for HTTPS when SSL mode is Full

## Related Pages

- [Cloudflare 526 Error]({{< relref "/tools/cloudflare/cloudflare-526" >}}) — Invalid SSL Certificate
- [Cloudflare 1020 Error]({{< relref "/tools/cloudflare/cloudflare-1020" >}}) — Access Denied
