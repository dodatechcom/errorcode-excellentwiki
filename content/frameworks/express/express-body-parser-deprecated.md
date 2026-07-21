---
title: "[Solution] Express Body-Parser Deprecated"
description: "Using deprecated body-parser."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Using deprecated body-parser.

## Common Causes

Old package.

## How to Fix

Use express built-in.

## Example

```javascript
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
```
