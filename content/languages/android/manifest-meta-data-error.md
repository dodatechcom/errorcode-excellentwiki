---
title: "Meta Data Configuration Error"
description: "Fix Android manifest meta-data configuration errors for Firebase and APIs"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App crashes because manifest meta-data is missing or malformed

## Common Causes

- meta-data tag has wrong android:value type
- Required API key or config value not in manifest
- meta-data placed outside application tag
- Name attribute does not match expected key

## Fixes

- Verify required meta-data from SDK documentation
- Use correct value type: string, integer, boolean, or resource
- Place meta-data inside <application> tag
- Double-check name strings for typos

## Code Example

```kotlin
<application ...>
    <!-- Google Maps API Key -->
    <meta-data
        android:name="com.google.android.geo.API_KEY"
        android:value="YOUR_API_KEY" />
    <!-- Firebase config -->
    <meta-data
        android:name="com.google.gms.version"
        android:value="@integer/google_play_services_version" />
</application>
```

# Find required meta-data for each SDK:
# Firebase: google-services.json auto-adds it
# Maps: add geo.API_KEY
# Check build/intermediates/merged_manifests for output
