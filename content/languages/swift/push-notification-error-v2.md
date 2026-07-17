---
title: "[Solution] APNs Device Token Error Fix"
description: "Fix Apple Push Notification device token errors when registration fails."
languages: ["swift"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["APNs", "push-notification", "device-token", "remote-notification", "swift"]
weight: 5
---

# APNs: Device Token Error Fix

An APNs device token error occurs when the app fails to register for push notifications or the device token is invalid.

## What This Error Means

Apple Push Notification service requires a valid device token to send notifications. Errors occur when registration is denied, the token isn't passed to your server correctly, or the token is invalidated.

## Common Causes

- User denied notification permission
- Device token not sent to server
- Token is stale or invalidated
- Wrong APNs environment (development vs production)
- Missing push notification entitlement

## How to Fix

### 1. Register for remote notifications

```swift
// CORRECT: Register for push notifications
func registerForNotifications() {
    UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .badge, .sound]) { granted, error in
        if granted {
            DispatchQueue.main.async {
                UIApplication.shared.registerForRemoteNotifications()
            }
        }
    }
}
```

### 2. Handle device token registration

```swift
// CORRECT: Handle successful registration
func application(_ application: UIApplication,
                 didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    let token = deviceToken.map { String(format: "%02.2hhx", $0) }.joined()
    print("Device Token: \(token)")

    // Send token to your server
    APIService.registerDevice(token: token)
}

// Handle failure
func application(_ application: UIApplication,
                 didFailToRegisterForRemoteNotificationsWithError error: Error) {
    print("Failed to register: \(error)")
}
```

### 3. Validate token with server

```swift
// CORRECT: Send token to backend
func registerDevice(token: String) {
    var request = URLRequest(url: serverURL)
    request.httpMethod = "POST"
    request.httpBody = try? JSONEncoder().encode(["token": token])
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    URLSession.shared.dataTask(with: request) { _, response, error in
        if let error = error {
            print("Token registration failed: \(error)")
        }
    }.resume()
}
```

### 4. Handle token refresh

```swift
// CORRECT: Handle token updates (iOS 13+)
func application(_ application: UIApplication,
                 didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    // Token may update — always send latest to server
    let token = deviceToken.map { String(format: "%02.2hhx", $0) }.joined()
    sendTokenToServer(token)
}
```

## Related Errors

- [Push Notification Error]({{< relref "/languages/swift/push-notification" >}}) — general notification errors
- [CloudKit Error](cloudkit-error-v2) — CloudKit issues
- [HealthKit Error](healthkit-error-v2) — HealthKit authorization
