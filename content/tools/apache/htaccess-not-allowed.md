---
title: "[Solution] Apache .htaccess Not Allowed"
description: "The .htaccess file is present but AllowOverride is set to None."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The .htaccess file is present but AllowOverride is set to None.

## Common Causes

- AllowOverride None set for the directory tree
- Directive in .htaccess requires AllowOverride All
- Per-directory overrides not permitted in main config

## How to Fix

- Set AllowOverride All or the specific directive class
- Move directives to the main config instead
- Use <Directory> blocks in the main config

## Examples

```
['<Directory /var/www/html>\n  AllowOverride All\n</Directory>']
```
