---
title: "[Solution] Apache LogLevel Invalid"
description: "An invalid log level or module-specific log level is specified in LogLevel."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

An invalid log level or module-specific log level is specified in LogLevel.

## Common Causes

- Misspelled log level name
- Module name in level spec is not loaded
- Level value is not one of the recognized levels

## How to Fix

- Use valid levels: emerg, alert, crit, error, warn, notice, info, debug, trace1-trace8
- Verify module names are correct and loaded
- Consult Apache log level documentation

## Examples

```
['LogLevel warn\nLogLevel authz_core:trace5']
```
