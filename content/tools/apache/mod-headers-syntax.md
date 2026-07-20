---
title: "[Solution] Apache mod_headers Syntax Error"
description: "A Header directive has incorrect syntax."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

A Header directive has incorrect syntax.

## Common Causes

- Missing header value or name
- Invalid condition syntax
- Unquoted strings with special characters
- Append vs. set vs. add used incorrectly

## How to Fix

- Check Header directive syntax: Header [condition] set|append|add|unset|echo header value
- Quote header values with special characters
- Use always option for error pages: Header always set X-Frame-Options DENY

## Examples

```
['Header set X-Content-Type-Options nosniff\nHeader always set X-Frame-Options DENY']
```
