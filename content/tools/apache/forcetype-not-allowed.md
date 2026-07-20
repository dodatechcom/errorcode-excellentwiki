---
title: "[Solution] Apache ForceType Not Allowed"
description: "The ForceType directive is used in a context where it is not permitted."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The ForceType directive is used in a context where it is not permitted.

## Common Causes

- ForceType in .htaccess but AllowOverride does not include FileInfo
- ForceType used in VirtualHost context instead of Directory
- Directive not supported in the current configuration

## How to Fix

- Ensure AllowOverride includes FileInfo
- Use ForceType within <Directory> or .htaccess blocks
- Use AddType or SetHandler instead if appropriate

## Examples

```
['<Directory /var/www/html>\n  ForceType text/plain\n</Directory>']
```
