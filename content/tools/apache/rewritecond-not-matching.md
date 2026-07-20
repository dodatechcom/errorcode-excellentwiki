---
title: "[Solution] Apache RewriteCond Not Matching"
description: "The RewriteCond test expression is not matching as expected."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The RewriteCond test expression is not matching as expected.

## Common Causes

- Incorrect test variable (e.g., %{REQUEST_URI} vs %{THE_REQUEST})
- Regex pattern does not match the intended input
- Condition flags like [NC] (case-insensitive) missing

## How to Fix

- Use %{THE_REQUEST} to match the original request line
- Test regex with online tools or command line
- Add [NC] for case-insensitive matching

## Examples

```
['RewriteCond %{THE_REQUEST} \\s/old-page\\s [NC]\nRewriteRule ^ /new-page [R=301,L]']
```
