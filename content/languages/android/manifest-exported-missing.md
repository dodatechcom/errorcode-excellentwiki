---
title: "Missing Exported Attribute"
description: "Fix missing android:exported attribute error for activities and services"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build fails because activity or service with intent-filter lacks android:exported

## Common Causes

- API 31+ requires explicit exported attribute
- Intent-filter present but exported not set
- Exported attribute missing on BroadcastReceiver
- Service with intent-filter needs exported flag

## Fixes

- Add android:exported="true" or "false" to each component
- Set exported=true only if component should be externally accessible
- Apply to all activities, services, and receivers with intent-filters
- Review merger report for all affected components

## Code Example

```kotlin
<!-- Required for API 31+ -->
<activity android:name=".MainActivity"
    android:exported="true">
    <intent-filter>...</intent-filter>
</activity>

<activity android:name=".InternalActivity"
    android:exported="false" />
```

# Quick fix: add exported to all components
# with intent-filters in your manifest
