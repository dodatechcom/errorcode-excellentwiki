---
title: "[Solution] Push Notification Device Token Error"
description: "Fix push notification device token registration failures in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Push Notification Device Token Error

Token registration fails when the app does not properly request notification permissions or the token is not sent to the server correctly.

## Common Causes
- APNS entitlement missing from provisioning profile
- User denied notification permissions
- Token not properly converted to hex string
- Wrong APNS environment (development vs production)

## How to Fix
1. Ensure push notification entitlement is enabled
2. Request authorization before registering
3. Convert device token Data to hex string properly
4. Use correct APNS environment for your build

```swift
// Register for notifications:
UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .badge, .sound]) { granted, error in
    if granted {
        DispatchQueue.main.async {
            UIApplication.shared.registerForRemoteNotifications()
        }
    }
}

// Handle token:
func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    let token = deviceToken.map { String(format: "%02.2hhx", $0) }.joined()
    print("Device Token: \(token)")
}
```

## Examples
```swift
// Token conversion patterns:
extension Data {
    var hexString: String {
        map { String(format: "%02.2hhx", $0) }.joined()
    }
}

// Or use Array:
let tokenParts = deviceToken.map { data in
    String(format: "%02.2hhx", data)
}
let token = tokenParts.joined()
```
