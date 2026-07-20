---
title: "[Solution] Apache SSLVerifyClient Required"
description: "Client certificate verification is required but failing or misconfigured."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Client certificate verification is required but failing or misconfigured.

## Common Causes

- SSLVerifyClient set to require but no CA configured
- Client certificate not signed by configured CA
- SSLCACertificatePath or SSLCACertificateFile not set
- Certificate expired or not yet valid

## How to Fix

- Set SSLCACertificateFile or SSLCACertificatePath
- Ensure client certificates are signed by the trusted CA
- Use SSLVerifyClient optional if client certs are not mandatory

## Examples

```
['SSLVerifyClient require\nSSLCACertificateFile /etc/ssl/ca-bundle.crt']
```
