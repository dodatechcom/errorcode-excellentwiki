---
title: "[Solution] React Native Overlay Modal not dismissing"
description: "react-native Modal or Overlay component not dismissing when pressing back or tapping outside on Android and iOS"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The overlay or modal dismiss error occurs when the Modal component does not hide in response to Android hardware back press or iOS swipe-down gesture. This is often caused by incorrect transparent prop, missing onRequestClose handler, or modal layered behind another view.

## Common Causes

- Modal on Android lacks the onRequestClose prop
- Multiple Modals stacked and the top one is not set visible=false
- Modal's presentation style conflicts with the navigation container
- TouchableOpacity or Pressable inside the modal absorbs tap events
- The modal's visible prop is not bound to the correct state setter
- hardwareAccelerated prop on Android causing z-index ordering issues

## How to Fix

1. Ensure onRequestClose is provided for Android:

```javascript
import { Modal } from 'react-native';

<Modal
  visible={isVisible}
  onRequestClose={() => setIsVisible(false)}
  animationType="slide"
>
  <View>
    <Text>Modal Content</Text>
    <Button title="Close" onPress={() => setIsVisible(false)} />
  </View>
</Modal>
```

2. Use transparent prop with a backdrop Pressable:

```javascript
<Modal
  visible={isVisible}
  transparent
  onRequestClose={() => setIsVisible(false)}
>
  <Pressable
    style={{ flex: 1, backgroundColor: 'rgba(0,0,0,0.5)' }}
    onPress={() => setIsVisible(false)}
  >
    <View style={{ marginTop: 200 }}>
      <Text>Content</Text>
    </View>
  </Pressable>
</Modal>
```

## Examples

```javascript
// Error: Android back button does not close modal
// Fix: add onRequestClose
<Modal visible={open} onRequestClose={() => setOpen(false)}>
  <Text>Hello</Text>
</Modal>
```

## Related Errors

- [Navigation Error]({{< relref "/frameworks/react-native/rn-navigation-error" >}})
