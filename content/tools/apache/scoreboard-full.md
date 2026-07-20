---
title: "[Solution] Apache Scoreboard Full"
description: "The scoreboard that tracks worker status is full, indicating all workers are busy."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The scoreboard that tracks worker status is full, indicating all workers are busy.

## Common Causes

- All MaxRequestWorkers are active
- Scoreboard file is too small
- Workers stuck in reading or sending states

## How to Fix

- Increase MaxRequestWorkers and ServerLimit
- Investigate slow requests tying up workers
- Check for application-level bottlenecks

## Examples

```
['# Increase workers (requires restart, not graceful)\nServerLimit 512\nMaxRequestWorkers 512']
```
