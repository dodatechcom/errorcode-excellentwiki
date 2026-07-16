---
title: "Network request failed"
description: "React Native fetch or XMLHttpRequest fails with a network connectivity error"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["network", "fetch", "connectivity", "offline", "http"]
weight: 5
---

This error occurs when a network request fails in React Native due to connectivity issues, invalid URLs, or SSL certificate problems. The `fetch` API throws a `TypeError` with the message "Network request failed".

## Common Causes

- Device has no internet connection
- Invalid or unreachable URL (e.g. localhost on a real device)
- SSL certificate issues (self-signed certs on Android)
- iOS App Transport Security blocking HTTP requests

## How to Fix

1. Handle network errors in fetch calls:

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (error) {
    if (error.message === 'Network request failed') {
      console.log('No internet connection');
    }
    throw error;
  }
}
```

2. Allow HTTP requests in iOS (development only):

```xml
<!-- ios/YourApp/Info.plist -->
<key>NSAppTransportSecurity</key>
<dict>
  <key>NSAllowsLocalNetworking</key>
  <true/>
</dict>
```

3. Allow cleartext traffic on Android:

```xml
<!-- android/app/src/main/AndroidManifest.xml -->
<application
  android:usesCleartextTraffic="true"
  ...>
```

4. Add a network status check before requests:

```javascript
import NetInfo from '@react-native-community/netinfo';

const state = await NetInfo.fetch();
if (!state.isConnected) {
  Alert.alert('Offline', 'Please check your internet connection');
  return;
}
```

## Examples

```javascript
fetch('http://10.0.2.2:3000/api') // Works on Android emulator, not on real device
  .then(res => res.json())
  .catch(err => console.log(err));
// TypeError: Network request failed
```

## Related Errors

- [Gradle/Xcode build error]({{< relref "/frameworks/react-native/build-error5" >}})
