---
title: "[Solution] Apache Gzip Compression Error"
description: "Fix Apache mod_deflate compression errors when gzip encoding fails or produces invalid output."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache Gzip Compression Error

Apache mod_deflate fails to compress responses or sends corrupted compressed data.

```
AH05067: name-based name mapping failed for deflate
```

## Common Causes

- mod_deflate not loaded
- Output filter not properly configured
- Already compressed content being re-compressed
- Memory limits exceeded during compression
- Broken pipe during compression

## How to Fix

### Enable mod_deflate

```bash
a2enmod deflate
systemctl restart apache2
```

### Configure Compression

```apache
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE text/javascript
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/json
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/xml
</IfModule>
```

### Avoid Re-Compressing Content

```apache
<IfModule mod_deflate.c>
    # Do not compress already compressed files
    SetOutputFilter DEFLATE
    SetEnvIfNoCase Request_URI \.(?:gif|jpe?g|png|zip|gz|bz2|rar)$ no-gzip
    SetEnvIfNoCase Request_URI \.(?:mp[34]|ogg|wav|flac)$ no-gzip
</IfModule>
```

### Fix Memory Issues

```apache
# Increase memory for compression
DeflateMemLevel 9
DeflateCompressionLevel 6
```

## Examples

```apache
# Full compression configuration
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/plain text/xml
    AddOutputFilterByType DEFLATE text/css text/javascript application/javascript
    AddOutputFilterByType DEFLATE application/json application/xml application/rss+xml
    AddOutputFilterByType DEFLATE image/svg+xml font/woff2

    DeflateCompressionLevel 6
    DeflateMemLevel 9

    SetEnvIfNoCase Request_URI \.(?:gif|jpe?g|png|zip|gz|bz2|rar|mp[34])$ no-gzip dont-vary
    Header append Vary User-Agent env=!dont-vary
</IfModule>
```
