---
title: "[Solution] Apache LogFormat Parse Error"
description: "The LogFormat string contains invalid or unrecognized format specifiers."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The LogFormat string contains invalid or unrecognized format specifiers.

## Common Causes

- Invalid percent directive (e.g., %Z which is not supported)
- Mismatched quotes in the format string
- Unknown format specifier used

## How to Fix

- Check format string against Apache log format documentation
- Remove or replace invalid specifiers
- Escape literal percent signs with %%

## Examples

```
['LogFormat "%h %l %u %t \\"%r\\" %>s %b \\"%{Referer}i\\" \\"%{User-Agent}i\\"" combined']
```
