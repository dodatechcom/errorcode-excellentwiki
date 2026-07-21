---
title: "[Solution] React Native Push Notifications iOS APNs Error"
description: "react-native iOS push notifications fail to register with Apple Push Notification service or device token is null on iOS simulators"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The iOS push notification error occurs when the APNs registration fails or the device token comes back as nil. iOS push notifications require proper provisioning profiles, entitlements, and are not available on simulators (except for iOS 16+ simulators with specific setup).

## Common Causes

- App does not have the Push Notifications capability enabled in Xcode
- Running on iOS simulator (< 16) which does not support APNs
- Missing aps-environment entitlement in provisioning profile
- @react-native-firebase/messaging on iOS without APNs certificate uploaded to Firebase
- UNUserNotificationCenter delegate not set before registerForRemoteNotifications
- App transport security blocking the APNs connection

## How to Fix

1. Enable push capability in Xcode:

```bash
# Open ios/YourApp.xcworkspace
# Select the target -> Signing & Capabilities -> + Capability -> Push Notifications
```

2. Register for notifications after requesting permission:

```javascript
import { Platform } from 'react-native';
import messaging from '@react-native-firebase/messaging';

async function requestPermission() {
  const authStatus = await messaging().requestPermission();
  const enabled =
    authStatus === messaging.AuthorizationStatus.AUTHORIZED ||
    authStatus === messaging.AuthorizationStatus.PROVISIONAL;

  if (enabled) {
    const token = await messaging().getToken();
    console.log('FCM Token:', token);
  }
}
```

3. Use a real device or configure simulator for iOS 16+:

```bash
# iOS 16+ simulators support push via xcrun
xcrun simctl push booted com.myapp payload.apns
```

## Examples

```javascript
// Error: "Registering for remote notifications failed: no valid aps-environment entitlement"
// Fix: enable Push Notifications in Xcode capabilities
```

## Related Errors

- [Push Notification Error]({{< relref "/frameworks/react-native/rn-push-notification-error" >}})
