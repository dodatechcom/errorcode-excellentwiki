---
title: "[Solution] Apache Client Denied by Server Configuration"
description: "Apache denied access to the client based on server configuration."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Apache denied access to the client based on server configuration.

## Common Causes

- Deny from all directive blocking the request
- Require directive does not match client IP or credentials
- Order allow,deny with missing Allow rule
- GeoIP or environment-based blocking

## How to Fix

- Check Allow/Deny or Require directives
- Verify client IP is permitted
- Review access logs for denial details

## Examples

```
['<Directory /var/www/protected>\n  Require ip 192.168.1.0/24\n</Directory>']
```
