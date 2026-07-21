---
title: "App Links Verification Error"
description: "Fix App Links verification and deep link handling in Compose Navigation"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App Links not verified correctly or deep links not opening correct destination

## Common Causes

- Digital Asset Links not configured
- assetlinks.json not accessible
- Deep link intent not reaching Navigation
- Package fingerprint not matching

## Fixes

- Configure Digital Asset Links in Firebase or manually
- Host assetlinks.json on domain
- Use intent-filter with autoVerify=true
- Verify package fingerprint matches

## Code Example

```kotlin
<!-- AndroidManifest.xml -->
<activity android:name=".MainActivity" android:exported="true">
    <intent-filter android:autoVerify="true">
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="https"
              android:host="example.com"
              android:pathPrefix="/product" />
    </intent-filter>
</activity>

// Verify:
// https://example.com/.well-known/assetlinks.json
// Should contain your app's package and fingerprint
```

# autoVerify: trigger verification
# assetlinks.json: Digital Asset Links file
# Package + fingerprint must match
# Use Firebase App Links for easier setup
