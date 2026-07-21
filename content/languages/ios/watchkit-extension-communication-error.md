---
title: "[Solution] WatchKit Extension Communication Error"
description: "Fix communication errors between iOS app and WatchKit extension."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# WatchKit Extension Communication Error

Watch-to-phone communication fails when WatchConnectivity session is not properly activated or when message payloads exceed size limits.

## Common Causes
- WCSession not activated on either side
- Message payload too large (context transfer limit)
- Both sides not running simultaneously
- Reply handler not implemented for expecting replies

## How to Fix
1. Activate WCSession on both iOS and watchOS
2. Keep message payloads under 60KB
3. Use transferUserInfo for large data
4. Implement reply handlers when expecting responses

```swift
// Activate session on both platforms:
if WCSession.isSupported() {
    let session = WCSession.default
    session.delegate = self
    session.activate()
}
```

## Examples
```swift
// Send message with reply:
if WCSession.default.isReachable {
    WCSession.default.sendMessage(["command": "refresh"], replyHandler: { reply in
        print("Reply: \(reply)")
    }, errorHandler: { error in
        print("Send failed: \(error)")
    })
}

// Transfer large data:
WCSession.default.transferUserInfo(["largeData": data])
```
