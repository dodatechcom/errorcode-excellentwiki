---
title: "[Solution] Apache mod_status Restricted"
description: "Access to server-status is restricted and returning errors."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Access to server-status is restricted and returning errors.

## Common Causes

- Require directive does not match the requesting client
- No Location block defined for /server-status
- mod_status not loaded

## How to Fix

- Add proper Require directives for trusted IPs
- Load mod_status module
- Restrict access to localhost or admin subnet

## Examples

```
['<Location /server-status>\n  SetHandler server-status\n  Require ip 127.0.0.1 10.0.0.0/8\n</Location>']
```
