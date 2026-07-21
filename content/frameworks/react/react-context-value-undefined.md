---
title: "[Solution] React Context Value Undefined"
description: "Error when context consumer receives undefined."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when context consumer receives undefined.

## Common Causes

Provider value prop not set.

## How to Fix

Provide a meaningful default value.

## Example

```javascript
const ThemeContext = createContext('light');
```
