---
title: "[Solution] React Native Permission Denied Error — How to Fix"
description: "Fix React Native permission errors. Resolve Android and iOS permission requests and access denied issues."
frameworks: ["react-native"]
error-types: ["security-error"]
severities: ["error"]
weight: 5
comments: true
---

A React Native permission denied error occurs when the application requests access to device resources (camera, location, storage) and the user denies the request, or when permissions are not properly declared in the app manifest.

## Why It Happens

Both iOS and Android require explicit permission declarations. Errors occur when permissions are not listed in `AndroidManifest.xml` or `Info.plist`, when the permission request API is not called before accessing the resource, when the user permanently denies the permission, or when the `react-native-permissions` library is not properly configured.

## Common Error Messages

```
PERMISSION_DENIED: Location permission not granted
```

```
Camera not available: Permission denied
```

```
Error: Permissions not granted
```

```
Permission denied: Cannot access camera without permission
```

## How to Fix It

### 1. Declare Permissions in Manifests

Add required permissions:

```xml
<!-- android/app/src/main/AndroidManifest.xml -->
<manifest>
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    <uses-permission android:name="android.permission.READ_CONTACTS" />
</manifest>
```

```xml
<!-- ios/YourApp/Info.plist -->
<key>NSCameraUsageDescription</key>
<string>Camera access is needed to take photos</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>Photo library access is needed to upload images</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>Location access is needed for map features</string>
<key>NSMicrophoneUsageDescription</key>
<string>Microphone access is needed for audio recording</string>
```

### 2. Request Permissions at Runtime

Use `react-native-permissions`:

```typescript
import { Platform, PermissionsAndroid, Alert } from 'react-native';
import { check, request, PERMISSIONS, RESULTS } from 'react-native-permissions';

async function requestCameraPermission() {
    if (Platform.OS === 'android') {
        const granted = await PermissionsAndroid.request(
            PermissionsAndroid.PERMISSIONS.CAMERA,
            {
                title: 'Camera Permission',
                message: 'This app needs camera access to take photos',
                buttonPositive: 'Allow',
                buttonNegative: 'Deny',
            }
        );
        return granted === PermissionsAndroid.RESULTS.GRANTED;
    } else {
        const result = await request(PERMISSIONS.IOS.CAMERA);
        return result === RESULTS.GRANTED;
    }
}

async function checkAndRequestPermission() {
    const status = await check(PERMISSIONS.IOS.CAMERA);

    switch (status) {
        case RESULTS.GRANTED:
            return true;
        case RESULTS.DENIED:
            const result = await request(PERMISSIONS.IOS.CAMERA);
            return result === RESULTS.GRANTED;
        case RESULTS.BLOCKED:
            Alert.alert(
                'Permission Required',
                'Please enable camera permission in Settings',
                [{ text: 'OK' }]
            );
            return false;
        default:
            return false;
    }
}
```

### 3. Handle Permission Denied Gracefully

Provide fallback behavior:

```typescript
async function takePhoto() {
    const hasPermission = await requestCameraPermission();

    if (!hasPermission) {
        Alert.alert(
            'Permission Denied',
            'Camera access is required to take photos. Please enable it in Settings.',
            [
                { text: 'Cancel', style: 'cancel' },
                { text: 'Open Settings', onPress: () => Linking.openSettings() },
            ]
        );
        return;
    }

    // Proceed with camera
    const result = await launchCamera({ mediaType: 'photo' });
}
```

### 4. Use CameraRoll with Permissions

Access the photo library:

```typescript
import { CameraRoll } from '@react-native-camera-roll/camera-roll';

async function savePhoto(uri: string) {
    if (Platform.OS === 'ios') {
        const status = await request(PERMISSIONS.IOS.PHOTO_LIBRARY_ADD_ONLY);
        if (status !== RESULTS.GRANTED) return;
    }

    try {
        await CameraRoll.save(uri, { type: 'photo' });
    } catch (error) {
        console.error('Failed to save photo:', error);
    }
}
```

## Common Scenarios

**Scenario 1: Permission not requested on first launch.**
Call the permission request before using the feature, not on app startup.

**Scenario 2: Permission works in debug but not release.**
Check that debug builds use the same permission declarations as release builds.

**Scenario 3: "Permanently denied" permission.**
When a user selects "Don't ask again", the app must direct them to device settings.

## Prevent It

1. **Always check permissions before accessing device resources** and handle denial gracefully.

2. **Provide clear explanations** when requesting permissions to improve user acceptance.

3. **Use `react-native-permissions`** instead of the deprecated `PermissionsAndroid` and `Info.plist` manual approaches.
