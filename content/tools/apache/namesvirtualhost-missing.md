---
title: "[Solution] Apache NameVirtualHost Missing"
description: "The NameVirtualHost directive is missing or misconfigured for name-based hosting."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The NameVirtualHost directive is missing or misconfigured for name-based hosting.

## Common Causes

- Forgot to define NameVirtualHost for the port
- NameVirtualHost IP does not match Listen IP
- Apache 2.4 deprecated NameVirtualHost; removing it is correct

## How to Fix

- On Apache 2.2: add NameVirtualHost *:80 before VirtualHosts
- On Apache 2.4: simply remove the NameVirtualHost directive
- Verify Listen and VirtualHost use matching addresses

## Examples

```
['# Apache 2.2 only\nNameVirtualHost *:80\n# Apache 2.4: this line is no longer needed']
```
