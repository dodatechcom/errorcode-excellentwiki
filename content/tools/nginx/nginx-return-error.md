---
title: "[Solution] Nginx Return Error"
description: "Fix Nginx return errors. Learn why this happens and how to resolve it quickly."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Nginx Return Error

Nginx return directive errors occur when return statements fail or create unexpected behavior.

## Why This Happens

- Invalid status code
- Return loop
- Header error
- Redirect failed

## Common Error Messages

- `return_status_error`
- `return_loop_error`
- `return_header_error`
- `return_redirect_error`

## How to Fix It

### Solution 1: Configure return

Set up return directive:

```nginx
location /old-path {
    return 301 /new-path;
}
```

### Solution 2: Fix status codes

Use valid HTTP status codes.

### Solution 3: Check return behavior

Verify return statements work as expected.


## Common Scenarios

- **Invalid status code:** Use a valid HTTP status code.
- **Return loop:** Check for redirect loops.

## Prevent It

- Use appropriate status codes
- Test return statements
- Monitor redirect chains
