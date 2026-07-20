---
title: "[Solution] Apache Proxy Connection Timeout"
description: "The proxy connection to the backend timed out."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The proxy connection to the backend timed out.

## Common Causes

- Backend server is unreachable
- Network latency too high
- Firewall blocking the connection
- Backend overloaded

## How to Fix

- Increase ProxyTimeout or ProxyIOTimeout
- Check network path between Apache and backend
- Verify firewall rules
- Consider connection pooling

## Examples

```
['ProxyTimeout 120\nProxyIOTimeout 120']
```
