---
title: "[Solution] Apache mod_status Disabled"
description: "The server-status handler is not available because mod_status is not loaded or configured."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The server-status handler is not available because mod_status is not loaded or configured.

## Common Causes

- LoadModule status_module is missing
- SetHandler server-status not configured
- Access denied by Require directive

## How to Fix

- LoadModule status_module modules/mod_status.so
- Add Location block for /server-status
- Restrict access with Require ip

## Examples

```
['<Location /server-status>\n  SetHandler server-status\n  Require ip 127.0.0.1\n</Location>']
```
