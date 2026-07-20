---
title: "[Solution] Apache SSLProtocol Mismatch"
description: "The SSLProtocol directive has incompatible or invalid values."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The SSLProtocol directive has incompatible or invalid values.

## Common Causes

- SSLProtocol set to only old, insecure protocols
- Client supports none of the specified protocols
- Mixing incompatible protocol flags

## How to Fix

- Use: SSLProtocol all -SSLv2 -SSLv3 -TLSv1 -TLSv1.1
- Enable TLSv1.2 and TLSv1.3 only
- Test with: openssl s_client -connect host:443 -tls1_2

## Examples

```
['SSLProtocol all -SSLv2 -SSLv3 -TLSv1 -TLSv1.1\nSSLProtocol TLSv1.2 TLSv1.3']
```
