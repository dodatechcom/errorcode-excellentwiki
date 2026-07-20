---
title: "[Solution] Apache DefaultType Missing"
description: "The DefaultType directive is not set, so Apache uses application/octet-stream for unknown types."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The DefaultType directive is not set, so Apache uses application/octet-stream for unknown types.

## Common Causes

- Unknown MIME types served with wrong Content-Type
- DefaultType not configured in main config
- Files without extensions served incorrectly

## How to Fix

- Set DefaultType to the most common type in your site
- Use text/html for HTML-heavy sites
- Set specific types with AddType for better accuracy

## Examples

```
['DefaultType text/html']
```
