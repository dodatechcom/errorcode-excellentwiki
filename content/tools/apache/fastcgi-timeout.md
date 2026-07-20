---
title: "[Solution] Apache FastCGI Timeout"
description: "The FastCGI application did not respond within the configured timeout."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The FastCGI application did not respond within the configured timeout.

## Common Causes

- Backend application is too slow
- FcgiIpcTimeout set too low
- Backend process is deadlocked or crashed
- Network latency between Apache and FastCGI backend

## How to Fix

- Increase FcgidIOTimeout or FcgidProcessLifeTime
- Optimize backend application response time
- Check if backend process is still running

## Examples

```
['FcgidIOTimeout 300\nFcgidConnectTimeout 60\nFcgidProcessLifeTime 3600']
```
