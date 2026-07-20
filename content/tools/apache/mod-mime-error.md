---
title: "[Solution] Apache mod_mime Error"
description: "The mod_mime module encountered an error mapping file extensions to content types."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The mod_mime module encountered an error mapping file extensions to content types.

## Common Causes

- Multiple extensions on a file (e.g., file.php.txt)
- AddType and RemoveType conflict
- Module not loaded but directives reference it

## How to Fix

- LoadModule mime_module modules/mod_mime.so
- Avoid multiple extensions on files
- Check AddType/RemoveType/DefaultType for conflicts

## Examples

```
['LoadModule mime_module modules/mod_mime.so\n# Ensure /etc/mime.types is accessible']
```
