---
title: "[Solution] Swift Error — APNS Error"
description: "Fix Swift APNS (Apple Push Notification service) errors. Learn about push notification registration failures, token issues, and notification handling."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["apns", "push-notification", "remote-notification", "token", "notification"]
weight: 5
---

# APNS Error

APNS errors occur when registering for or receiving Apple Push Notification service. Common issues include missing entitlements, invalid device tokens, and certificate problems.

## Description

APNS is Apple's service for delivering push notifications to iOS, macOS, and other Apple devices. Errors can occur during token registration, token delivery, or notification handling. Production vs development certificates and sandbox vs production environments must match.

Common patterns:

- **Missing entitlement** — app not configured for push notifications.
- **Wrong certificate/environment** — production certificate used with sandbox.
- **Token issues** — stale or invalid device tokens.
- **Background refresh** — push notification not arriving in background.

## Common Causes

```swift
// Cause 1: Not requesting notification permissions
func application(_ application: UIApplication,
                 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // Missing: UNUserNotificationCenter setup
    // Missing: application.registerForRemoteNotifications()
    return true
}

// Cause 2: Wrong delegate method
func application(_ application: UIApplication,
                 didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    // Must send token to server
}

func application(_ application: UIApplication,
                 didFailToRegisterForRemoteNotificationsWithError error: Error) {
    print("APNS registration failed: \(error)")
}

// Cause 3: Development vs production mismatch
// Using development certificate with production APNS server

// Cause 4: Missing notification categories/handlers
func userNotificationCenter(_ center: UNUserNotificationCenter,
                             willPresent notification: UNNotification,
                             withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
    completionHandler([.banner, .sound]) // Must call completionHandler
}
```

## How to Fix

### Fix 1: Set up push notification registration properly

```swift
import UserNotifications

func application(_ application: UIApplication,
                 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    let center = UNUserNotificationCenter.current()
    center.delegate = self
    center.requestAuthorization(options: [.alert, .sound, .badge]) { granted, error in
        if let error = error {
            print("Authorization error: \(error)")
        }
        if granted {
            DispatchQueue.main.async {
                application.registerForRemoteNotifications()
            }
        }
    }
    return true
}
```

### Fix 2: Handle registration results

```swift
func application(_ application: UIApplication,
                 didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    let token = deviceToken.map { String(format: "%02.2hhx", $0) }.joined()
    // Send token to your server
    sendTokenToServer(token)
}

func application(_ application: UIApplication,
                 didFailToRegisterForRemoteNotificationsWithError error: Error) {
    print("Failed to register: \(error.localizedDescription)")
}
```

### Fix 3: Handle incoming notifications

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                             didReceive response: UNNotificationResponse,
                             withCompletionHandler completionHandler: @escaping () -> Void) {
    let userInfo = response.notification.request.content.userInfo
    // Process notification data
    completionHandler()
}

func userNotificationCenter(_ center: UNUserNotificationCenter,
                             willPresent notification: UNNotification,
                             withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
    completionHandler([.banner, .sound])
}
```

### Fix 4: Ensure entitlements and provisioning profile

```swift
// Verify in Xcode:
// 1. Target > Signing & Capabilities > + Push Notifications
// 2. Provisioning profile includes Push Notification capability
// 3. APNS certificate matches environment (sandbox/production)
```

## Examples

```swift
// Example 1: Forgetting to register
func application(_ application: UIApplication,
                 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // No push notification registration at all
    return true
}

// Example 2: Wrong token format
let token = deviceToken.description // Wrong: includes angle brackets
// Correct: use map with format string
```

## Related Errors

- [CloudKit Error]({{< relref "/languages/swift/cloudkit-error" >}}) — iCloud-related push issues.
- [Keychain Error]({{< relref "/languages/swift/keychain-error" >}}) — token storage issues.
- [URLError]({{< relref "/languages/swift/url-session-error" >}}) — network errors affecting token delivery.
