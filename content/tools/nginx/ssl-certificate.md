---
title: "[Solution] Nginx SSL Certificate Problem — self-signed certificate"
description: "Fix Nginx SSL certificate problems. Resolve self-signed certificate and SSL handshake errors."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["ssl", "certificate", "self-signed", "tls", "handshake"]
weight: 5
---

# Nginx SSL Certificate Problem — self-signed certificate

This error occurs when Nginx or a client encounters an SSL certificate that is self-signed, expired, or not trusted by the certificate authority. The SSL handshake fails and the connection is rejected.

## Common Causes

- Using a self-signed certificate instead of one from a trusted CA
- Certificate has expired
- Certificate does not match the domain name being accessed
- Intermediate certificates are missing from the chain

## How to Fix

### Generate a Let's Encrypt Certificate

```bash
sudo certbot --nginx -d example.com
```

### Generate a Self-Signed Certificate (for development)

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/ssl/private/nginx-selfsigned.key \
  -out /etc/ssl/certs/nginx-selfsigned.crt
```

### Configure Nginx SSL

```nginx
server {
    listen 443 ssl;
    ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
    ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;
}
```

### Verify Certificate Chain

```bash
openssl s_client -connect example.com:443 -showcerts
```

### Update Nginx After Certificate Renewal

```bash
sudo nginx -t
sudo systemctl reload nginx
```

## Examples

```bash
# Example 1: Self-signed cert in development
# Browser shows: NET::ERR_CERT_AUTHORITY_INVALID
# Fix: use certbot for trusted certificate or accept self-signed in dev

# Example 2: Expired certificate
openssl x509 -enddate -noout -in /etc/ssl/certs/cert.pem
# notAfter=Dec 31 23:59:59 2025 GMT
# Fix: renew with certbot renew
```

## Related Errors

- [Upstream Error]({{< relref "/tools/nginx/upstream-error" >}}) — 502 Bad Gateway from upstream
- [Service Failed]({{< relref "/tools/systemd/service-failed" >}}) — Nginx service failing to start
