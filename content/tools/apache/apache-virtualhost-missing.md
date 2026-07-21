---
title: "[Solution] Apache VirtualHost Missing Error"
description: "Fix Apache VirtualHost missing errors when no matching VirtualHost block handles the request."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Apache returns the default VirtualHost content or an error because no matching VirtualHost configuration exists for the requested domain or IP.

## Common Causes

- VirtualHost block not defined for the domain
- ServerName or ServerAlias does not match request
- VirtualHost disabled or commented out
- Configuration file not included in main config
- IP-based VirtualHost uses wrong IP address

## How to Fix

- Add or correct a VirtualHost block with matching ServerName
- Ensure the configuration file is included in apache2.conf or sites-enabled
- Test configuration before restarting

## Examples

```apache
# /etc/apache2/sites-available/example.com.conf
<VirtualHost *:80>
    ServerName example.com
    ServerAlias www.example.com
    DocumentRoot /var/www/example.com

    <Directory /var/www/example.com>
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/example.com-error.log
    CustomLog ${APACHE_LOG_DIR}/example.com-access.log combined
</VirtualHost>

# Enable the site
sudo a2ensite example.com.conf
sudo systemctl reload apache2
```
