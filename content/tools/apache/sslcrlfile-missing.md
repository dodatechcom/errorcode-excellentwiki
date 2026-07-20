---
title: "[Solution] Apache SSLCRLFile Missing"
description: "The Certificate Revocation List file is missing or invalid."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The Certificate Revocation List file is missing or invalid.

## Common Causes

- CRL file path is incorrect
- CRL file not generated or updated
- CRL has expired

## How to Fix

- Download or generate a fresh CRL
- Set the correct path in SSLCRLFile
- Automate CRL updates with a cron job

## Examples

```
['SSLCRLFile /etc/ssl/crl/ca-crl.pem']
```
