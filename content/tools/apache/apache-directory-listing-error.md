---
title: "[Solution] Apache Directory Listing Error"
description: "Fix Apache directory listing not showing or showing when it should not be displayed."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Apache Directory Listing Error

Apache either shows or hides directory listings contrary to expectations.

```
AH01276: Cannot access directory /var/www/app/ - end of directory list
```

## Common Causes

- Indexes option enabled when not intended
- DirectoryIndex not configured or missing
- No index.html or index.php in the directory
- .htaccess overrides global configuration
- Options directive set to All instead of specific options

## How to Fix

### Disable Directory Listing Globally

```apache
<Directory /var/www>
    Options -Indexes +FollowSymLinks
    AllowOverride None
</Directory>
```

### Configure Default Index Files

```apache
DirectoryIndex index.html index.php index.htm default.html
```

### Enable Only for Specific Directories

```apache
<Directory /var/www/downloads>
    Options +Indexes
    IndexOptions FancyIndexing VersionSort HTMLTable
    IndexIgnore .htaccess README
</Directory>
```

### Override via .htaccess

```apache
# /var/www/app/.htaccess
Options -Indexes
```

### Add Custom Index Page

```html
<!-- /var/www/app/index.html -->
<!DOCTYPE html>
<html>
<head><title>App</title></head>
<body><h1>Welcome</h1></body>
</html>
```

## Examples

```bash
# Find directories with directory listing enabled
grep -r "Options.*Indexes" /etc/apache2/ /var/www/
```

```apache
# Fancy directory listing configuration
<Directory /var/www/public-files>
    Options +Indexes
    IndexOptions FancyIndexing VersionSort HTMLTable NameWidth=*
    IndexIgnore .htaccess *.pyc __pycache__
    HeaderName /HEADER.html
    ReadmeName /README.html
</Directory>
```
