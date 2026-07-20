---
title: "[Solution] Nginx Split Clients Range Overflow Error"
description: "The split_clients percentage values exceed 100% or have overlapping ranges."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The split_clients percentage values exceed 100% or have overlapping ranges.

## Common Causes

- **Percentages summing > 100%**
- **Overlapping ranges**
- **Missing catch-all ***

## How to Fix

1. Ensure total <= 100%
2. Use * for remainder: `50% a; * b;`
3. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
split_clients $request_id $v { 60% a; 50% b; }  # > 100%
```
**Valid:**
```nginx
split_clients $request_id $v { 25% v1; 25% v2; 25% v3; 25% v4; }
```