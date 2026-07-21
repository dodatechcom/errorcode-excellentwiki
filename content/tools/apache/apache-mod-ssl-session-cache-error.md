---
title: "[Solution] Apache mod_ssl Session Cache Error"
description: "Fix Apache mod_ssl shared session cache errors when SSL session caching fails."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache mod_ssl Session Cache Error

Apache mod_ssl encounters errors with shared SSL session cache.

```
AH02577: SSLSessionCache: Invalid argument
AH01941: dub: shared memory cache error
```

## Common Causes

- Shared memory segment too small
- SessionCache directory permissions wrong
- Cache file corruption
- Incorrect SessionCacheTimeout value
- Multiple SSL virtual hosts conflicting

## How to Fix

### Configure SSL Session Cache

```apache
# Use file-based session cache
SSLSessionCache shmcb:/var/run/ssl_scache(512000)
SSLSessionCacheTimeout 300
```

### Fix Shared Memory Permissions

```bash
# Ensure correct ownership
chown www-data:www-data /var/run/ssl_scache
chmod 755 /var/run
```

### Use Alternative Cache Storage

```apache
# Use DBM file-based cache
SSLSessionCache dbm:/var/lib/apache2/ssl_scache
SSLSessionCacheTimeout 300
```

### Increase Cache Size

```apache
# Increase shmcb size for high-traffic sites
SSLSessionCache shmcb:/var/run/ssl_scache(1024000)
SSLSessionCacheTimeout 600
```

### Disable SSL Session Cache for Testing

```apache
SSLSessionCache none
SSLSessionCacheTimeout 0
```

## Examples

```apache
# Production SSL configuration
<VirtualHost *:443>
    ServerName example.com
    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/example.com.crt
    SSLCertificateKeyFile /etc/ssl/private/example.com.key
    SSLSessionCache shmcb:/var/run/ssl_scache(512000)
    SSLSessionCacheTimeout 300
    SSLCompression off
    SSLProtocol all -SSLv3 -TLSv1 -TLSv1.1
</VirtualHost>
```
