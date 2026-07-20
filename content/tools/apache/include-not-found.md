---
title: "[Solution] Apache Include Not Found"
description: "An Include directive references a file or directory that does not exist."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

An Include directive references a file or directory that does not exist.

## Common Causes

- Typo in the Include file path
- The referenced file was deleted or moved
- File permissions prevent Apache from reading the file
- Glob pattern in Include matches no files

## How to Fix

- Verify the path is correct and file exists
- Check file and directory permissions
- Use glob patterns with care; ensure at least one file matches

## Examples

```
['# Wrong path\nInclude /etc/apache2/conf.d/mistyped.conf\n# Correct\nInclude /etc/apache2/conf.d/myconfig.conf']
```
