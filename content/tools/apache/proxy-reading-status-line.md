---
title: "[Solution] Apache Proxy Error Reading Status Line"
description: "Apache could not read the HTTP status line from the backend server response."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Apache could not read the HTTP status line from the backend server response.

## Common Causes

- Backend closed connection before sending status line
- Backend is using an incompatible protocol
- Network issue between Apache and backend
- Backend is down or not listening

## How to Fix

- Verify backend is running and accepting connections
- Check network connectivity between Apache and backend
- Increase ProxyTimeout
- Check backend logs for errors

## Examples

```
['# Test backend connectivity\ncurl -v http://backend:8080/\n# Check if backend is listening\nss -tlnp | grep 8080']
```
