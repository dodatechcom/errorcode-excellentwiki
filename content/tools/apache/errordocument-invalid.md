---
title: "[Solution] Apache ErrorDocument Invalid"
description: "The ErrorDocument directive points to an invalid file or URL."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The ErrorDocument directive points to an invalid file or URL.

## Common Causes

- File path does not exist
- Relative paths not resolved correctly
- ErrorDocument points to a URL without leading slash

## How to Fix

- Verify the ErrorDocument file exists and is readable
- Use absolute paths or paths relative to DocumentRoot
- For external URLs, use a full URL starting with http://

## Examples

```
['ErrorDocument 404 /errors/404.html\nErrorDocument 500 http://example.com/error500.html']
```
