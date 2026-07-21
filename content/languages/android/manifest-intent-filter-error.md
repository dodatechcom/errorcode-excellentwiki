---
title: "Intent Filter Configuration Error"
description: "Fix intent filter configuration errors in Android manifest for deep links"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App cannot handle intents because intent filter is incorrectly configured

## Common Causes

- Missing action, category, or data tag in intent filter
- Intent filter placed outside correct activity
- exported attribute not set for API 31+
- Data scheme or host not matching expected deep link

## Fixes

- Verify intent filter has action + category minimum
- Set android:exported=true for activities with intent filters
- Match data scheme to actual URI format
- Use App Links Assistant in Android Studio

## Code Example

```kotlin
<activity android:name=".ShareActivity"
    android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.SEND" />
        <category android:name="android.intent.category.DEFAULT" />
        <data android:mimeType="text/plain" />
    </intent-filter>
</activity>
```

# For deep links, add data tags:
<intent-filter android:autoVerify="true">
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data android:scheme="https"
          android:host="example.com"
          android:pathPrefix="/share" />
</intent-filter>
