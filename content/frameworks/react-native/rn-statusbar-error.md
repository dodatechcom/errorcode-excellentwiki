---
title: "[Solution] react-native StatusBar Error"
description: "StatusBar not hiding."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

StatusBar not hiding.

## Common Causes

Wrong prop.

## How to Fix

Use barStyle.

## Example

```javascript
import { StatusBar } from 'react-native';
<StatusBar barStyle="dark-content" backgroundColor="white" />
```
