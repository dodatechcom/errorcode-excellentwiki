---
title: "[Solution] Swift Error — MKError"
description: "Fix Swift MapKit errors. Learn about MKError codes, map loading failures, and how to handle geocoding and routing errors."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["mapkit", "map", "geocoding", "routing", "annotation"]
weight: 5
---

# MKError

`MKError` is thrown by MapKit operations when map loading fails, geocoding encounters issues, or routing requests fail. Common codes include `.loadingThrottled`, `.placemarkNotFound`, and `.directionsNotFound`.

## Description

MapKit provides mapping, geocoding, and routing services. `MKError` indicates failures in these operations. Unlike many framework errors, MapKit sometimes degrades gracefully rather than throwing, but errors still occur in completion handlers.

Common patterns:

- **Geocoding failure** — invalid or ambiguous address.
- **No route found** — impossible route between two points.
- **Rate limiting** — too many requests in quick succession.
- **Missing entitlement** — MapKit requires specific capabilities.

## Common Causes

```swift
// Cause 1: Geocoding invalid address
let geocoder = CLGeocoder()
geocoder.geocodeAddressString("") { placemarks, error in
    // error may be CLError or MKError
}

// Cause 2: Route not found
let request = MKDirections.Request()
request.source = MKMapItem(placemark: MKPlacemark(coordinate: start))
request.destination = MKMapItem(placemark: MKPlacemark(coordinate: end))
let directions = MKDirections(request: request)
directions.calculateDirectionsWithCompletion { response, error in
    // error may be MKError(.noMatches) or MKError(.loadingThrottled)
}

// Cause 3: Too many requests
for i in 0..<100 {
    let request = MKLocalSearch.Request()
    request.naturalLanguageQuery = "coffee \(i)"
    let search = MKLocalSearch(request: request)
    search.start { _, error in
        // MKError.loadingThrottled after too many requests
    }
}

// Cause 4: MKMapView without proper setup
let mapView = MKMapView()
mapView.delegate = self
// Not setting region or visible map rect
```

## How to Fix

### Fix 1: Handle MKError in completion handlers

```swift
let directions = MKDirections(request: request)
directions.calculateDirectionsWithCompletion { response, error in
    if let error = error as? MKError {
        switch error.code {
        case .loadingThrottled:
            print("Too many requests - try again later")
        case .placemarkNotFound:
            print("Could not find location")
        case .directionsNotFound:
            print("No route found")
        default:
            print("MapKit error: \(error.localizedDescription)")
        }
        return
    }
    // Process response
}
```

### Fix 2: Validate inputs before geocoding

```swift
func geocode(address: String) {
    guard !address.trimmingCharacters(in: .whitespaces).isEmpty else {
        print("Empty address")
        return
    }
    let geocoder = CLGeocoder()
    geocoder.geocodeAddressString(address) { placemarks, error in
        if let error = error {
            print("Geocoding failed: \(error.localizedDescription)")
            return
        }
        // Process placemarks
    }
}
```

### Fix 3: Rate-limit MapKit requests

```swift
class MapKitThrottler {
    private var lastRequestTime: Date?
    private let minimumInterval: TimeInterval = 1.0

    func throttle(_ action: @escaping () -> Void) {
        let now = Date()
        if let last = lastRequestTime, now.timeIntervalSince(last) < minimumInterval {
            let delay = minimumInterval - now.timeIntervalSince(last)
            DispatchQueue.main.asyncAfter(deadline: .now() + delay, execute: action)
        } else {
            action()
        }
        lastRequestTime = Date()
    }
}
```

### Fix 4: Set up MKMapView properly

```swift
let mapView = MKMapView()
mapView.showsUserLocation = true
mapView.delegate = self
let region = MKCoordinateRegion(center: coordinate,
                                 latitudinalMeters: 1000,
                                 longitudinalMeters: 1000)
mapView.setRegion(region, animated: true)
```

## Examples

```swift
// Example 1: Empty search query
let request = MKLocalSearch.Request()
request.naturalLanguageQuery = ""
let search = MKLocalSearch(request: request)
search.start { _, error in
    // May return MKError.placemarkNotFound
}

// Example 2: Route with same source and destination
let request = MKDirections.Request()
request.source = MKMapItem(placemark: MKPlacemark(coordinate: coord))
request.destination = MKMapItem(placemark: MKPlacemark(coordinate: coord))
let directions = MKDirections(request: request)
directions.calculateDirectionsWithCompletion { _, error in
    // MKError.directionsNotFound
}
```

## Related Errors

- [Core Location Error]({{< relref "/languages/swift/corelocation-error" >}}) — underlying location errors.
- [URLError]({{< relref "/languages/swift/url-session-error" >}}) — network errors affecting map loading.
- [URLError:notConnectedToInternet]({{< relref "/languages/swift/network-connection" >}}) — offline map issues.
