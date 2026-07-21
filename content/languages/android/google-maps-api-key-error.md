---
title: "Maps API Key Error"
description: "Fix Google Maps API key configuration errors in Android manifest"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Google Maps fragment fails to load because API key is missing or invalid

## Common Causes

- Meta-data API key not in manifest
- Wrong API key for current project
- API restrictions on key do not include Maps SDK
- Package name not authorized for key

## Fixes

- Add com.google.android.geo.API_KEY to manifest meta-data
- Generate correct key in Google Cloud Console
- Enable Maps SDK for Android in Cloud Console
- Add package name fingerprint to key restrictions

## Code Example

```kotlin
<!-- AndroidManifest.xml -->
<application>
    <meta-data
        android:name="com.google.android.geo.API_KEY"
        android:value="YOUR_API_KEY" />
</application>
```

# Get API key:
# 1. Google Cloud Console > APIs & Services > Credentials
# 2. Create API key
# 3. Enable Maps SDK for Android
# 4. Add app SHA-1 and package name restrictions
