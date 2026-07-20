---
title: "[Solution] Nginx API Not Enabled Error"
description: "The Nginx API or status module is not enabled in the compiled binary."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The Nginx API or status module is not enabled in the compiled binary.

## Common Causes

- **Module not compiled in**
- **Trying to use stub_status or api without module**
- **Wrong Nginx build**

## How to Fix

1. Check: `nginx -V 2>&1 | grep -E 'stub_status|api'`
2. Use official Nginx package with modules
3. Recompile with --with-http_stub_status_module

## Examples

**Check modules:**
```bash
nginx -V 2>&1 | tr ' ' '
' | grep 'with-'
```