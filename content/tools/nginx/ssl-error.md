---
title: "[Solution] Nginx SSL Certificate Error"
description: "Fix Nginx SSL certificate errors. Resolve certificate verification, chain, and configuration issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Nginx SSL Certificate Error

An SSL certificate error occurs when Nginx cannot establish a secure connection because the certificate is invalid, expired, self-signed, or the certificate chain is incomplete.

## Common Causes

- The SSL certificate has expired
- The certificate does not match the server's domain name
- Intermediate or root certificates are missing from the chain
- The certificate or key file path is wrong in the Nginx config

## How to Fix

### Verify Certificate Details

```bash
openssl x509 -in /etc/ssl/certs/cert.pem -noout -dates -subject
```

### Check Certificate Chain

```bash
openssl s_client -connect example.com:443 -showcerts
```

### Configure Correct Certificate Paths

```nginx
server {
    listen 443 ssl;
    ssl_certificate /etc/ssl/certs/fullchain.pem;
    ssl_certificate_key /etc/ssl/private/privkey.pem;
}
```

### Renew an Expired Certificate

```bash
sudo certbot renew
sudo nginx -t && sudo systemctl reload nginx
```

### Generate a New Self-Signed Certificate (Development)

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/ssl/private/selfsigned.key \
  -out /etc/ssl/certs/selfsigned.crt
```

## Examples

```bash
# Expired certificate
# SSL: error:0A000086:SSL routines::certificate verify failed
# Fix: renew with certbot renew

# Missing intermediate certificate
# SSL: error:0A000086:SSL routines::certificate verify failed
# Fix: concatenate intermediate into fullchain.pem
cat cert.pem intermediate.pem > fullchain.pem
```

## Related Errors

- [SSL Certificate Problem]({{< relref "/tools/nginx/ssl-certificate" >}}) — self-signed certificate issues
- [Connection Refused]({{< relref "/tools/nginx/connection-refused6" >}}) — TCP connection rejected
