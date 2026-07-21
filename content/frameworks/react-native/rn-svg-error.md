---
title: "[Solution] react-native SVG Error"
description: "SVG not rendering."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

SVG not rendering.

## Common Causes

Wrong import.

## How to Fix

Use react-native-svg.

## Example

```javascript
import Svg, { Circle } from 'react-native-svg';
<Svg><Circle cx="50" cy="50" r="40" /></Svg>
```
