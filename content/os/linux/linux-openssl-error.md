---
title: "[Solution] Linux openssl Certificate Error — Fix"
description: "Fix Linux 'openssl: certificate error' and verification failures. Diagnose SSL/TLS certificate issues, expired certs, and chain problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["openssl", "certificate-error", "ssl", "tls", "x509", "ca-certificate"]
weight: 5
---

# Linux: openssl: certificate error

The `openssl: certificate error` message means the OpenSSL library encountered a problem verifying or processing an SSL/TLS certificate. This can occur when using `openssl s_client`, `openssl verify`, or when applications linked against OpenSSL fail certificate validation.

## What This Error Means

OpenSSL is the underlying cryptographic library used by most Linux tools for SSL/TLS. Certificate errors in OpenSSL indicate the certificate chain cannot be validated against the trusted CA store, the certificate is malformed, expired, or the hostname doesn't match. Understanding the specific error code helps identify the root cause.

## Common Causes

- CA certificate bundle is outdated or missing
- Certificate has expired or is not yet valid
- Self-signed certificate not in trust store
- Certificate chain is incomplete (missing intermediate)
- Hostname mismatch (CN or SAN doesn't match)
- Certificate uses deprecated algorithms (MD5, SHA-1)
- OpenSSL version doesn't support the certificate's TLS version

## How to Fix

### 1. Update CA Certificate Bundle

```bash
# Debian/Ubuntu
sudo apt update && sudo apt install ca-certificates
sudo update-ca-certificates

# RHEL/CentOS/Fedora
sudo dnf install ca-certificates
sudo update-ca-trust
```

### 2. Verify a Certificate

```bash
# Check certificate validity
openssl x509 -in certificate.pem -noout -dates -subject -issuer

# Verify against CA bundle
openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt certificate.pem

# Check certificate chain
openssl s_client -connect example.com:443 -showcerts

# Check specific TLS version support
openssl s_client -connect example.com:443 -tls1_2
openssl s_client -connect example.com:443 -tls1_3
```

### 3. Diagnose the Specific Error

```bash
# Common OpenSSL error codes:
# 20 = unable to get local issuer certificate
# 21 = unable to verify first certificate
# 10 = certificate has expired
# 18 = self signed certificate
# 19 = self signed certificate in certificate chain

# Get detailed error
openssl s_client -connect example.com:443 2>&1 | grep -E "Verify|error|depth"
```

### 4. Fix Certificate Chain Issues

```bash
# Download the full certificate chain
openssl s_client -connect example.com:443 -showcerts < /dev/null 2>/dev/null | \
  awk '/BEGIN CERTIFICATE/,/END CERTIFICATE/{print}' > chain.pem

# Split into individual certificates
csplit chain.pem '/-----BEGIN CERTIFICATE-----/' '{*}'
```

### 5. Generate and Use Self-Signed Certificates

```bash
# Generate a self-signed certificate
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout server.key -out server.crt \
  -subj "/CN=example.com"

# Generate with SAN
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout server.key -out server.crt \
  -subj "/CN=example.com" \
  -addext "subjectAltName=DNS:example.com,DNS:*.example.com"
```

### 6. Add Certificate to System Trust Store

```bash
# Copy certificate to trust store
sudo cp my-ca.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates

# For RHEL/CentOS
sudo cp my-ca.crt /etc/pki/ca-trust/source/anchors/
sudo update-ca-trust
```

### 7. Set OpenSSL Environment Variables

```bash
# Set CA bundle location
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_DIR=/etc/ssl/certs

# For custom CA
export CURL_CA_BUNDLE=/path/to/custom-ca.crt
```

## Examples

```bash
$ openssl s_client -connect example.com:443
...
Verify return code: 10 (certificate has expired)

$ openssl x509 -in server.crt -noout -dates
notBefore=Jan  1 00:00:00 2024 GMT
notAfter=Jan  1 00:00:00 2025 GMT
# Expired!

$ openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt server.crt
error 10: certificate has expired

$ openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt server.crt
server.crt: OK
# After renewal
```

## Related Errors

- [curl SSL error]({{< relref "/os/linux/linux-curl-error" >}}) — curl certificate verification failures
- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — Network connectivity issues
- [DNS errors]({{< relref "/os/linux/linux-resolv-conf-error" >}}) — DNS resolution failures
