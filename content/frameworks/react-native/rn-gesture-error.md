---
title: "[Solution] react-native Gesture Error"
description: "Gesture not responding."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Gesture not responding.

## Common Causes

Not wrapped.

## How to Fix

Wrap with GestureHandlerRootView.

## Example

```javascript
import { GestureHandlerRootView } from 'react-native-gesture-handler';
<GestureHandlerRootView><App /></GestureHandlerRootView>
```
