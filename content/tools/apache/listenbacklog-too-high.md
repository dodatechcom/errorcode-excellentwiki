---
title: "[Solution] Apache ListenBacklog Too High"
description: "The ListenBacklog value exceeds the system's maximum connection queue size."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The ListenBacklog value exceeds the system's maximum connection queue size.

## Common Causes

- Value exceeds sysctl somaxconn limit
- Value is negative or extremely large
- Value not supported by the operating system kernel

## How to Fix

- Set ListenBacklog to match or be below somaxconn
- Increase somaxconn: sysctl -w net.core.somaxconn=1024
- Use a reasonable value like 200-511

## Examples

```
['ListenBacklog 511\n# Or increase system limit:\n# sysctl -w net.core.somaxconn=1024']
```
