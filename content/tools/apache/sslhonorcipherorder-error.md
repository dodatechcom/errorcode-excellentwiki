---
title: "[Solution] Apache SSLHonorCipherOrder Error"
description: "The SSLHonorCipherOrder directive is misconfigured."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The SSLHonorCipherOrder directive is misconfigured.

## Common Causes

- Directive used when SSLCipherSuite is not set
- Value is not On or Off
- Conflicts with client's cipher preferences

## How to Fix

- Set SSLHonorCipherOrder On to prefer server cipher order
- Ensure SSLCipherSuite is defined
- Use server cipher order for security

## Examples

```
['SSLHonorCipherOrder on\nSSLCipherSuite HIGH:!aNULL:!MD5']
```
