---
title: "[Solution] Nginx SSL Certificate Error"
description: "Nginx fails to start or process HTTPS connections because the SSL certificate or private key file is missing, invalid, or has incorrect permissions."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

# Nginx SSL Certificate Error

Nginx requires valid SSL certificate and key files to serve HTTPS traffic. An SSL certificate error occurs when the files are missing, expired, or have incorrect permissions.

## Common Causes

- The `ssl_certificate` path does not point to an existing file
- The private key does not match the certificate
- The certificate has expired or is not yet valid
- File permissions prevent Nginx worker process from reading the files

## How to Fix

1. Verify the certificate files exist:

```bash
ls -la /etc/nginx/ssl/cert.pem /etc/nginx/ssl/key.pem
```

2. Check that the key matches the certificate:

```bash
openssl x509 -noout -modulus -in cert.pem | md5sum
openssl rsa -noout -modulus -in key.pem | md5sum
# Both checksums must match
```

3. Fix file permissions:

```bash
chmod 644 /etc/nginx/ssl/cert.pem
chmod 600 /etc/nginx/ssl/key.pem
chown root:root /etc/nginx/ssl/cert.pem /etc/nginx/ssl/key.pem
```

4. Configure SSL in the server block:

```nginx
server {
    listen 443 ssl;
    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
}
```

## Examples

```bash
# Error output
nginx: [emerg] SSL_CTX_use_PrivateKey_file
  "/etc/nginx/ssl/key.pem" failed
  (SSL: error:02001002:system library:fopen:No such file or directory)
```

```nginx
# Correct SSL configuration
server {
    listen 443 ssl http2;
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
}
```

## Related Errors

- [SSL Error]({{< relref "/tools/nginx/nginx-ssl-error" >}}) -- general SSL issues
- [SSL Handshake Failed]({{< relref "/tools/nginx/nginx-ssl-handshake-failed-error" >}}) -- handshake failures
- [Cert Not Found]({{< relref "/tools/nginx/nginx-cert-not-found-error" >}}) -- missing certificates
