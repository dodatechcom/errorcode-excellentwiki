---
title: "[Solution] Nginx Log Format Undefined Error"
description: "The access_log directive references a log format that was not defined with log_format."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The access_log directive references a log format that was not defined with log_format.

## Common Causes

- **access_log referencing undefined format**
- **log_format in wrong context**
- **Typo in format name**

## How to Fix

1. Define format before use
2. Check name matches exactly
3. Ensure at http level

## Examples

**Config:**
```nginx
http {
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" "$http_user_agent"';
    access_log /var/log/nginx/access.log main;
}
```