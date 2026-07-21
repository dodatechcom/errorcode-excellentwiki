---
title: "[Solution] react-native TypeError Undefined Object"
description: "Cannot read property of undefined."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Cannot read property of undefined.

## Common Causes

Data not loaded yet.

## How to Fix

Add null checks.

## Example

```javascript
const name = user?.name ?? 'Unknown';
```
