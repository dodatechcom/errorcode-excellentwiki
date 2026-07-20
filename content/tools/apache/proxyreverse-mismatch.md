---
title: "[Solution] Apache ProxyPassReverse Mismatch"
description: "ProxyPassReverse does not match the corresponding ProxyPass configuration."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

ProxyPassReverse does not match the corresponding ProxyPass configuration.

## Common Causes

- ProxyPassReverse missing for a proxied path
- ProxyPassReverse URL does not match backend response
- Multiple ProxyPass without corresponding ProxyPassReverse

## How to Fix

- Add matching ProxyPassReverse for each ProxyPass
- Ensure the reverse URL matches the backend's redirect location
- Test with curl -I to check response headers

## Examples

```
['ProxyPass /app http://backend:8080/app\nProxyPassReverse /app http://backend:8080/app']
```
