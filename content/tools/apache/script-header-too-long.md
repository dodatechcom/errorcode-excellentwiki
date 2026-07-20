---
title: "[Solution] Apache Script Header Too Long"
description: "The CGI script output headers that exceed Apache's maximum header length."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The CGI script output headers that exceed Apache's maximum header length.

## Common Causes

- Script generates extremely long headers
- Infinite header output due to script bug
- Header buffer size exceeded

## How to Fix

- Reduce header length in the script
- Check for infinite loops in header generation
- Increase header buffer if legitimately needed

## Examples

```
['# In Apache config\nLimitRequestFields 100\nLimitRequestFieldSize 8190']
```
