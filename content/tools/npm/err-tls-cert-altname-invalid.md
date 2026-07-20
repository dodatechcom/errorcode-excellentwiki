---
title: "[Solution] npm install ERR_TLS_CERT_ALTNAME_INVALID TLS Cert Error"
description: "Handle ERR_TLS_CERT_ALTNAME_INVALID TLS certificate errors in npm install by fixing certificate trust, updating CA certs, and adjusting strict-ssl."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ERR_TLS_CERT_ALTNAME_INVALID TLS Cert Error

This guide helps you diagnose and resolve npm install ERR_TLS_CERT_ALTNAME_INVALID TLS Cert Error errors encountered when running npm commands.

## Common Causes

- Server TLS certificate does not match the expected hostname
- Corporate proxy intercepts HTTPS with a self-signed certificate
- System CA certificate store is outdated or missing root certificates

## How to Fix

### Update CA Certificates

```bash
sudo apt-get update && sudo apt-get install ca-certificates
```

### Set npm SSL Strict Mode Off Temporarily

```bash
npm config set strict-ssl false
```

### Set Custom CA Certificate

```bash
npm config set cafile /path/to/custom-ca.pem
```

## Examples

```bash
# Corporate proxy MITM certificate
npm install express
# Fix: Add corporate CA cert
npm config set cafile /etc/ssl/corporate-ca.pem

# Outdated CA certificates
npm install typescript
# Fix: Update system CA certs
sudo update-ca-certificates

```

## Related Errors

- [Connection Refused]({{< relref "/tools/npm/econnrefused-connection-refused" >}}) -- connection refused
- [DNS Error]({{< relref "/tools/npm/enotfound-dns-error" >}}) -- DNS resolution failed
