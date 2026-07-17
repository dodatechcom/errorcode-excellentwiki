---
title: "Flipper - plugin load error"
description: "Flipper fails to load plugins or connect to the React Native app, preventing debugging and inspection"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A Flipper plugin load error occurs when the Flipper desktop app cannot load its plugins or establish a connection with the React Native app. This prevents access to debugging tools like the network inspector, database viewer, and layout inspector.

## Common Causes

- Flipper version mismatch between desktop app and mobile SDK
- Flipper server not running or crashed
- Network connection between desktop and device lost
- Plugin requires native code that was not built
- Flipper cache corruption

## How to Fix

1. Ensure Flipper is up to date:

```bash
# Update Flipper desktop app
# Download latest from https://fbflipper.com/

# Update mobile SDK in package.json
npm install flipper-plugin react-native-flipper@latest
```

2. Clear Flipper cache:

```bash
rm -rf ~/.flipper
# Restart Flipper desktop app
```

3. Enable Flipper in `android/app/build.gradle`:

```gradle
dependencies {
  debugImplementation('com.facebook.flipper:flipper:${FLIPPER_VERSION}')
}
```

4. Initialize Flipper in your app:

```javascript
import { useEffect } from 'react';

if (__DEV__) {
  const connectToFlipper = async () => {
    try {
      await import('react-native-flipper');
    } catch (e) {
      console.warn('Flipper not available:', e);
    }
  };
  connectToFlipper();
}
```

5. Verify Flipper connection from desktop app:

```bash
# Check if Flipper server is running
netstat -an | grep 8088
```

## Examples

```bash
# Flipper desktop shows "No devices connected"
# Check that the app is running in debug mode
adb reverse tcp:8088 tcp:8088
```

```javascript
// Flipper plugin error in console
// Error: Plugin 'databases' failed to load
// Fix: ensure debug build with Flipper support
```

## Related Errors

- [Network error]({{< relref "/frameworks/react-native/rn-network-error" >}})
- [Storage error]({{< relref "/frameworks/react-native/rn-storage-error" >}})
