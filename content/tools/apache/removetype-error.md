---
title: "[Solution] Apache RemoveType Error"
description: "The RemoveType directive has incorrect syntax or does not remove the expected type."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The RemoveType directive has incorrect syntax or does not remove the expected type.

## Common Causes

- Extension argument does not include the dot
- Extension does not match any previously added type
- RemoveType used in wrong context

## How to Fix

- Use the full extension with dot: RemoveType .cgi
- Ensure the type was previously added with AddType
- Check config file load order

## Examples

```
['RemoveType .php\nRemoveType .cgi']
```
