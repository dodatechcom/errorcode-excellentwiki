---
title: "[Solution] React Native Share Error"
description: "Share not working."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Share not working.

## Common Causes

Wrong usage.

## How to Fix

Use Share.share.

## Example

```javascript
import { Share } from 'react-native';
Share.share({ message: 'Check this out' });
```
