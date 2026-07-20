---
title: "[Solution] Apache Worker Thread Limit"
description: "The thread limit for the MPM worker or event module is reached."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The thread limit for the MPM worker or event module is reached.

## Common Causes

- ThreadsPerChild exceeds ThreadLimit
- ThreadLimit not increased before ThreadsPerChild
- Default ThreadLimit of 64 or 19200 exceeded

## How to Fix

- Set ThreadLimit >= ThreadsPerChild
- Both require a full restart
- Tune based on system resources

## Examples

```
['ThreadLimit 256\nThreadsPerChild 256\nServerLimit 64']
```
