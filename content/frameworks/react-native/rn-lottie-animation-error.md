---
title: "[Solution] React Native Lottie Animation Not Playing"
description: "react-native-lottie animation file does not render or freezes on first frame on Android and iOS in React Native apps"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The Lottie animation error occurs when an imported Lottie JSON file does not play or appears as a blank/static first frame. This can be caused by resource loading failure, incorrect source reference, or native renderer incompatibility.

## Common Causes

- Lottie JSON file not bundled with the app on Android
- Animation resource path uses require() with an incorrect relative path
- Lottie file contains expressions that are not supported on mobile
- Loop or autoplay props set to false without manual play()
- Animation JSON is too large causing out-of-memory on low-end devices
- LottieView width or height is 0 in the first render cycle

## How to Fix

1. Use require() for local animations:

```javascript
import LottieView from 'lottie-react-native';

<LottieView
  source={require('./animations/loader.json')}
  autoPlay
  loop
  style={{ width: 200, height: 200 }}
/>
```

2. For web-hosted animations, ensure the source is a valid URL:

```javascript
<LottieView
  source={{ uri: 'https://assets.example.com/loader.json' }}
  autoPlay
/>
```

3. Ensure the View has layout before Lottie renders:

```javascript
<View style={{ width: 200, height: 200 }}>
  <LottieView
    source={animData}
    autoPlay
    resizeMode="cover"
  />
</View>
```

## Examples

```javascript
// Error: Lottie shows blank screen on Android
// Fix: set resizeMode and explicit dimensions
<LottieView
  source={require('./anim/logo.json')}
  style={{ width: 100, height: 100 }}
  resizeMode="contain"
  autoPlay
/>
```

## Related Errors

- [Animated API Error]({{< relref "/frameworks/react-native/rn-animated-api-error" >}})
