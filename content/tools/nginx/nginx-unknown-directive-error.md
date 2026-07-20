---
title: "[Solution] Nginx Unknown Directive Error"
description: "Nginx fails to start because of an unknown directive in the configuration file."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx fails to start because of an unknown directive in the configuration file.

## Common Causes

- **Typo in directive name** (e.g., `direcitve` instead of `directive`)
- **Module not loaded** - the directive requires a module not compiled in
- **Deprecated syntax** no longer supported in your version
- **Wrong context** - using a directive where it is not allowed

## How to Fix

1. Check for typos: `grep -n 'unknown directive' /var/log/nginx/error.log`
2. Verify module: `nginx -V 2>&1 | grep -o 'with-[a-z_-]*' | sort`
3. Check the line number from the error and correct it
4. Validate: `sudo nginx -t`

## Examples

**Incorrect (typo):**
```nginx
server { lisetn 80; }  # typo
```
**Correct:**
```nginx
server { listen 80; server_name example.com; }
```
**Testing:**
```bash
sudo nginx -t
# syntax is ok
# test is successful
```