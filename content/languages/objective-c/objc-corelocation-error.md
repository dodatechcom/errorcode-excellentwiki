---
title: "[Solution] Objective-C CoreLocation Error"
description: "CoreLocation errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C CoreLocation Error

CoreLocation errors.

### Common Causes
Permission not granted; accuracy

### How to Fix
```objc
CLLocationManager *manager = [[CLLocationManager alloc] init];
manager.delegate = self;
manager.desiredAccuracy = kCLLocationAccuracyBest;
[manager requestWhenInUseAuthorization];
[manager startUpdatingLocation];
```

### Examples
```objc
- (void)locationManager:(CLLocationManager *)manager didUpdateLocations:(NSArray<CLLocation *> *)locations {
    CLLocation *location = locations.lastObject;
    NSLog(@"Lat: %f, Lon: %f", location.coordinate.latitude, location.coordinate.longitude);
}
```
