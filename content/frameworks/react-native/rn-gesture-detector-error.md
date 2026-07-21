---
title: "[Solution] React Native Gesture Detector Pan/Pinch Conflict"
description: "react-native-gesture-handler PanResponder or PinchHandler fails to activate or both fire simultaneously in React Native applications"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The gesture detector conflict error happens when multiple gesture handlers compete for the same touch sequence. The Gesture Handler library uses a waterfall activation model where only one handler should win, but improper configuration results in both pan and pinch handlers failing to meet activation criteria.

## Common Causes

- Pan and PinchGestureHandler nested without simultaneousHandlers config
- GestureDetector wrapping an element with its own touch responder
- Using both react-native-gesture-handler and PanResponder in the same view
- minDist or minPointers thresholds set too high for activation
- Handler refs not connected correctly via gestureDependency

## How to Fix

1. Use the composable Gesture API:

```javascript
import { Gesture, GestureDetector } from 'react-native-gesture-handler';

const pan = Gesture.Pan()
  .onStart((e) => console.log('pan started'))
  .minDistance(10);

const pinch = Gesture.Pinch()
  .onStart((e) => console.log('pinch started'));

const composed = Gesture.Simultaneous(pan, pinch);
```

2. Use simultaneousHandlers property for older API:

```javascript
<PanGestureHandler
  onGestureEvent={onPan}
  simultaneousHandlers={pinchRef}>
  <PinchGestureHandler
    ref={pinchRef}
    onGestureEvent={onPinch}>
    <Animated.View />
  </PinchGestureHandler>
</PanGestureHandler>
```

## Examples

```javascript
// Error: both pan and pinch fire at the same time
// Fix: use simultaneous gesture composition

const composed = Gesture.Race(pan, pinch);
<GestureDetector gesture={composed}>
  <Animated.View style={styles.box} />
</GestureDetector>
```

## Related Errors

- [Gesture Handler Error]({{< relref "/frameworks/react-native/rn-gesture-handler-error" >}})
