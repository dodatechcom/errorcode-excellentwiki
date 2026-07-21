---
title: "[Solution] React Native Background Thread Operation Error"
description: "react-native UI updates dispatched from a background thread causing native module callback failures or silent crashes on Android and iOS in React Native apps"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The Background Thread error occurs when a native module callback or a worklet attempts to update the React Native UI from a non-main thread. On Android this surfaces as a CalledFromWrongThreadException, while on iOS it may cause silent view hierarchy corruption.

## Common Causes

- Native module callback invoked from a background queue
- Using setTimeout or setInterval inside a worklet thread in Reanimated
- Dispatching setState after a network call completes on a background thread
- AsyncStorage multiGet callback executing on a worker pool thread
- Calling NativeModules from a non-JS thread without dispatching

## How to Fix

1. Dispatch UI updates to the main thread in native modules:

```objectivec
// iOS: ensure callback on main thread
dispatch_async(dispatch_get_main_queue(), ^{
  self.onProgress(@{ @"progress": @(percentage) });
});
```

2. For Android, use runOnUiThread:

```java
// Android
new Handler(Looper.getMainLooper()).post(() -> {
  promise.resolve(result);
});
```

## Examples

```java
// Error: android.view.ViewRootImpl$CalledFromWrongThreadException
// Only the original thread that created a view hierarchy can touch its views.

// Fix:
runOnUiThread(new Runnable() {
  @Override
  public void run() {
    reactContext.getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)
      .emit("onProgress", data);
  }
});
```

## Related Errors

- [Native Module Error]({{< relref "/frameworks/react-native/rn-native-module-error-rn" >}})
