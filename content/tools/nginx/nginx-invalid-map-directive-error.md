---
title: "[Solution] Nginx Invalid Map Directive Error"
description: "The map directive has invalid syntax or conflicting source/target definitions."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The map directive has invalid syntax or conflicting source/target definitions.

## Common Causes

- **Duplicate source values** in same map block
- **Missing `default`** when no source matches
- **Invalid regex patterns**
- **Wrong number of parameters**

## How to Fix

1. Check for duplicates: `grep -A20 'map ' file.conf | sort | uniq -d`
2. Use `default` for unmatched values
3. Ensure only one `default` per map block
4. Validate: `sudo nginx -t`

## Examples

**Invalid - duplicate:**
```nginx
map $uri $handler {
    default file_a; /api handler_api; /api handler_api2;
}
```
**Fixed:**
```nginx
map $uri $handler { default file_a; /api handler_api; /dashboard handler_dash; }
```