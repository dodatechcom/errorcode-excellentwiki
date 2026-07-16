---
title: "[Solution] Swift Error — CLError"
description: "Fix Swift Core Location errors. Learn about CLError codes, location authorization, and how to handle location service failures."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["corelocation", "location", "gps", "authorization", "cllocation"]
weight: 5
---

# CLError

`CLError` is thrown by Core Location when location services fail, authorization is denied, or location data is unavailable. Each error has a specific `CLError.Code`.

## Description

Core Location provides device location data. Access requires user authorization (either "When In Use" or "Always") and enabled location services. `CLError` codes indicate specific failures like `.denied`, `.locationUnknown`, `.network`, and `.regionMonitoringDenied`.

Common patterns:

- **Authorization not requested** — starting location updates without requesting permission.
- **Authorization denied** — user declined location access.
- **Location services disabled** — device-wide location services turned off.
- **Background location** — requesting "Always" without proper entitlements.

## Common Causes

```swift
// Cause 1: Starting updates without authorization
let manager = CLLocationManager()
manager.startUpdatingLocation() // Fails silently without authorization

// Cause 2: Not checking authorization status
func locationManager(_ manager: CLLocationManager,
                     didFailWithError error: Error) {
    // error is CLError
}

// Cause 3: Background location without capability
manager.allowsBackgroundLocationUpdates = true // Requires background mode

// Cause 4: Requesting "Always" without "When In Use" first
manager.requestAlwaysAuthorization() // May be rejected without prior When In Use
```

## How to Fix

### Fix 1: Request authorization before use

```swift
let manager = CLLocationManager()

func setupLocation() {
    manager.requestWhenInUseAuthorization()
}

func locationManager(_ manager: CLLocationManager,
                     didChangeAuthorization status: CLAuthorizationStatus) {
    switch status {
    case .authorizedWhenInUse, .authorizedAlways:
        manager.startUpdatingLocation()
    case .denied, .restricted:
        print("Location access denied")
    default:
        break
    }
}
```

### Fix 2: Handle CLError in delegate

```swift
func locationManager(_ manager: CLLocationManager,
                     didFailWithError error: Error) {
    if let clError = error as? CLError {
        switch clError.code {
        case .denied:
            print("Location access denied")
        case .locationUnknown:
            print("Location temporarily unavailable")
        case .network:
            print("Network error getting location")
        default:
            print("Location error: \(clError.localizedDescription)")
        }
    }
}
```

### Fix 3: Check services before starting

```swift
if CLLocationManager.locationServicesEnabled() {
    let manager = CLLocationManager()
    manager.requestWhenInUseAuthorization()
} else {
    print("Location services disabled")
}
```

### Fix 4: Handle significant location changes for background

```swift
if CLLocationManager.significantLocationChangeMonitoringAvailable() {
    manager.startMonitoringSignificantLocationChanges()
} else {
    print("Significant location changes not available")
}
```

## Examples

```swift
// Example 1: Requesting location without checking status
let manager = CLLocationManager()
manager.startUpdatingLocation() // Silent failure without auth

// Example 2: Force-unwrapping location
func locationManager(_ manager: CLLocationManager,
                     didUpdateLocations locations: [CLLocation]) {
    let location = locations.first! // May crash on empty array
    print(location.coordinate)
}
```

## Related Errors

- [HKError]({{< relref "/languages/swift/healthkit-error" >}}) — similar permission pattern for HealthKit.
- [MKError]({{< relref "/languages/swift/mapkit-error" >}}) — MapKit errors (depends on location).
- [URLError:notConnectedToInternet]({{< relref "/languages/swift/network-connection" >}}) — network dependency.
