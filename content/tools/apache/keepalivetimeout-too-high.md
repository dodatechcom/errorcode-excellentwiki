---
title: "[Solution] Apache KeepAliveTimeout Too High"
description: "The KeepAliveTimeout is set too high, consuming worker resources."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The KeepAliveTimeout is set too high, consuming worker resources.

## Common Causes

- Timeout set to many seconds or minutes
- Idle connections occupying workers
- Combined with high MaxKeepAliveRequests

## How to Fix

- Reduce KeepAliveTimeout to 2-5 seconds
- Set MaxKeepAliveRequests to 100
- Monitor with server-status for idle connections

## Examples

```
['KeepAlive On\nKeepAliveTimeout 5\nMaxKeepAliveRequests 100']
```
