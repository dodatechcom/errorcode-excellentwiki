---
title: "[Solution] Apache ErrorLog Rotation Failed"
description: "The error log rotation mechanism has failed."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The error log rotation mechanism has failed.

## Common Causes

- Log rotation command is not executable
- Rotated log file permissions wrong
- Disk full preventing log rotation
- Log file locked by another process

## How to Fix

- Check logrotate configuration
- Ensure the rotation script has proper permissions
- Verify sufficient disk space
- Use: lsof +D /var/log/apache2/

## Examples

```
['# Check disk space\ndf -h /var/log/apache2/\n# Check for locked files\nlsof /var/log/apache2/error.log']
```
