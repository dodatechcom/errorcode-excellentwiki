---
title: "[Solution] React Native LinearGradient Not Rendering"
description: "react-native-linear-gradient component shows blank or solid color instead of gradient fill on Android and iOS in React Native apps"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The LinearGradient rendering error occurs when the react-native-linear-gradient library fails to draw the gradient. On Android the library uses a custom Drawable layer, and on iOS it uses CAGradientLayer. Both can fail if the view layout is zero-sized or the colors array is invalid.

## Common Causes

- colors array contains fewer than 2 items
- View wrapping LinearGradient uses position: absolute without proper layout
- Parent has overflow: hidden and the gradient's native layer is clipped away
- LinearGradient style lacks width and height under a flex container
- Custom start and end points result in an invisible gradient (same point or inverted)
- Using rgba with double alpha like rgba(255,255,255, 1, 0.5) (syntax error)

## How to Fix

1. Ensure at least two colors are provided:

```javascript
import LinearGradient from 'react-native-linear-gradient';

<LinearGradient
  colors={['#4c669f', '#3b5998', '#192f6a']}
  style={{ width: '100%', height: 200 }}
>
  <Text>Gradient Wrapper</Text>
</LinearGradient>
```

2. Check for proper layout dimensions:

```javascript
// Bad: flex: 0 or no dimensions in parent
<View style={{ flex: 0 }}>
  <LinearGradient colors={['red','blue']} />
</View>

// Good: explicit or flex-based dimensions
<View style={{ flex: 1 }}>
  <LinearGradient colors={['red','blue']} style={{ flex: 1 }} />
</View>
```

## Examples

```javascript
// Error: LinearGradient shows white screen
// Fix: verify start/end points are not equal
<LinearGradient
  colors={['red', 'blue']}
  start={{ x: 0, y: 0 }}
  end={{ x: 1, y: 0 }}
  // ^ end.x != start.x -> horizontal gradient visible
/>
```

## Related Errors

- [StyleSheet Error]({{< relref "/frameworks/react-native/rn-stylesheet-error" >}})
