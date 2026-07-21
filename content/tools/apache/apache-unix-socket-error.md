---
title: "[Solution] Apache Unix Socket Error"
description: "Fix Apache Unix domain socket errors when Apache cannot connect via Unix socket."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache Unix Socket Error

Apache fails to connect to a backend service via Unix domain socket.

```
AH01084: failed reading from /run/php/php-fpm.sock
AH00898: proxy: failed to connect to unix:/run/php/php-fpm.sock
```

## Common Causes

- Socket file does not exist
- Permissions on socket file too restrictive
- Socket path in Apache config is wrong
- Backend service not running
- SELinux blocking socket access

## How to Fix

### Verify Socket Exists

```bash
ls -la /run/php/php-fpm.sock
# If missing, restart the backend service
systemctl restart php-fpm
```

### Fix Socket Permissions

```apache
# For PHP-FPM socket
# In php-fpm pool config:
# Listen /run/php/php-fpm.sock
# ListenOwner www-data
# ListenGroup www-data
# ListenMode 0660
```

### Configure Apache to Use Socket

```apache
# In proxy config
<Proxy "unix:/run/php/php-fpm.sock|http://localhost">
    ProxyPass "unix:/run/php/php-fpm.sock|http://localhost"
</Proxy>
```

### Fix SELinux for Socket Access

```bash
# Check SELinux context
ls -Z /run/php/php-fpm.sock

# Allow Apache to connect
setsebool -P httpd_can_network_connect 1

# Or set proper context
semanage fcontext -a -t httpd_sys_rw_content_t "/run/php/php-fpm.sock"
restorecon -v /run/php/php-fpm.sock
```

### Ensure Correct Socket Path

```apache
# Double-check the socket path in both configs
# PHP-FPM: /etc/php/8.1/fpm/pool.d/www.conf
# Apache: /etc/apache2/sites-available/*.conf
```

## Examples

```apache
# PHP-FPM via Unix socket (faster than TCP)
<VirtualHost *:80>
    ServerName example.com
    DocumentRoot /var/www/html

    <FilesMatch \.php$>
        SetHandler "proxy:unix:/run/php/php-fpm.sock|http://localhost"
    </FilesMatch>
</VirtualHost>
```
