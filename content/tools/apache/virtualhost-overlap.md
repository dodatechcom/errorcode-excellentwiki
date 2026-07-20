---
title: "[Solution] Apache VirtualHost Address Overlap"
description: "Two virtual hosts are configured on the same IP:port combination without name-based differentiation."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Two virtual hosts are configured on the same IP:port combination without name-based differentiation.

## Common Causes

- Multiple VirtualHost blocks with the same IP and port but no ServerName
- Default virtual host catches all unmatched requests
- Name-based virtual hosting not properly configured

## How to Fix

- Add unique ServerName to each VirtualHost
- Use name-based virtual hosting
- Ensure one VirtualHost is designated as the default

## Examples

```
['<VirtualHost *:80>\n  ServerName site1.com\n</VirtualHost>\n<VirtualHost *:80>\n  ServerName site2.com\n</VirtualHost>']
```
