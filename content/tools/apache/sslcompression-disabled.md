---
title: "[Solution] Apache SSLCompression Disabled"
description: "SSLCompression directive is configured but compression is not supported or is a security risk."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

SSLCompression directive is configured but compression is not supported or is a security risk.

## Common Causes

- SSLCompression on set but OpenSSL compiled without compression
- CRIME attack vulnerability when compression is enabled
- Directive not recognized by older OpenSSL

## How to Fix

- Set SSLCompression off (recommended)
- Do not enable TLS compression due to CRIME attack
- Remove the directive if using default (off)

## Examples

```
['SSLCompression off']
```
