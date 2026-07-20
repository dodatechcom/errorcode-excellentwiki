---
title: "[Solution] Apache suEXEC Error"
description: "The suEXEC wrapper encountered an error running CGI as a different user."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The suEXEC wrapper encountered an error running CGI as a different user.

## Common Causes

- suEXEC binary not installed or not in correct location
- User/group not permitted to run CGI
- suEXEC binary permissions are wrong
- DocumentRoot is not owned by the user

## How to Fix

- Verify suEXEC is installed: which suexec
- Ensure user/group exist and are valid
- Check suEXEC permissions: ls -la /usr/sbin/suexec

## Examples

```
['# Check suEXEC configuration\n/usr/sbin/suexec -V\n# Verify ownership\nls -la /home/user/public_html/']
```
