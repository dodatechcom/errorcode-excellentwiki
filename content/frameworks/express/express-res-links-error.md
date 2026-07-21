---
title: "[Solution] Express res.links Error"
description: "Links header not setting."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Links header not setting.

## Common Causes

Wrong usage.

## How to Fix

Use res.links.

## Example

```javascript
res.links({ next: '/api?page=2' });
```
