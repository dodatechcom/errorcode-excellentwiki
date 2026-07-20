---
title: "[Solution] Apache CustomLog Permission Denied"
description: "Apache cannot open or write to the log file specified in CustomLog."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Apache cannot open or write to the log file specified in CustomLog.

## Common Causes

- Log file directory does not exist
- Apache user lacks write permissions
- SELinux or AppArmor blocks access
- Log file is owned by another process

## How to Fix

- Create the log directory and set ownership to the Apache user
- Use: chown www-data:www-data /var/log/apache2/
- Check SELinux: ausearch -m avc

## Examples

```
['# Ensure directory exists and is writable\nmkdir -p /var/log/apache2\nchown www-data:www-data /var/log/apache2']
```
