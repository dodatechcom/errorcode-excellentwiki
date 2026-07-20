---
title: "[Solution] Apache AuthUserFile Not Found"
description: "The htpasswd file specified in AuthUserFile does not exist or is not readable."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The htpasswd file specified in AuthUserFile does not exist or is not readable.

## Common Causes

- File path is incorrect
- File not created with htpasswd utility
- File permissions prevent Apache from reading it

## How to Fix

- Create the file: htpasswd -c /etc/apache2/.htpasswd username
- Verify file exists and is readable by Apache user
- Check file permissions: chmod 640 .htpasswd

## Examples

```
['# Create password file\nhtpasswd -c /etc/apache2/.htpasswd admin\n# In Apache config\nAuthUserFile /etc/apache2/.htpasswd']
```
