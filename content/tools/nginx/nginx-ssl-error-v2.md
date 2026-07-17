---
title: "[Solution] Nginx SSL — SSL_do_handshake failed"
description: "Fix Nginx SSL_do_handshake failed. Resolve SSL/TLS handshake failures in Nginx."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An SSL_do_handshake failed error means Nginx cannot complete the TLS handshake with either a client or an upstream server. The SSL/TLS negotiation fails and the connection is terminated.

## What This Error Means

The TLS handshake is the process where client and server negotiate encryption parameters, exchange certificates, and establish a secure session. When Nginx logs `SSL_do_handshake() failed`, it means the cryptographic negotiation broke down. This can happen during client-facing HTTPS (Nginx as server) or when connecting to an HTTPS upstream (Nginx as client). The specific error code reveals whether the issue is certificate-related, protocol mismatch, or cipher suite incompatibility.

## Common Causes

- SSL certificate has expired or is not yet valid
- Certificate chain is incomplete (missing intermediate CA)
- SSL protocol version mismatch (TLS 1.0 disabled vs client requirement)
- Cipher suite mismatch between client/server
- SNI hostname does not match certificate Common Name/SAN
- Self-signed certificate not trusted by the peer

## How to Fix

### Check Nginx SSL Error Logs

```bash
sudo tail -f /var/log/nginx/error.log | grep "SSL_do_handshake"
```

### Verify Certificate Chain

```bash
openssl s_client -connect example.com:443 -showcerts
```

### Check Certificate Expiry

```bash
openssl x509 -in /etc/nginx/ssl/cert.pem -noout -dates
```

### Fix Certificate Chain

```bash
# Concatenate certificate and intermediates
cat server.crt intermediate.crt root.crt > fullchain.crt
```

### Test SSL Configuration

```bash
openssl s_client -connect example.com:443 -tls1_2
openssl s_client -connect example.com:443 -tls1_3
```

### Fix Upstream SSL Verification

```nginx
location / {
    proxy_pass https://backend;
    proxy_ssl_verify on;
    proxy_ssl_trusted_certificate /etc/nginx/ssl/ca-bundle.crt;
    proxy_ssl_server_name on;
}
```

### Configure Modern TLS Settings

```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
ssl_prefer_server_ciphers off;
ssl_session_cache shared:SSL:10m;
ssl_session_timeout 10m;
```

### Fix SNI Configuration

```nginx
server {
    listen 443 ssl;
    server_name example.com;
    ssl_certificate /etc/nginx/ssl/example.com.crt;
    ssl_certificate_key /etc/nginx/ssl/example.com.key;
}
```

## Related Errors

- [Nginx 502 Bad Gateway]({{< relref "/tools/nginx/nginx-502-error-v2" >}}) — upstream connection closed
- [Nginx Proxy Error]({{< relref "/tools/nginx/nginx-proxy-error-v2" >}}) — proxy_pass connection error
- [Kubernetes Ingress Error]({{< relref "/tools/kubernetes/k8s-ingress-error-v2" >}}) — TLS configuration error
