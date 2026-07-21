---
title: "[Solution] React Native Accessibility Display Error"
description: "react-native AccessibilityInfo or accessibility display features returning incorrect values on Android and iOS, causing UI blindness for assistive tools in React Native apps"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The Accessibility/Display error in React Native occurs when AccessibilityInfo API returns unexpected values or the screen reader is not detected, leading to inaccessible UI components. This typically happens when the system's TalkBack or VoiceOver state is misread or when the accessibility data is not refreshed after navigation.

## Common Causes

- AccessibilityInfo not re-queried after component mount
- Incorrect handling of screen reader state on orientation change
- Race between WebView and AccessibilityInfo due to async callbacks
- React Navigation focus fires before AccessibilityInfo update
- AccessibilityInfo is undefined in WebView context

## How to Fix

1. Re-query AccessibilityInfo after navigation and layout changes:

```javascript
import { AccessibilityInfo } from 'react-native';

useEffect(() => {
  AccessibilityInfo.isScreenReaderEnabled().then((enabled) => {
    setIsScreenReaderEnabled(enabled);
  });
}, []);
```

2. Use the updated API for React Native 0.71+:

```javascript
AccessibilityInfo.addEventListener('screenReaderChanged', updateHandler);
```

3. For WebViews, inject accessibility data after load:

```javascript
import { WebView } from 'react-native-webview';

<WebView
  source={{ html }}
  onLoad={() => {
    AccessibilityInfo.isScreenReaderEnabled().then(enabled =>
      postAccessibilityState(enabled)
    );
  }}
/>;
```

## Examples

```javascript
// Error: accessibility info out of sync after navigate
navigation.addListener('blur', () => {
  // Missing re-query of AccessibilityInfo
});

// Fix: query on focus
navigation.addListener('focus', () => {
  AccessibilityInfo.isScreenReaderEnabled().then(setIsScreen).catch(console.warn);
});
```

## Related Errors

- [React Native Navigation Error]({{< relref "/frameworks/react-native/rn-navigation-error" >}})
