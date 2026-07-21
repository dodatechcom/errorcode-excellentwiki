---
title: "Broadcast Permission Error"
description: "Fix Android broadcast permission and security configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Broadcast receiver cannot send or receive because of permission restrictions

## Common Causes

- Sending broadcast without required permission
- Receiver requires permission not declared by sender
- Exported receiver accessible by malicious apps
- Permission not declared in manifest

## Fixes

- Declare required permission on receiver in manifest
- Send broadcast with permission parameter
- Set exported=false for internal receivers
- Use signature-level permission for app-to-app broadcasts

## Code Example

```kotlin
<!-- Receiver with permission requirement -->
<receiver android:name=".SecureReceiver"
    android:permission="com.example.SEND_SECURE"
    android:exported="false">
    <intent-filter>
        <action android:name="com.example.SECURE_ACTION" />
    </intent-filter>
</receiver>

// Send with permission:
val intent = Intent("com.example.SECURE_ACTION")
sendBroadcast(intent, "com.example.SEND_SECURE")
```

# Use signature permission for inter-app security
# Set exported=false for app-internal receivers
# Always specify permission when sending broadcasts
