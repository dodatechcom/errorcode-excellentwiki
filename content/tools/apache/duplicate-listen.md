---
title: "[Solution] Apache Duplicate Listen Address"
description: "Two or more Listen directives try to bind to the same IP address and port combination."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Two or more Listen directives try to bind to the same IP address and port combination.

## Common Causes

- Configuration files both define Listen on the same port
- Include'd files redundantly specify the same port
- Listen directives in both global and virtual host context conflict

## How to Fix

- Remove duplicate Listen directives
- Use Include directives carefully to avoid duplication
- Bind different virtual hosts to different ports or IPs

## Examples

```
['# Remove one of these duplicates\nListen 80\nListen 80']
```
