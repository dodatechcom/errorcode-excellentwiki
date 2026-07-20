---
title: "[Solution] Apache mod_ssl Not Loaded"
description: "SSL directives are used but the mod_ssl module is not loaded."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

SSL directives are used but the mod_ssl module is not loaded.

## Common Causes

- LoadModule ssl_module is missing or commented out
- mod_ssl not installed
- SSL directives used before module is loaded

## How to Fix

- LoadModule ssl_module modules/mod_ssl.so
- On Debian/Ubuntu: a2enmod ssl
- Ensure mod_ssl matches Apache version

## Examples

```
['LoadModule ssl_module modules/mod_ssl.so\nSSLEngine on']
```
