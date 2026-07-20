---
title: "[Solution] Apache ProxyBadHeader"
description: "The backend server returned HTTP headers that are malformed or invalid."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The backend server returned HTTP headers that are malformed or invalid.

## Common Causes

- Backend sends non-standard header format
- Header contains invalid characters
- Backend response encoding is wrong
- Network corruption of response

## How to Fix

- Fix the backend application to send valid HTTP headers
- Check for encoding issues in backend response
- Use proxy-error overrides if backend cannot be fixed

## Examples

```
['# Check backend response\ncurl -v http://backend:8080/\n# Ensure clean HTTP/1.1 headers']
```
