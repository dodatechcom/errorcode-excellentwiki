---
title: "[Solution] Apache server-status 403 Forbidden"
description: "Access to /server-status returns 403 Forbidden."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Access to /server-status returns 403 Forbidden.

## Common Causes

- No Require directive allows the client IP
- All Require denied the request
- Location block missing for server-status handler

## How to Fix

- Add Require ip for the accessing client
- Allow from localhost: Require ip 127.0.0.1
- Check access logs for denial reason

## Examples

```
['<Location /server-status>\n  SetHandler server-status\n  Require ip 127.0.0.1\n</Location>']
```
