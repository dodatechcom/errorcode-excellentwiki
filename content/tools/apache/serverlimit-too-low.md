---
title: "[Solution] Apache ServerLimit Too Low"
description: "The ServerLimit directive is set too low to accommodate the current MaxRequestWorkers setting."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The ServerLimit directive is set too low to accommodate the current MaxRequestWorkers setting.

## Common Causes

- MaxRequestWorkers exceeds ServerLimit
- ServerLimit not increased before MaxRequestWorkers
- Default ServerLimit of 256 exceeded

## How to Fix

- Set ServerLimit >= MaxRequestWorkers
- ServerLimit requires a full restart (not graceful)
- Adjust both directives together

## Examples

```
['ServerLimit 512\nMaxRequestWorkers 512']
```
