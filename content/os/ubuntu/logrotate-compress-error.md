---
title: "Logrotate Compression Failed Error"
description: "Logrotate fails to compress rotated log files"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Logrotate Compression Failed Error

Logrotate fails to compress rotated log files

## Common Causes

- gzip or bzip2 not installed
- Disk full cannot write compressed file
- Permission denied on log directory
- Rotated file still open by application

## How to Fix

1. Check compressor: `which gzip bzip2`
2. Check disk space: `df -h /var/log/`
3. Use copytruncate to avoid holding file handles
4. Verify log directory permissions

## Examples

```bash
# Check available compressors
which gzip bzip2 xz

# Use copytruncate to avoid issues
# In logrotate config:
# /var/log/myapp.log {
#     daily
#     compress
#     copytruncate
# }
```
