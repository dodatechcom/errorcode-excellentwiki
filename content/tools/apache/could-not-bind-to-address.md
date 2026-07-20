---
title: "[Solution] Apache Could Not Bind to Address"
description: "Apache cannot bind to the specified IP address and port."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Apache cannot bind to the specified IP address and port.

## Common Causes

- Port already in use by another process
- Insufficient privileges for ports below 1024
- IP address is not configured on this machine
- IPv6 address format incorrect

## How to Fix

- Check what is using the port: ss -tlnp | grep :80
- Use setcap or authbind for low ports
- Ensure the IP address exists on the system

## Examples

```
['# Find conflicting process\nss -tlnp | grep :80\n# Use a different port\nListen 8080']
```
