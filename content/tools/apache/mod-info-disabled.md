---
title: "[Solution] Apache mod_info Disabled"
description: "The server-info handler is not available because mod_info is not loaded or configured."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The server-info handler is not available because mod_info is not loaded or configured.

## Common Causes

- LoadModule info_module missing
- SetHandler server-info not configured
- No access restrictions defined

## How to Fix

- LoadModule info_module modules/mod_info.so
- Add Location block for /server-info
- Restrict to trusted IPs only

## Examples

```
['<Location /server-info>\n  SetHandler server-info\n  Require ip 127.0.0.1\n</Location>']
```
