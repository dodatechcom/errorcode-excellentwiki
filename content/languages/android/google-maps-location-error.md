---
title: "Maps Location Error"
description: "Fix Google Maps location permission and my-location layer errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Google Maps cannot show user location or camera follows incorrectly

## Common Causes

- ACCESS_FINE_LOCATION permission not granted
- My location button not enabled
- LocationClient not initialized
- Camera not following location updates

## Fixes

- Request runtime location permission before enabling
- Enable my-location layer on MapFragment
- Initialize FusedLocationProviderClient
- Set camera to follow location with OnMyLocationChangeListener

## Code Example

```kotlin
// Check permission
if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION)
    == PackageManager.PERMISSION_GRANTED) {
    map.isMyLocationEnabled = true
}

// Get location updates
val fusedLocationClient = LocationServices.getFusedLocationProviderClient(this)
fusedLocationClient.lastLocation.addOnSuccessListener { location ->
    location?.let {
        val latLng = LatLng(it.latitude, it.longitude)
        map.animateCamera(CameraUpdateFactory.newLatLngZoom(latLng, 15f))
    }
}
```

# Request permission first:
ActivityCompat.requestPermissions(this,
    arrayOf(Manifest.permission.ACCESS_FINE_LOCATION), LOCATION_PERMISSION_REQUEST)
