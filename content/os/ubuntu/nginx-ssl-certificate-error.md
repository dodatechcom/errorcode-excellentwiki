---
title: "[Solution] Ubuntu Server: nginx-ssl-certificate-error"
description: "Fix Ubuntu nginx-ssl-certificate-error. nginx SSL certificate configuration fails."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Nginx SSL Certificate Error

nginx fails to load SSL certificate or key.

## Common Causes
- Certificate file path incorrect
- Key file does not match certificate
- Certificate expired
- Private key permissions wrong
- Intermediate certificates missing

## How to Fix
1. Check certificate
```bash
sudo openssl x509 -in /etc/letsencrypt/live/example.com/fullchain.pem -text -noout | head -20
```
2. Verify key matches
```bash
sudo openssl x509 -noout -modulus -in cert.pem | md5sum
sudo openssl rsa -noout -modulus -in key.pem | md5sum
```
3. Fix permissions
```bash
sudo chmod 600 /etc/letsencrypt/live/example.com/privkey.pem
```

## Examples
```bash
$ sudo nginx -t
nginx: [emerg] SSL_CTX_use_PrivateKey_file("/etc/letsencrypt/live/example.com/privkey.pem") failed

$ sudo openssl x509 -noout -dates
notBefore=Mar 15 00:00:00 2023 GMT
notAfter=Jun 15 23:59:59 2023 GMT  # expired
```
