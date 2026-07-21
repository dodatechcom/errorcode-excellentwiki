---
title: "Android 14 Implicit Intent Error"
description: "Fix Android 14 implicit intent restrictions and package visibility errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Implicit intents fail on Android 14 because of security restrictions

## Common Causes

- Implicit broadcast receivers restricted further
- Package visibility filtering blocking intent resolution
- PendingIntent mutability requirements stricter
- Intent flags not compatible with Android 14

## Fixes

- Use explicit intents with component name
- Add queries element for package visibility
- Use PendingIntent.FLAG_IMMUTABLE
- Check target SDK compatibility

## Code Example

```kotlin
<!-- Package visibility -->
<queries>
    <intent>
        <action android:name="android.intent.action.SEND" />
        <data android:mimeType="text/plain" />
    </intent>
    <package android:name="com.example.target" />
</queries>

// Explicit intent:
val intent = Intent(this, SpecificActivity::class.java)
intent.putExtra("key", "value")
startActivity(intent)
```

# Implicit intents increasingly restricted
# Use explicit intents when possible
# Declare package visibility in manifest
