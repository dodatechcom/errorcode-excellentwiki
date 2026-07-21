---
title: "[Solution] react-native Keyboard Dismiss Error"
description: "Keyboard not dismissing."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Keyboard not dismissing.

## Common Causes

Not calling dismiss.

## How to Fix

Call Keyboard.dismiss.

## Example

```javascript
import { Keyboard } from 'react-native';
Keyboard.dismiss();
```
