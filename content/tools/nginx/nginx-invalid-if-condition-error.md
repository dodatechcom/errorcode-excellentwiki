---
title: "[Solution] Nginx Invalid If Condition Error"
description: "An if directive contains an invalid condition or uses unsupported operators."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

An if directive contains an invalid condition or uses unsupported operators.

## Common Causes

- **Wrong operator** (Nginx if only supports =, !=, ~, ~*, ^~, -f, -d, -e, -x)
- **Missing quotes** around regex
- **Using if with proxy_pass** ("if is evil")
- **Complex boolean logic**

## How to Fix

1. Use only supported operators
2. Prefer separate location blocks over if
3. Use map for complex conditions
4. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
if ($host ~= "example.com") { }  # ~= not valid
```
**Valid:**
```nginx
if ($host = "example.com") { return 301 https://www.example.com$request_uri; }
```