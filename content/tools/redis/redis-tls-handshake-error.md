---
title: "[Solution] Redis TLS Handshake Error"
description: "How to fix Redis TLS handshake failure when establishing encrypted connections"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Expired or self-signed SSL certificate
- TLS version mismatch between client and server
- Missing or wrong certificate file paths in `redis.conf`
- Certificate chain incomplete
- Cipher suite not supported

## How to Fix

Verify TLS is enabled:

```bash
redis-cli CONFIG GET tls-port
```

Check certificate validity:

```bash
openssl x509 -in /etc/redis/tls/redis.crt -noout -dates
```

Verify the key matches the certificate:

```bash
diff <(openssl x509 -in /etc/redis/tls/redis.crt -noout -modulus)      <(openssl rsa -in /etc/redis/tls/redis.key -noout -modulus)
```

Test the TLS connection:

```bash
openssl s_client -connect localhost:6380 -cert /etc/redis/tls/redis.crt -key /etc/redis/tls/redis.key
```

Update `redis.conf` with correct TLS paths:

```bash
tls-cert-file /etc/redis/tls/redis.crt
tls-key-file /etc/redis/tls/redis.key
tls-ca-cert-file /etc/redis/tls/ca.crt
```

## Examples

```bash
# Connect with TLS
redis-cli --tls --cert /etc/redis/tls/redis.crt --key /etc/redis/tls/redis.key --cacert /etc/redis/tls/ca.crt

# Regenerate certificates
openssl req -x509 -newkey rsa:4096 -sha256 -days 365 -nodes   -keyout redis.key -out redis.crt -subj "/CN=localhost"
```
