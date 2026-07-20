---
title: "[Solution] Nginx Addition Types Error"
description: "The addition_types directive does not match the MIME type of the response being modified."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The addition_types directive does not match the MIME type of the response being modified.

## Common Causes

- **Default addition_types** only includes text/html
- **Response type not matching**
- **Module not compiled in**

## How to Fix

1. Add types: `addition_types text/html text/plain application/json;`
2. Add content before/after response

## Examples

**Config:**
```nginx
location / {
    addition_types text/html text/plain;
    add_before_body /includes/header.html;
    add_after_body /includes/footer.html;
    proxy_pass http://backend;
}
```