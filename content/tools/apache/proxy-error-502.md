---
title: "[Solution] Apache Proxy Error 502 Bad Gateway"
description: "The backend server returned an invalid response or is unreachable."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The backend server returned an invalid response or is unreachable.

## Common Causes

- Backend server is down or not responding
- Backend returned malformed HTTP response
- Connection to backend was reset mid-transfer
- Backend overloaded or out of resources

## How to Fix

- Verify backend server is running
- Check ProxyPass and backend URL configuration
- Increase ProxyTimeout
- Check firewall rules between Apache and backend

## Examples

```
['ProxyPass /app http://backend:8080/\nProxyTimeout 300']
```
