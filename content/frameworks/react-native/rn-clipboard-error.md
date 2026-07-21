---
title: "[Solution] React Native Clipboard Error"
description: "Clipboard not working."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Clipboard not working.

## Common Causes

Not imported.

## How to Fix

Import Clipboard.

## Example

```javascript
import Clipboard from '@react-native-clipboard/clipboard';
Clipboard.setString('text');
```
