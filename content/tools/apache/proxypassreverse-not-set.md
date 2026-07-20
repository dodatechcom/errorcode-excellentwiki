---
title: "[Solution] Apache ProxyPassReverse Not Set"
description: "Backend server responses contain internal redirects or links that are not rewritten."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Backend server responses contain internal redirects or links that are not rewritten.

## Common Causes

- Missing ProxyPassReverse directive
- ProxyPassReverse URL does not match backend's redirect location
- Application generates absolute URLs pointing to backend

## How to Fix

- Add ProxyPassReverse for each ProxyPass
- Match ProxyPassReverse URL to backend's actual redirect URL
- Test with curl -I to verify Location headers

## Examples

```
['ProxyPass /app http://backend:8080/\nProxyPassReverse /app http://backend:8080/']
```
