---
title: "[Solution] Apache AddHandler Conflict"
description: "Multiple AddHandler or SetHandler directives conflict for the same file extension."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Multiple AddHandler or SetHandler directives conflict for the same file extension.

## Common Causes

- Two handlers registered for the same extension
- AddHandler and SetHandler contradict each other
- Handler for extension defined in multiple config files

## How to Fix

- Use only one handler per extension
- Remove conflicting handler definitions
- Use a single AddHandler for each extension

## Examples

```
['# Choose one:\nAddHandler cgi-script .cgi\n# Remove any conflicting:\n# SetHandler cgi-script .cgi']
```
