---
title: "[Solution] Nginx Invalid Upstream Name Error"
description: "The upstream block name contains invalid characters or conflicts with a reserved name."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The upstream block name contains invalid characters or conflicts with a reserved name.

## Common Causes

- **Special characters** in name (`@`, `#`, spaces)
- **Name starts with digit or hyphen**
- **Duplicate upstream names** in different files

## How to Fix

1. Use only alphanumeric, hyphens, underscores, dots
2. Check duplicates: `grep -rn 'upstream ' /etc/nginx/conf.d/`
3. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
upstream backend@pool { }   # @ not allowed
upstream 1backend { }       # starts with digit
```
**Valid:**
```nginx
upstream backend_pool { }
upstream api-v2 { }
```