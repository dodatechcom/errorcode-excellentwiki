---
title: "[Solution] Apache MaxClients Too High"
description: "MaxRequestWorkers (formerly MaxClients) is set higher than the system can support."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

MaxRequestWorkers (formerly MaxClients) is set higher than the system can support.

## Common Causes

- Value exceeds available system memory
- Exceeds ServerLimit value
- System cannot fork enough child processes

## How to Fix

- Reduce MaxRequestWorkers to match available RAM
- Set appropriate values based on: Available RAM / memory per process
- Monitor with server-status to tune

## Examples

```
['# With 2GB RAM and ~20MB per process:\nMaxRequestWorkers 100']
```
