---
title: "[Solution] Nginx Subrequest Error"
description: "Fix Nginx subrequest errors. Learn why this happens and how to resolve it quickly."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Nginx Subrequest Error

Nginx subrequest errors occur when internal requests or SSI includes fail.

## Why This Happens

- Subrequest failed
- Include not found
- SSI error
- Loop detected

## Common Error Messages

- `subrequest_failed_error`
- `subrequest_include_error`
- `subrequest_ssi_error`
- `subrequest_loop_error`

## How to Fix It

### Solution 1: Configure subrequests

Set up SSI includes:

```nginx
location / {
    ssi on;
}
```

### Solution 2: Fix include paths

Verify include file paths exist.

### Solution 3: Check for loops

Ensure subrequests don't create infinite loops.


## Common Scenarios

- **Subrequest failed:** Check the include path and file.
- **Loop detected:** Review subrequest chain for cycles.

## Prevent It

- Test subrequests carefully
- Monitor SSI performance
- Document include paths
