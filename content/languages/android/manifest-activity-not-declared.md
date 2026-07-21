---
title: "Activity Not Declared in Manifest"
description: "Fix Android activity not declared in manifest errors when launching activities"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App crashes because the activity class was not registered in AndroidManifest.xml

## Common Causes

- Forgot to add activity tag in manifest
- Activity declared in wrong module manifest
- Activity in library module not merged correctly
- Typo in activity class name in manifest

## Fixes

- Add <activity> tag inside <application> in manifest
- Verify class name matches actual activity class
- Check manifest merger output for conflicts
- Use fully qualified class name

## Code Example

```kotlin
<!-- AndroidManifest.xml -->
<application ...>
    <activity
        android:name=".MainActivity"
        android:exported="true">
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
    </activity>
    <!-- Add new activity here -->
    <activity android:name=".DetailActivity" />
</application>
```

# Find the activity class package
grep -r "class DetailActivity" app/src/
# Then add matching entry to manifest
