---
title: "[Solution] Apache Script Output Too Large"
description: "The CGI script produced output that exceeds the configured size limit."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The CGI script produced output that exceeds the configured size limit.

## Common Causes

- Script generates more output than LimitRequestBody allows
- Script error causes massive output
- Default output limit exceeded

## How to Fix

- Increase LimitRequestBody if large output is expected
- Fix script to produce output within limits
- Stream output instead of buffering

## Examples

```
['# Allow up to 10MB\nLimitRequestBody 10485760']
```
