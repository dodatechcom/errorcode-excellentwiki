---
title: "ContentProvider Permission Error"
description: "Fix Android ContentProvider permission and URI grant errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ContentProvider access fails because of missing permissions or URI grants

## Common Causes

- ContentProvider not exported but client tries to access
- Write permission not declared in provider tag
- URI grant flags not properly configured
- Permission level not sufficient for client app

## Fixes

- Set android:exported=true if provider needs external access
- Add android:writePermission or android:readPermission
- Use FLAG_GRANT_READ_URI_PERMISSION for temporary access
- Use android:permission for fine-grained control

## Code Example

```kotlin
<!-- AndroidManifest.xml -->
<provider
    android:name=".MyProvider"
    android:authorities="com.example.provider"
    android:exported="true"
    android:readPermission="com.example.READ_DATA"
    android:writePermission="com.example.WRITE_DATA" />

<!-- Client requesting access: -->
<uses-permission android:name="com.example.READ_DATA" />

// Or grant URI permission temporarily:
intent.flags = Intent.FLAG_GRANT_READ_URI_PERMISSION
contentResolver.query(uri, ...)
```

# Provider permissions declared in manifest
# Client must declare matching uses-permission
# URI grants are temporary and per-URI
