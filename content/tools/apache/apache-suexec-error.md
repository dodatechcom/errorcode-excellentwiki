---
title: "[Solution] Apache suexec Error"
description: "Fix Apache suexec errors when CGI scripts fail to run under the correct user identity."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache suexec Error

Apache suexec fails to execute CGI scripts under the specified user identity.

```
suexec policy violation: directory not owned by root
AH01210: suexec: uid != (uid_min + uid) || gid != (gid_min + gid)
```

## Common Causes

- DocumentRoot not owned by root
- CGI script directory has wrong permissions
- Script binary is world-writable
- suexec binary is not installed
- Script not in allowed directory path

## How to Fix

### Fix Directory Permissions

```bash
# DocumentRoot must be owned by root
chown root:root /var/www/html
chmod 755 /var/www/html

# CGI directory needs correct ownership
chown root:www-data /var/www/cgi-bin
chmod 755 /var/www/cgi-bin
```

### Fix Script Permissions

```bash
# CGI scripts must be owned by the user they run as
chown www-data:www-data /var/www/cgi-bin/script.cgi
chmod 755 /var/www/cgi-bin/script.cgi
```

### Check suexec Configuration

```bash
# Verify suexec is installed and correct
ls -la /usr/sbin/suexec
# Must be setuid root
```

### Validate suexec Path

```bash
# Check compiled paths
/usr/sbin/suexec -V
# Should show docroot and directory match your setup
```

### Disable suexec if Not Needed

```apache
# Remove or comment out suexec from config
# Use mod_php or fcgid instead
```

## Examples

```bash
# Create proper CGI directory
mkdir -p /var/www/cgi-bin
chown root:root /var/www/cgi-bin
chmod 755 /var/www/cgi-bin

# Place and set up a CGI script
cp myscript.cgi /var/www/cgi-bin/
chown www-data:www-data /var/www/cgi-bin/myscript.cgi
chmod 755 /var/www/cgi-bin/myscript.cgi
```
