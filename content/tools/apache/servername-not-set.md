---
title: "[Solution] Apache ServerName Not Set"
description: "The ServerName directive is not defined, so Apache cannot determine its own hostname."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The ServerName directive is not defined, so Apache cannot determine its own hostname.

## Common Causes

- ServerName not set globally or in VirtualHost
- DNS resolution fails for the server's hostname
- Apache uses the IP address instead of a hostname

## How to Fix

- Set ServerName in the global config or each VirtualHost
- Ensure DNS or /etc/hosts resolves the server name
- Use FQDN for ServerName

## Examples

```
['ServerName www.example.com:80']
```
