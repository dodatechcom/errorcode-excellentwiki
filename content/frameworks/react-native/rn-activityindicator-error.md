---
title: "[Solution] React Native ActivityIndicator Styling Issue"
description: "react-native ActivityIndicator component fails to render custom colors or sizes on Android and iOS, resulting in invisible or mis-sized loading spinners in React Native apps"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The ActivityIndicator error occurs when the default spinner hides or refuses to render with the expected color/size. This is commonly encountered on Android where the ProgressBar default may conflict with host themes, or when using the color prop with a value that is not a valid string.

## Common Causes

- color prop is passed a number or object instead of a string
- style width/height is set too small or in a flex: 0 container
- Android native ProgressBar inherits a completely transparent theme
- ActivityIndicator is placed inside a collapsed parent view
- Dynamic color switching triggers internal state inconsistency

## How to Fix

1. Ensure color is a valid string, not a number or RGB object:

```javascript
// Wrong
<ActivityIndicator color={0x00FF00} />
// Wrong
<ActivityIndicator color={{r:0,g:255,b:0}} />
// Correct
<ActivityIndicator color="green" />
<ActivityIndicator color="#00FF00" />
<ActivityIndicator color="rgba(0,255,0,0.5)" />
```

2. Set explicit size if default is not visible:

```javascript
<ActivityIndicator
  size="large"
  color="#007AFF"
  style={{ flex: 1, justifyContent: 'center' }}
/>
```

3. Android-only: ensure theme does not hide ProgressBar:

```java
// MainActivity.java
// Force the spinner to be visible with default color
getWindow().getDecorView().setSystemUiVisibility(
  View.SYSTEM_UI_FLAG_VISIBLE
);
```

## Examples

```javascript
// Error: Spinner does not show on Android after theme update
<ActivityIndicator color="#000" />

// Fix: wrap in a View with explicit background
<View style={{backgroundColor: '#FFF', justifyContent: 'center'}}>
  <ActivityIndicator size="large" color="#007AFF" />
</View>
```

## Related Errors

- [StyleSheet Error]({{< relref "/frameworks/react-native/rn-stylesheet-error" >}})
