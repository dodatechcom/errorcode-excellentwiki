---
title: "[Solution] Apache mod_deflate Conflict"
description: "mod_deflate has a conflict, often with mod_ssl or caching modules."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

mod_deflate has a conflict, often with mod_ssl or caching modules.

## Common Causes

- DeflateFilterNote conflicts with SSL compression
- mod_deflate and mod_ssl compression both active
- Conflicting output filter chain

## How to Fix

- Disable SSLCompression when using mod_deflate
- Order output filters correctly
- Check for duplicate Deflate directives

## Examples

```
['# Disable SSL compression\nSSLCompression off\n# Use mod_deflate for HTTP\n<IfModule mod_deflate.c>\n  AddOutputFilterByType DEFLATE text/html\n</IfModule>']
```
