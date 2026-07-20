---
title: "[Solution] Nginx Invalid Log Level Error"
description: "The error_log directive specifies an invalid or unrecognized log level."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The error_log directive specifies an invalid or unrecognized log level.

## Common Causes

- **Misspelled level** (e.g., "debg" instead of "debug")
- **Unsupported level** for your Nginx version
- **Level without debug module**

## How to Fix

1. Valid levels: debug, info, notice, warn, error, crit, alert, emerg
2. Debug requires --with-debug compilation
3. Check syntax

## Examples

**Valid levels:**
```nginx
error_log /var/log/nginx/error.log warn;
error_log /var/log/nginx/error.log error;
error_log /var/log/nginx/error.log crit;
error_log /var/log/nginx/error.log emerg;
```
**Debug (requires module):**
```nginx
error_log /var/log/nginx/error.log debug;
```