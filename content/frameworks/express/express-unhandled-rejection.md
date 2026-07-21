---
title: "[Solution] Express Unhandled Rejection"
description: "Promise rejection not caught."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Promise rejection not caught.

## Common Causes

No handler.

## How to Fix

Add handler.

## Example

```javascript
process.on('unhandledRejection', (r) => console.error(r));
```
