---
title: "[Solution] Flutter Permission Error — permission_handler, request, open settings"
description: "Fix Flutter permission errors from permission_handler plugin, request flow, settings navigation, and platform-specific config."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 192
---

Permission errors occur when permissions are not properly requested, denied by the user, or platform-specific configuration is missing.

## Common Causes

1. Permission not requested before accessing the feature.
2. `PermissionStatus.deniedForever` not being handled.
3. Missing platform-specific permission declarations.
4. Requesting permission during build instead of on user action.
5. Not checking `isRestricted` on iOS.

## How to Fix It

**Solution 1: Request permission with status handling**

```dart
import 'package:permission_handler/permission_handler.dart';

Future<void> requestCameraPermission() async {
  PermissionStatus status = await Permission.camera.status;
  
  if (status.isGranted) {
    print('Already granted');
    return;
  }
  
  if (status.isPermanentlyDenied) {
    // Open app settings
    await openAppSettings();
    return;
  }
  
  status = await Permission.camera.request();
  
  if (status.isGranted) {
    print('Permission granted');
  } else if (status.isPermanentlyDenied) {
    print('Please enable camera in settings');
  } else {
    print('Permission denied');
  }
}
```

**Solution 2: Request multiple permissions**

```dart
import 'package:permission_handler/permission_handler.dart';

Future<void> requestMultiplePermissions() async {
  Map<Permission, PermissionStatus> statuses = await [
    Permission.camera,
    Permission.microphone,
    Permission.storage,
  ].request();
  
  statuses.forEach((permission, status) {
    print('$permission: $status');
  });
}
```

**Solution 3: Handle permanent denial**

```dart
import 'package:permission_handler/permission_handler.dart';

void handlePermission(Permission permission) async {
  if (await permission.isGranted) {
    // Proceed
    return;
  }
  
  if (await permission.isPermanentlyDenied) {
    // Show dialog explaining why permission is needed
    // Then open settings
    await openAppSettings();
    return;
  }
  
  // Request permission
  PermissionStatus status = await permission.request();
  
  if (status.isGranted) {
    // Proceed
  } else if (status.isPermanentlyDenied) {
    await openAppSettings();
  }
}
```

**Solution 4: Check permission status without requesting**

```dart
import 'package:permission_handler/permission_handler.dart';

void checkPermissions() async {
  // Check without requesting
  PermissionStatus cameraStatus = await Permission.camera.status;
  PermissionStatus locationStatus = await Permission.location.status;
  
  print('Camera: ${cameraStatus.isGranted}');
  print('Location: ${locationStatus.isGranted}');
  print('Location when in use: ${locationStatus.isLimited}');
}
```

**Solution 5: Platform-specific configuration**

```dart
// Android - AndroidManifest.xml:
// <uses-permission android:name="android.permission.CAMERA"/>
// <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
// <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>

// iOS - Info.plist:
// <key>NSCameraUsageDescription</key>
// <string>Camera access for taking photos</string>
// <key>NSLocationWhenInUseUsageDescription</key>
// <string>Location access for nearby features</string>

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // Check permissions early
  if (await Permission.camera.isGranted) {
    print('Camera ready');
  }
  
  runApp(MyApp());
}
```

## Examples

Add `permission_handler: ^10.4.0` to your `pubspec.yaml`. Each platform requires specific permission declarations in their manifest/plist files.

## Related Errors

- [Flutter Camera Error](/languages/dart/flutter-camera-error/)
- [Flutter Location Error](/languages/dart/flutter-location-error/)
- [Flutter Shared Preferences Error](/languages/dart/flutter-shared-preferences-error/)
