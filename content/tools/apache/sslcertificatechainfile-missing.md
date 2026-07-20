---
title: "[Solution] Apache SSLCertificateChainFile Missing"
description: "The certificate chain or intermediate certificates are not configured."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The certificate chain or intermediate certificates are not configured.

## Common Causes

- Intermediate CA certificates not included
- SSLCertificateChainFile directive missing or points to wrong file
- Browser cannot validate the certificate chain

## How to Fix

- Combine intermediate certificates into a chain file
- Set SSLCertificateChainFile to the chain file path
- Order: server cert first, then intermediates, no root

## Examples

```
['# Create chain file\ncat intermediate.crt > chain.pem\n# Configure\nSSLCertificateChainFile /etc/ssl/chain.pem']
```
