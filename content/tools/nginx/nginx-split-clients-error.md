---
title: "[Solution] Nginx Split Clients Error"
description: "The split_clients block has an invalid hash source or percentage range."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The split_clients block has an invalid hash source or percentage range.

## Common Causes

- **Percentages exceeding 100%** total
- **Missing hash source**
- **Invalid variable** name
- **Ranges that do not add up**

## How to Fix

1. Ensure percentages do not exceed 100%
2. Use `*` catch-all for remainder
3. Provide valid hash source ($request_id, $remote_addr)
4. Validate: `sudo nginx -t`

## Examples

**Invalid:**
```nginx
split_clients $remote_addr $v { 60% a; 60% b; }  # total > 100%
```
**Fixed:**
```nginx
split_clients $remote_addr $v { 50% a; 50% b; }
```