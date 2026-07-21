---
title: "[Solution] react-native Text Input Error"
description: "TextInput not focusing."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

TextInput not focusing.

## Common Causes

Wrong ref.

## How to Fix

Use useRef.

## Example

```javascript
const inputRef = useRef(null);
inputRef.current.focus();
```
