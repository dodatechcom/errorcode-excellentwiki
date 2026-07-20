---
title: "[Solution] Apache PidFile Not Writable"
description: "Apache cannot write the PID file to the specified location."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Apache cannot write the PID file to the specified location.

## Common Causes

- Directory does not exist
- Apache user lacks write permissions
- File already exists and is locked by another process
- SELinux context is wrong

## How to Fix

- Create the PID directory with proper ownership
- Set permissions: chown www-data:www-data /var/run/apache2/
- Check SELinux: restorecon -Rv /var/run/apache2/

## Examples

```
['mkdir -p /var/run/apache2\nchown www-data:www-data /var/run/apache2\nchmod 755 /var/run/apache2']
```
