---
title: "[Solution] Cloudflare 1303 Error — SSL Certificate Error"
description: "Fix Cloudflare Error 1303 when the origin SSL certificate is invalid, expired, or mismatched. Renew certificates, fix hostname mismatches, and update CA bundles."
tools: ["cloudflare"]
error-types: ["ssl-error"]
severities: ["error"]
weight: 5
---

Cloudflare Error 1303 occurs when Cloudflare tries to connect to your origin server over HTTPS but the origin's SSL certificate is invalid, expired, or does not match the requested hostname.

## What This Error Means

Cloudflare establishes a TCP connection to your origin but the SSL certificate validation fails. The certificate may be expired, self-signed (when strict mode is enabled), or mismatch the hostname.

## Why It Happens

- The origin SSL certificate has expired
- The certificate common name (CN) or Subject Alternative Name (SAN) does not match the origin hostname
- The certificate is self-signed and Cloudflare SSL mode is Full (strict)
- The certificate was issued by an untrusted certificate authority
- The certificate chain is incomplete (missing intermediate certificates)
- The origin server serves a certificate for a different domain (wrong SNI configuration)
- The origin is behind a load balancer that terminates SSL with a mismatched certificate

## How to Fix It

### Check the Origin Certificate

```bash
openssl s_client -connect your-origin.com:443 -servername your-origin.com
```

### Verify Certificate Details

```bash
echo | openssl s_client -connect your-origin.com:443 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

### Check Hostname Match

```bash
echo | openssl s_client -connect your-origin.com:443 2>/dev/null | openssl x509 -noout -text | grep DNS:
```

### Renew the Certificate

```bash
# Using Certbot for Let's Encrypt
sudo certbot renew --nginx
```

### Switch SSL Mode in Cloudflare

Go to SSL/TLS > Overview and change to **Full** mode (which accepts self-signed certs) instead of Full (strict).

### Fix Incomplete Certificate Chain

```bash
# Download intermediate certificates
curl -O https://letsencrypt.org/certs/lets-encrypt-r3.pem
# Combine with your certificate
cat your-cert.pem lets-encrypt-r3.pem > fullchain.pem
```

### Update SNI Configuration

```nginx
# nginx
server {
    listen 443 ssl;
    server_name your-origin.com;
    ssl_certificate /etc/ssl/certs/fullchain.pem;
    ssl_certificate_key /etc/ssl/private/privkey.pem;
}
```

## Common Mistakes

- Using SSL Full (strict) mode with a self-signed or expired certificate
- Not including intermediate certificates in the server configuration
- Serving a certificate for a different hostname than Cloudflare expects
- Forgetting to renew Let's Encrypt certificates every 90 days

## Related Pages

- [Cloudflare 1200 Error]({{< relref "/tools/cloudflare/cloudflare-1200" >}}) -- SSL/TLS protocol error
- [Cloudflare 526 Error]({{< relref "/tools/cloudflare/cloudflare-526" >}}) -- Invalid SSL certificate
- [Cloudflare 525 Error]({{< relref "/tools/cloudflare/cloudflare-525" >}}) -- SSL handshake failed
