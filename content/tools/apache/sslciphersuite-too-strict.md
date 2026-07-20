---
title: "[Solution] Apache SSLCipherSuite Too Strict"
description: "The cipher suite configuration excludes all possible ciphers or is incompatible."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The cipher suite configuration excludes all possible ciphers or is incompatible.

## Common Causes

- Cipher suite string is invalid or empty
- No ciphers match both client and server capabilities
- CipherSuite uses deprecated cipher names

## How to Fix

- Use a well-known cipher suite string
- Test with: openssl ciphers -v 'YOUR-CIPHER-STRING'
- Use Mozilla SSL Configuration Generator as reference

## Examples

```
['SSLCipherSuite HIGH:!aNULL:!MD5:!3DES\nSSLHonorCipherOrder on']
```
