---
title: "[Solution] Apache Address Already in Use"
description: "Another Apache instance or process is already bound to the requested address."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Another Apache instance or process is already bound to the requested address.

## Common Causes

- Previous Apache process did not shut down cleanly
- Duplicate Listen directive in configuration
- Apache was restarted without stopping the old process first

## How to Fix

- Kill stale Apache processes: pkill httpd
- Ensure only one Apache instance runs
- Check for zombie processes

## Examples

```
['# Check for running processes\nps aux | grep apache\n# Kill if needed\npkill -9 httpd']
```
