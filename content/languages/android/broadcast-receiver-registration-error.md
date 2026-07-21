---
title: "Broadcast Receiver Registration Error"
description: "Fix Android BroadcastReceiver registration and intent filter errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
BroadcastReceiver does not receive broadcasts because of registration issues

## Common Causes

- Receiver not registered in manifest for implicit broadcasts
- Dynamic receiver not unregistered causing leak
- Intent filter action does not match sent broadcast
- API 26+ restrictions on implicit broadcast receivers

## Fixes

- Register implicit broadcast receivers in manifest
- Unregister dynamic receivers in onStop/onDestroy
- Use exact action string matching
- Use LocalBroadcastManager for in-app broadcasts

## Code Example

```kotlin
<!-- Manifest registration for implicit broadcasts -->
<receiver android:name=".BootReceiver"
    android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.BOOT_COMPLETED" />
    </intent-filter>
</receiver>

// Dynamic registration (preferred for most cases):
val filter = IntentFilter("com.example.MY_ACTION")
val receiver = MyReceiver()
registerReceiver(receiver, filter)

// Always unregister:
override fun onStop() {
    super.onStop()
    unregisterReceiver(receiver)
}
```

# Implicit broadcasts restricted in API 26+
# Use WorkManager for most background triggers
# Use LocalBroadcastManager for in-app only
