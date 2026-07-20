---
title: "[Solution] Apache RewriteMap Error"
description: "The RewriteMap directive references an invalid map or map type."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The RewriteMap directive references an invalid map or map type.

## Common Causes

- Map file does not exist or is not readable
- Invalid map type (int, rnd, dbm, txt, int)
- Map name is misspelled in RewriteRule

## How to Fix

- Verify the map file exists and is readable
- Use correct map type: txt, rnd, int, dbm, or prg
- Ensure map name matches in RewriteRule

## Examples

```
['RewriteMap lc int:tolower\nRewriteRule ^(.*)$ ${lc:$1} [L]']
```
