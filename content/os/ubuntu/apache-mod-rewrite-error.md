---
title: "Apache Mod_Rewrite Error"
description: "Apache mod_rewrite rules not working or causing 500 errors"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Apache Mod_Rewrite Error

Apache mod_rewrite rules not working or causing 500 errors

## Common Causes

- mod_rewrite module not enabled
- .htaccess override not allowed (AllowOverride None)
- RewriteRule syntax error in config
- Missing RewriteCond causing infinite loops

## How to Fix

1. Enable module: `sudo a2enmod rewrite`
2. Set AllowOverride: `AllowOverride All` for document root
3. Test rules: `apachectl -t` to check syntax
4. Check error log: `tail /var/log/apache2/error.log`

## Examples

```apache
# Enable AllowOverride in Apache config
<Directory /var/www/html>
    AllowOverride All
</Directory>

# Example .htaccess rewrite
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```
