---
title: "[Solution] Nginx Invalid Listen Directive Error"
description: "The listen directive contains invalid syntax or unsupported parameters."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The listen directive contains invalid syntax or unsupported parameters.

## Common Causes

- Using **protocol names** instead of port numbers
- **Invalid IP:port format**
- Misspelled **parameters** (e.g., `defualt_server`)
- **Deprecated parameters** in newer versions

## How to Fix

1. Use correct syntax: `listen [IP]:PORT [parameters];`
2. Valid params: `default_server`, `ssl`, `http2`, `reuseport`, `backlog=N`
3. Check for typos
4. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
listen http;           # error: not a port
listen 80 default;     # error: should be default_server
```
**Valid:**
```nginx
listen 80;
listen 443 ssl;
listen [::]:80 default_server;
listen 8080 reuseport backlog=1024;
```