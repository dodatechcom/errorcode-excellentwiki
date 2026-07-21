---
title: "Broadcast Receiver Not Registered"
description: "Fix BroadcastReceiver registration errors in Android manifest declarations"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App cannot receive broadcasts because receiver is not properly declared

## Common Causes

- Receiver not declared in manifest for implicit broadcasts
- Wrong intent-filter action in receiver declaration
- Receiver class name does not match actual class
- API 26+ restrictions on implicit broadcast receivers

## Fixes

- Declare receiver in manifest for implicit broadcasts
- Use registerReceiver() for runtime-registered receivers
- Verify action strings match expected broadcast actions
- Check API level restrictions on broadcast types

## Code Example

```kotlin
<!-- Static registration -->
<receiver android:name=".MyReceiver"
    android:exported="false">
    <intent-filter>
        <action android:name="com.example.MY_ACTION" />
    </intent-filter>
</receiver>
```

# Dynamic registration (preferred for most cases)
val filter = IntentFilter("com.example.MY_ACTION")
registerReceiver(MyReceiver(), filter)
