---
title: "[Solution] Apache Rsync Deploy Error"
description: "Fix Apache rsync deployment errors when syncing web files to the server fails."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache Rsync Deploy Error

Rsync fails to sync files to the Apache document root.

```
rsync: [sender] mkstemp failed: Permission denied (13)
rsync error: some files could not be transferred
```

## Common Causes

- Insufficient write permissions on DocumentRoot
- SSH key not configured for rsync
- SELinux blocking rsync write operations
- Disk space full on destination
- File ownership mismatch

## How to Fix

### Fix Permissions

```bash
# Set correct ownership
chown -R www-data:www-data /var/www/html

# Use rsync with correct flags
rsync -avz --delete --chown=www-data:www-data ./dist/ user@server:/var/www/html/
```

### Handle SELinux

```bash
# Check SELinux context
ls -Z /var/www/html

# Restore correct context
restorecon -Rv /var/www/html

# Or set permissive for rsync
setsebool -P httpd_sys_rw_content_t on
```

### Configure Rsync Script

```bash
#!/bin/bash
RSYNC_OPTS="-avz --delete --compress"
SRC="./dist/"
DEST="deploy@webserver:/var/www/html/"

rsync $RSYNC_OPTS "$SRC" "$DEST" && \
    ssh deploy@webserver "sudo systemctl reload apache2"
```

### Fix Disk Space

```bash
# Check disk usage
df -h /var/www
du -sh /var/www/html/*
```

## Examples

```bash
# Exclude files from rsync
rsync -avz --delete --exclude='.git' --exclude='node_modules' \
    ./dist/ deploy@server:/var/www/html/

# Dry run first
rsync -avzn --delete ./dist/ deploy@server:/var/www/html/
```
