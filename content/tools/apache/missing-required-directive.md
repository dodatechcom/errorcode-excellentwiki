---
title: "[Solution] Apache Missing Required Directive"
description: "A mandatory configuration directive is missing from the configuration file."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

A mandatory configuration directive is missing from the configuration file.

## Common Causes

- ServerName not defined in virtual host
- DocumentRoot directive is absent
- Missing Listen directive so no ports are bound
- Required module-specific directives not set

## How to Fix

- Add the missing directive with a valid value
- Check module documentation for required parameters
- Use apachectl configtest to identify missing directives

## Examples

```
['<VirtualHost *:80>\n  # ServerName is required\n  ServerName example.com\n  DocumentRoot /var/www/html\n</VirtualHost>']
```
