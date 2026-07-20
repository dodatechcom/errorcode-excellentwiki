---
title: "[Solution] Flutter Location Error — permission, accuracy, background location"
description: "Fix Flutter location plugin errors from permission requests, GPS accuracy settings, and background location issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 191
---

Location errors occur when location permissions are denied, GPS accuracy is too low, or background location access is not configured.

## Common Causes

1. Location permission not requested or denied by user.
2. GPS disabled on the device.
3. Background location permission not requested separately.
4. Accuracy settings too high for indoor use.
5. Location services timing out on weak signal.

## How to Fix It

**Solution 1: Request location permission and get position**

```dart
import 'package:geolocator/geolocator.dart';

Future<Position?> getCurrentLocation() async {
  bool serviceEnabled = await Geolocator.isLocationServiceEnabled();
  if (!serviceEnabled) {
    print('Location services disabled');
    return null;
  }
  
  LocationPermission permission = await Geolocator.checkPermission();
  if (permission == LocationPermission.denied) {
    permission = await Geolocator.requestPermission();
    if (permission == LocationPermission.denied) {
      print('Permission denied');
      return null;
    }
  }
  
  if (permission == LocationPermission.deniedForever) {
    print('Permission permanently denied');
    return null;
  }
  
  return await Geolocator.getCurrentPosition(
    desiredAccuracy: LocationAccuracy.high,
  );
}
```

**Solution 2: Stream location updates**

```dart
import 'package:geolocator/geolocator.dart';

class LocationTracker {
  StreamSubscription<Position>? _subscription;
  
  void startTracking() {
    _subscription = Geolocator.getPositionStream(
      locationSettings: LocationSettings(
        accuracy: LocationAccuracy.high,
        distanceFilter: 10, // Update every 10 meters
      ),
    ).listen((Position position) {
      print('Lat: ${position.latitude}, Lng: ${position.longitude}');
    });
  }
  
  void stopTracking() {
    _subscription?.cancel();
    _subscription = null;
  }
}
```

**Solution 3: Handle background location permission**

```dart
import 'package:geolocator/geolocator.dart';
import 'package:permission_handler/permission_handler.dart';

Future<void> requestBackgroundLocation() async {
  // Request foreground first
  LocationPermission permission = await Geolocator.requestPermission();
  
  if (permission == LocationPermission.whileInUse ||
      permission == LocationPermission.always) {
    // Request background permission (Android 10+)
    if (await Permission.locationAlways.isDenied) {
      await Permission.locationAlways.request();
    }
  }
}
```

**Solution 4: Calculate distance between points**

```dart
import 'package:geolocator/geolocator.dart';

double calculateDistance(double lat1, double lon1, double lat2, double lon2) {
  return Geolocator.distanceBetween(lat1, lon1, lat2, lon2);
}

void main() {
  double distance = calculateDistance(
    37.7749, -122.4194, // San Francisco
    34.0522, -118.2437, // Los Angeles
  );
  
  print('Distance: ${(distance / 1000).toStringAsFixed(1)} km');
}
```

**Solution 5: Check and open location settings**

```dart
import 'package:geolocator/geolocator.dart';

Future<void> ensureLocationEnabled() async {
  bool serviceEnabled = await Geolocator.isLocationServiceEnabled();
  
  if (!serviceEnabled) {
    // Open location settings
    await Geolocator.openLocationSettings();
    
    // Re-check after returning from settings
    serviceEnabled = await Geolocator.isLocationServiceEnabled();
    if (!serviceEnabled) {
      throw Exception('Location services are required');
    }
  }
}
```

## Examples

Add `geolocator: ^10.1.0` to `pubspec.yaml`. On iOS, add `NSLocationWhenInUseUsageDescription` and optionally `NSLocationAlwaysUsageDescription` to `Info.plist`.

## Related Errors

- [Flutter Permission Error](/languages/dart/flutter-permission-error/)
- [Flutter Camera Error](/languages/dart/flutter-camera-error/)
- [Flutter Connectivity Error](/languages/dart/flutter-connectivity-error/)
