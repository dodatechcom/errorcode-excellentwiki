---
title: "[Solution] Apache mod_rewrite Not Loaded"
description: "The mod_rewrite module is required but has not been loaded."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The mod_rewrite module is required but has not been loaded.

## Common Causes

- LoadModule rewrite_module line is commented out or missing
- Module not installed
- RewriteEngine directives appear without loading the module

## How to Fix

- Uncomment or add: LoadModule rewrite_module modules/mod_rewrite.so
- On Debian/Ubuntu: a2enmod rewrite
- Restart Apache after enabling the module

## Examples

```
['# Enable mod_rewrite\nLoadModule rewrite_module modules/mod_rewrite.so\n# Or on Debian:\n# sudo a2enmod rewrite']
```
