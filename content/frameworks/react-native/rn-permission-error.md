---
title: "Permission - camera/storage denied"
description: "React Native app receives permission denied error when accessing camera, storage, or other device features"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["permission", "camera", "storage", "android", "ios", "grant"]
weight: 5
---

The permission denied error occurs when React Native apps try to access device features like camera or storage without the proper platform permissions. On both Android and iOS, apps must request permissions at runtime before accessing protected resources.

## Common Causes

- Missing permission declarations in `AndroidManifest.xml` or `Info.plist`
- Not requesting permission at runtime before accessing the feature
- User explicitly denied the permission request
- Permission rationale not provided before requesting
- Using deprecated permission APIs on newer OS versions

## How to Fix

1. Declare permissions in `android/app/src/main/AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

2. Declare permissions in `ios/YourApp/Info.plist`:

```xml
<key>NSCameraUsageDescription</key>
<string>We need camera access to take photos</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>We need storage access to save photos</string>
```

3. Request permission at runtime with `react-native-permissions`:

```javascript
import { check, request, PERMISSIONS, RESULTS } from 'react-native-permissions';

const requestCamera = async () => {
  const result = await check(
    Platform.OS === 'ios'
      ? PERMISSIONS.IOS.CAMERA
      : PERMISSIONS.ANDROID.CAMERA
  );

  if (result === RESULTS.DENIED) {
    return await request(
      Platform.OS === 'ios'
        ? PERMISSIONS.IOS.CAMERA
        : PERMISSIONS.ANDROID.CAMERA
    );
  }
  return result;
};
```

4. Handle the denied case gracefully:

```javascript
const handleCameraPress = async () => {
  const status = await requestCamera();
  if (status === RESULTS.GRANTED) {
    openCamera();
  } else {
    Alert.alert(
      'Permission Required',
      'Camera access is needed to take photos'
    );
  }
};
```

## Examples

```javascript
// Error: Camera permission denied
import { launchCamera } from 'react-native-image-picker';

const takePhoto = () => {
  launchCamera({ mediaType: 'photo' }, (response) => {
    if (response.errorCode === 'permission') {
      console.error('Camera permission denied');
    }
  });
};
```

## Related Errors

- [Platform error]({{< relref "/frameworks/react-native/native-module-error" >}})
- [Network error]({{< relref "/frameworks/react-native/rn-network-error" >}})
