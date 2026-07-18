---
title: "[Solution] Nginx Sub Filter Error"
description: "Fix Nginx sub filter errors. Learn why this happens and how to resolve it quickly."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Nginx Sub Filter Error

Nginx sub_filter errors occur when content replacement fails or produces incorrect results.

## Why This Happens

- Filter not applied
- Pattern not found
- Replacement failed
- Multiple filters error

## Common Error Messages

- `nginx_sub_filter_not_applied_error`
- `nginx_sub_filter_pattern_error`
- `nginx_sub_filter_replacement_error`
- `nginx_sub_filter_multiple_error`

## How to Fix It

### Solution 1: Configure sub_filter

Set up content replacement:

```nginx
location / {
    sub_filter 'old' 'new';
    sub_filter_once off;
}
```

### Solution 2: Fix pattern issues

Verify the search pattern exists.

### Solution 3: Handle multiple filters

Chain sub_filter directives if needed.


## Common Scenarios

- **Filter not applied:** Check sub_filter configuration.
- **Pattern not found:** Verify the pattern exists in responses.

## Prevent It

- Test content replacement
- Monitor filter performance
- Handle edge cases
