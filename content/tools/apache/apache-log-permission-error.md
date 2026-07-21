---
title: "[Solution] Apache Log Permission Error"
description: "Fix Apache log permission errors when the server cannot write to error or access log files."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Apache fails to write to log files due to permission restrictions on the log directory or file.

## Common Causes

- Log directory not writable by Apache user
- Log file owned by root with restrictive permissions
- Disk space full on log partition
- SELinux blocking log writes
- Custom log path does not exist

## How to Fix

- Create log directory with correct ownership for Apache user
- Ensure disk space is available
- Verify SELinux context on log paths

## Examples

```bash
sudo mkdir -p /var/log/apache2
sudo chown www-data:www-data /var/log/apache2
sudo chmod 755 /var/log/apache2

# Check disk space
df -h /var/log

# Verify Apache can write logs
sudo -u www-data touch /var/log/apache2/test-write
sudo rm /var/log/apache2/test-write

# SELinux fix
sudo restorecon -Rv /var/log/apache2
```
