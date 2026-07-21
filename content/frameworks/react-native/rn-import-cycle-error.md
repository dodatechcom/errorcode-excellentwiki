---
title: "[Solution] React Native Import Cycle Error"
description: "Circular dependency."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Circular dependency.

## Common Causes

Modules importing each other.

## How to Fix

Refactor.

## Example

```javascript
// Avoid A imports B, B imports A
```
