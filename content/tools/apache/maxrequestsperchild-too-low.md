---
title: "[Solution] Apache MaxRequestsPerChild Too Low"
description: "MaxRequestsPerChild is set so low that child processes recycle too frequently."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

MaxRequestsPerChild is set so low that child processes recycle too frequently.

## Common Causes

- Value is very small (e.g., 10-50)
- Frequent process restarts wasting resources
- Child processes do not live long enough to benefit from caching

## How to Fix

- Set MaxRequestsPerChild to 1000 or higher
- Set to 0 for unlimited (caution with memory leaks)
- Monitor process lifecycle with server-status

## Examples

```
['# Recycle processes after 10000 requests\nMaxRequestsPerChild 10000']
```
