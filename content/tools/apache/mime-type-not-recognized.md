---
title: "[Solution] Apache MIME Type Not Recognized"
description: "The MIME type specified in AddType or Content-Type is not recognized."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The MIME type specified in AddType or Content-Type is not recognized.

## Common Causes

- Typo in the MIME type string
- MIME type is not in the system's mime.types
- Custom MIME type not registered

## How to Fix

- Check the MIME type spelling against IANA list
- Add custom types with AddType
- Verify /etc/mime.types is up to date

## Examples

```
['AddType application/wasm .wasm\nAddType font/woff2 .woff2']
```
