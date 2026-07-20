---
title: "[Solution] Apache RewriteLog Deprecated"
description: "The RewriteLog directive is used but has been deprecated."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The RewriteLog directive is used but has been deprecated.

## Common Causes

- Using RewriteLog instead of LogLevel for rewrite debugging
- Apache 2.4+ removed RewriteLog
- Logging level not set high enough for rewrite traces

## How to Fix

- Use LogLevel rewrite:trace3 or higher instead of RewriteLog
- Set LogLevel in the relevant VirtualHost or Directory
- Use trace levels 1-8 for varying detail

## Examples

```
['LogLevel rewrite:trace3\n# Trace levels:\n# trace1 - minimal\n# trace8 - most verbose']
```
