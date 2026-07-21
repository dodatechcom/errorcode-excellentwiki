---
title: "Apache Directory Index Error"
description: "Apache serves wrong directory listing or 403 Forbidden for directories"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Apache Directory Index Error

Apache serves wrong directory listing or 403 Forbidden for directories

## Common Causes

- DirectoryIndex not configured or file missing
- Options Indexes enabled but Indexes not available
- .htaccess overriding DirectoryIndex incorrectly
- Default index.html not present in directory

## How to Fix

1. Check config: `apachectl -S`
2. Set DirectoryIndex: `DirectoryIndex index.html index.htm`
3. Check file exists: `ls -la /var/www/html/`
4. Verify .htaccess: `apachectl -t`

## Examples

```apache
# Set directory index
<IfModule dir_module>
    DirectoryIndex index.html index.htm index.php
</IfModule>

# Check if file exists
# ls /var/www/html/index.html
```
