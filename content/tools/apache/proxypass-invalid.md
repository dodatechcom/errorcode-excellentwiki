---
title: "[Solution] Apache ProxyPass Invalid"
description: "The ProxyPass directive has invalid syntax or configuration."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The ProxyPass directive has invalid syntax or configuration.

## Common Causes

- Missing URL or backend URL
- Invalid path syntax
- ProxyPass used in wrong context
- Trailing slash mismatch between source and target

## How to Fix

- Verify ProxyPass syntax: ProxyPass /path http://backend:port/path
- Ensure source and target paths have consistent trailing slashes
- Check that mod_proxy is loaded

## Examples

```
['# Correct - trailing slash matters\nProxyPass /app/ http://backend:8080/app/\nProxyPass /app http://backend:8080/app/']
```
