---
title: "[Solution] Apache AddDefaultCharset Error"
description: "The AddDefaultCharset directive specifies an invalid or unrecognized character set."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The AddDefaultCharset directive specifies an invalid or unrecognized character set.

## Common Causes

- Charset name is misspelled
- Charset is not supported by Apache
- AddDefaultCharset conflicts with AddDefaultCharsetOff

## How to Fix

- Use a valid charset name: UTF-8, ISO-8859-1
- Check Apache documentation for supported charsets
- Remove AddDefaultCharsetOff if you want default charset

## Examples

```
['AddDefaultCharset UTF-8']
```
