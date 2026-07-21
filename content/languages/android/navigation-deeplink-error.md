---
title: "Navigation Deep Link Error"
description: "Fix Android Navigation deep link configuration and handling errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Deep links do not open the correct screen or fail to navigate

## Common Causes

- Deep link URI pattern does not match intent filter
- Arguments not parsed from deep link URI
- Deep link action not defined in nav graph
- App Links not verified for domain

## Fixes

- Define deep link in navigation XML with app:uri
- Add matching intent-filter in manifest
- Parse URI arguments in destination Fragment
- Verify App Links with Digital Asset Links

## Code Example

```kotlin
<!-- nav_graph.xml -->
<fragment
    android:id="@+id/detailFragment"
    android:name="com.example.DetailFragment">
    <deepLink
        app:uri="myapp://detail/{itemId}" />
    <argument
        android:name="itemId"
        app:argType="long" />
</fragment>
```

<!-- Manifest intent-filter -->
<activity android:name=".MainActivity" android:exported="true">
    <intent-filter android:autoVerify="true">
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="myapp"
              android:host="detail" />
    </intent-filter>
</activity>
