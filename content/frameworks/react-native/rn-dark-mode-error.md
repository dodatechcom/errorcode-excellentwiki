---
title: "[Solution] react-native Dark Mode Error"
description: "Dark mode not switching."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Dark mode not switching.

## Common Causes

Not using theme.

## How to Fix

Use useColorScheme.

## Example

```javascript
import { useColorScheme } from 'react-native';
const colorScheme = useColorScheme();
```
