---
title: "[Solution] Apache Options Directive Conflict"
description: "Multiple conflicting Options directives apply to the same directory."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Multiple conflicting Options directives apply to the same directory.

## Common Causes

- Options set in .htaccess conflicts with main config
- Parent and child directory have incompatible Options
- Mixing +/- with full Options replacement

## How to Fix

- Use Options + or - syntax to selectively add or remove flags
- Ensure .htaccess options are compatible with AllowOverride
- Set Options in only one location if possible

## Examples

```
['# Avoid conflicting full declarations\n# Instead use\nOptions +FollowSymLinks\nOptions -Indexes']
```
