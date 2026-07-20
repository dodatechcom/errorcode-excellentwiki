---
title: "[Solution] Apache AllowOverride Not Allowed"
description: "The .htaccess file is trying to use directives that are not permitted by AllowOverride."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The .htaccess file is trying to use directives that are not permitted by AllowOverride.

## Common Causes

- AllowOverride None is set for the directory
- AllowOverride does not include the required directive category
- Directive category (AuthConfig, FileInfo, etc.) not enabled

## How to Fix

- Set AllowOverride All or the specific category needed
- Restart Apache after changing AllowOverride
- Place directives in the main config instead of .htaccess

## Examples

```
['<Directory /var/www/html>\n  AllowOverride AuthConfig FileInfo\n</Directory>']
```
