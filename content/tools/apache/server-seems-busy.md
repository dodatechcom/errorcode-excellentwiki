---
title: "[Solution] Apache Server Seems Busy"
description: "Apache is responding slowly and workers are all occupied."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Apache is responding slowly and workers are all occupied.

## Common Causes

- High concurrent connections
- Slow CGI or application responses
- Insufficient worker threads or processes
- Denial-of-service traffic

## How to Fix

- Increase ServerLimit and MaxRequestWorkers
- Move slow applications to separate servers
- Enable rate limiting with mod_ratelimit
- Use mod_evasive for DoS protection

## Examples

```
['# Use event MPM for better performance\nLoadModule mpm_event_module modules/mod_mpm_event.so']
```
