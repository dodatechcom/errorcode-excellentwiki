---
title: "[Solution] Core Location Authorization Denied Error"
description: "Fix Core Location authorization denied errors preventing location access in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Core Location Authorization Denied Error

Location authorization is denied when the user denies permission or when the app lacks required Info.plist location usage descriptions.

## Common Causes
- Missing NSLocationWhenInUseUsageDescription in Info.plist
- User denied location permission
- Always authorization requested without proper justification
- Location services disabled globally on device

## How to Fix
1. Add required usage description strings to Info.plist
2. Request authorization before using location services
3. Handle the denied authorization state gracefully
4. Direct users to Settings if permission is denied

```swift
// Request location authorization:
let locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()

// Check authorization status:
switch locationManager.authorizationStatus {
case .authorizedWhenInUse: break // OK
case .denied: break // Show settings prompt
case .notDetermined: locationManager.requestWhenInUseAuthorization()
default: break
}
```

## Examples
```swift
// CLLocationManagerDelegate implementation:
func locationManagerDidChangeAuthorization(_ manager: CLLocationManager) {
    switch manager.authorizationStatus {
    case .authorizedWhenInUse, .authorizedAlways:
        manager.startUpdatingLocation()
    case .denied, .restricted:
        showLocationDeniedAlert()
    case .notDetermined:
        manager.requestWhenInUseAuthorization()
    @unknown default: break
    }
}
```
