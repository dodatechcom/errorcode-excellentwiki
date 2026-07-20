---
title: "[Solution] Nginx Range Not Satisfiable Error"
description: "The client requested a byte range outside the bounds of the available resource (HTTP 416)."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The client requested a byte range outside the bounds of the available resource (HTTP 416).

## Common Causes

- **Range start exceeds** file size
- **Range end exceeds** file size
- **Malformed Range header**
- **File size changed** since calculation

## How to Fix

1. Ensure backend handles Range correctly
2. Validate Range format
3. Disable if not needed: `proxy_set_header Range "";`

## Examples

**Test:**
```bash
curl -r 0-1023 http://example.com/file.zip -o /dev/null -w '%{http_code}'
# Valid: 206 Partial Content
# Invalid: 416 Range Not Satisfiable
```