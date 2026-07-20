---
title: "[Solution] Apache LogFormat Undefined"
description: "A CustomLog directive references a LogFormat nickname that has not been defined."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

A CustomLog directive references a LogFormat nickname that has not been defined.

## Common Causes

- Typo in the LogFormat nickname
- CustomLog references format before it is defined
- LogFormat defined in an unreachable config section

## How to Fix

- Define LogFormat before referencing it in CustomLog
- Check spelling of the nickname
- Ensure both directives are in the same config scope

## Examples

```
['LogFormat "%h %l %u %t \\"%r\\" %>s %b" common\nCustomLog logs/access.log common']
```
