---
title: "[Solution] Express req.acceptsLanguages Error"
description: "Language negotiation failing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Language negotiation failing.

## Common Causes

No matching language.

## How to Fix

Check Accept-Language.

## Example

```javascript
const lang = req.acceptsLanguages('en', 'es');
```
