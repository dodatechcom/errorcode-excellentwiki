---
title: "[Solution] Apache RewriteRule Too Complex"
description: "The RewriteRule pattern is too complex, causing performance issues or errors."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The RewriteRule pattern is too complex, causing performance issues or errors.

## Common Causes

- Excessive backreferences or lookaheads
- Pattern matching is too broad and matches everything
- Rule tries to do too much in a single step

## How to Fix

- Simplify the regex pattern
- Break complex rules into multiple simpler rules
- Use RewriteCond to narrow matches

## Examples

```
['# Instead of one complex rule:\nRewriteCond %{HTTP_HOST} ^www\\.(.*)$\nRewriteCond %{REQUEST_URI} !^/old/\nRewriteRule ^(.*)$ /%1$1 [R=301,L]']
```
