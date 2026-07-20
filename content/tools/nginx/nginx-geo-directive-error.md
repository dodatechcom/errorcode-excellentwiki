---
title: "[Solution] Nginx Geo Directive Error"
description: "The geo block contains invalid IP ranges, overlapping CIDR blocks, or incorrect syntax."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The geo block contains invalid IP ranges, overlapping CIDR blocks, or incorrect syntax.

## Common Causes

- **Incomplete CIDR notation**
- **Overlapping IP ranges**
- **Invalid variable name** or missing default
- **Mixing IPv4 and IPv6** incorrectly

## How to Fix

1. Use proper CIDR: `192.168.1.0/24`
2. Check overlapping: `grep -A30 'geo ' /etc/nginx/nginx.conf`
3. Use geo only at http level
4. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
geo $region { default 0; 192.168.1 1; }  # missing /24
```
**Fixed:**
```nginx
geo $trusted { default 0; 192.168.0.0/16 1; 10.0.0.0/8 1; }
```