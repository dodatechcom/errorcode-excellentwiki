---
title: "[Solution] Apache DocumentRoot Not Found"
description: "The directory specified by DocumentRoot does not exist or is not accessible."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The directory specified by DocumentRoot does not exist or is not accessible.

## Common Causes

- Typo in DocumentRoot path
- Directory was deleted or moved
- File system permissions deny Apache access

## How to Fix

- Create the directory or correct the path
- Ensure proper ownership: chown -R www-data:www-data /var/www/html
- Check SELinux or AppArmor contexts

## Examples

```
['DocumentRoot /var/www/html\n<Directory /var/www/html>\n  Require all granted\n</Directory>']
```
