---
title: "[Solution] Apache FastCGI Process Exhausted"
description: "All FastCGI processes are busy and no more can be spawned."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

All FastCGI processes are busy and no more can be spawned.

## Common Causes

- FcgidMaxProcesses reached
- Backend processes not releasing resources
- FcgidProcessLifeTime too long keeping dead processes

## How to Fix

- Increase FcgidMaxProcesses
- Reduce FcgidProcessLifeTime to recycle stale processes
- Check for resource leaks in the application

## Examples

```
['FcgidMaxProcesses 100\nFcgidProcessLifeTime 600\nFcgidMinProcesses 5']
```
