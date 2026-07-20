---
title: "[Solution] Apache SetHandler Not Allowed"
description: "The SetHandler directive is used in an invalid context."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The SetHandler directive is used in an invalid context.

## Common Causes

- SetHandler in .htaccess without AllowOverride FileInfo
- SetHandler used where AddHandler should be
- SetHandler in wrong configuration block

## How to Fix

- Ensure AllowOverride includes FileInfo for .htaccess usage
- Use SetHandler within <Location>, <Files>, or Directory
- Use AddHandler for file extension-based processing

## Examples

```
['<Location /server-status>\n  SetHandler server-status\n</Location>']
```
