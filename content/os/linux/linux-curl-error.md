---
title: "[Solution] Linux curl SSL Certificate Problem — Fix"
description: "Fix Linux 'curl: SSL certificate problem' errors. Resolve SSL/TLS certificate verification failures, expired certificates, and CA bundle issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: curl: SSL certificate problem

The `curl: (60) SSL certificate problem` error means curl cannot verify the SSL/TLS certificate presented by the remote server. This happens when the server's certificate is expired, self-signed, issued by an unknown CA, or when the local CA certificate bundle is outdated.

## What This Error Means

curl verifies SSL certificates by checking: (1) the certificate is not expired, (2) the hostname matches the certificate, and (3) the certificate chain traces back to a trusted Certificate Authority (CA). When any of these checks fail, curl refuses to connect. The error message typically includes the specific verification failure.

## Common Causes

- Server certificate is expired or not yet valid
- Self-signed certificate not trusted by the client
- CA certificate bundle is outdated on the client
- Hostname doesn't match the certificate's CN or SAN
- Certificate chain is incomplete (missing intermediate CA)
- System clock is incorrect
- Corporate proxy intercepting HTTPS traffic

## How to Fix

### 1. Update CA Certificates

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install ca-certificates
sudo update-ca-certificates

# RHEL/CentOS/Fedora
sudo dnf install ca-certificates
sudo update-ca-trust

# Arch
sudo pacman -S ca-certificates
```

### 2. Verify the Certificate Chain

```bash
# Check the certificate presented by the server
openssl s_client -connect example.com:443 -showcerts

# Check certificate expiry
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates

# Check certificate CN and SAN
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -text | grep -A1 "Subject Alternative"
```

### 3. Use --cacert to Specify CA Bundle

```bash
# Use a specific CA certificate file
curl --cacert /path/to/ca-certificates.crt https://example.com

# Use a specific certificate
curl --cacert /path/to/server.crt https://example.com
```

### 4. Disable Certificate Verification (Less Secure)

For testing or when you trust the server:

```bash
# Disable SSL verification
curl -k https://example.com
curl --insecure https://example.com

# For wget
wget --no-check-certificate https://example.com
```

### 5. Add Self-Signed Certificate to Trust Store

```bash
# Copy the certificate
sudo cp self-signed.crt /usr/local/share/ca-certificates/

# Update the trust store
sudo update-ca-certificates

# Or for RHEL/CentOS
sudo cp self-signed.crt /etc/pki/ca-trust/source/anchors/
sudo update-ca-trust
```

### 6. Fix System Clock

```bash
# Check current time
date

# If time is wrong, sync with NTP
sudo ntpdate pool.ntp.org    # If ntpdate installed
sudo timedatectl set-ntp true

# Or manually set time
sudo date -s "2025-01-01 12:00:00"
```

### 7. Handle Corporate Proxy Certificates

```bash
# Set the CA certificate for the proxy
export CURL_CA_BUNDLE=/path/to/proxy-ca.crt
curl https://example.com

# Or add to curl configuration
echo "cacert = /path/to/proxy-ca.crt" >> ~/.curlrc
```

## Examples

```bash
$ curl https://self-signed.example.com
curl: (60) SSL certificate problem: self-signed certificate

$ curl -k https://self-signed.example.com
{"status": "ok"}

$ openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
notBefore=Jan  1 00:00:00 2025 GMT
notAfter=Jan  1 00:00:00 2026 GMT
# Certificate is valid

$ curl https://expired.example.com
curl: (60) SSL certificate problem: certificate has expired
```

## Related Errors

- [openssl certificate error]({{< relref "/os/linux/linux-openssl-error" >}}) — OpenSSL verification issues
- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — Network connectivity issues
- [DNS errors]({{< relref "/os/linux/linux-resolv-conf-error" >}}) — DNS resolution failures
