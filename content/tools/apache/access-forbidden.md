---
title: "[Solution] Apache Access to Path Forbidden"
description: "Access to a specific path or resource is forbidden by Apache configuration."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Access to a specific path or resource is forbidden by Apache configuration.

## Common Causes

- Options -Indexes set and no index file exists
- Require all denied for the directory
- File permissions prevent access
- SELinux or AppArmor blocking access

## How to Fix

- Add an index file or enable Options +Indexes
- Set Require all granted for the directory
- Check file ownership and permissions

## Examples

```
['<Directory /var/www/html>\n  Options +FollowSymLinks +Indexes\n  Require all granted\n</Directory>']
```
