---
title: "[Solution] Apache server-info 403 Forbidden"
description: "Access to /server-info returns 403 Forbidden."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Access to /server-info returns 403 Forbidden.

## Common Causes

- No Require directive allows the client
- mod_info not loaded
- Location block for server-info missing or has wrong Require

## How to Fix

- Add Require ip for trusted clients only
- Load mod_info module
- Restrict to admin IPs for security

## Examples

```
['<Location /server-info>\n  SetHandler server-info\n  Require ip 127.0.0.1\n</Location>']
```
