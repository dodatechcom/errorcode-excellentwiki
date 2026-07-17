---
title: "[Solution] Nginx SSL Handshake Error"
description: "Fix Nginx SSL handshake errors. Resolve TLS/SSL certificate and protocol issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An SSL handshake error means Nginx cannot establish a secure TLS connection with the client. This can be caused by certificate issues, protocol mismatches, or cipher suite problems.

## Common Causes

- SSL certificate is expired or invalid
- Certificate does not match the domain name
- SSL certificate chain is incomplete
- Client and server cannot agree on TLS protocol version
- Weak or unsupported cipher suites

## How to Fix

### Check Certificate Expiry

```bash
openssl x509 -in /etc/nginx/ssl/cert.pem -noout -dates
```

### Verify Certificate Chain

```bash
openssl verify -CAfile /etc/nginx/ssl/ca.pem /etc/nginx/ssl/cert.pem
```

### Test SSL Configuration

```bash
openssl s_client -connect example.com:443 -servername example.com
```

### Configure SSL Protocols

```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
```

### Fix Certificate Chain

```bash
cat intermediate.pem >> fullchain.pem
```

## Examples

```bash
# Expired certificate
# SSL handshake failed
# Fix: renew certificate with certbot

# Incomplete chain
# SSL handshake error
# Fix: include intermediate certificates
```

## Related Errors

- [Nginx SSL Error]({{< relref "/tools/nginx/nginx-ssl-error" >}}) — SSL certificate error
- [Nginx Proxy Error]({{< relref "/tools/nginx/nginx-proxy-error" >}}) — reverse proxy error
