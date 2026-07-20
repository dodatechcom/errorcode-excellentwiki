---
title: "[Solution] Apache AddType Invalid"
description: "The AddType directive has invalid syntax or an unrecognized MIME type."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The AddType directive has invalid syntax or an unrecognized MIME type.

## Common Causes

- MIME type string is incorrect
- File extension does not include the dot
- MIME type not registered in the system

## How to Fix

- Use correct MIME type format: application/javascript
- Ensure extension starts with a dot: .js
- Consult IANA MIME type list

## Examples

```
['AddType application/javascript .js\nAddType text/css .css']
```
