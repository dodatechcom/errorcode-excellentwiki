---
title: "Location Provider Error"
description: "Fix Android location provider and fused location client errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Location provider does not return location updates or returns stale data

## Common Causes

- FusedLocationProviderClient not initialized
- Location request interval too frequent or too slow
- Location priority not set for use case
- Location updates not stopped when activity paused

## Fixes

- Initialize FusedLocationProviderClient
- Configure LocationRequest with appropriate interval
- Use PRIORITY_HIGH_ACCURACY for GPS
- Stop updates in onPause to save battery

## Code Example

```kotlin
val fusedLocationClient = LocationServices.getFusedLocationProviderClient(this)

val locationRequest = LocationRequest.Builder(Priority.PRIORITY_HIGH_ACCURACY, 5000)
    .setMinUpdateDistanceMeters(10f)
    .build()

val locationCallback = object : LocationCallback() {
    override fun onLocationResult(result: LocationResult) {
        result.lastLocation?.let { location ->
            val lat = location.latitude
            val lng = location.longitude
        }
    }
}

fusedLocationClient.requestLocationUpdates(
    locationRequest, locationCallback, Looper.getMainLooper()
)

// Stop in onPause:
fusedLocationClient.removeLocationUpdates(locationCallback)
```

# PRIORITY_HIGH_ACCURACY: GPS
# PRIORITY_BALANCED_POWER_ACCURACY: network
# PRIORITY_LOW_POWER: battery saving
# Stop updates when not needed!
