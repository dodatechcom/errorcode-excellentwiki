---
title: "[Solution] Swift Error — HKError"
description: "Fix Swift HealthKit errors. Learn about HKError codes, authorization failures, and how to handle HealthKit data access issues."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["healthkit", "health", "fitness", "authorization", "hysical-health"]
weight: 5
---

# HKError

`HKError` is thrown by HealthKit operations when authorization is denied, data types are unavailable, or the health store encounters issues.

## Description

HealthKit manages health and fitness data on Apple platforms. Accessing this data requires user authorization and specific entitlements. `HKError` provides codes like `.authorizationDenied`, `.invalidArgument`, and `.dataUnavailable` to indicate what went wrong.

Common patterns:

- **Authorization not requested** — querying data before requesting permission.
- **Authorization denied** — user declined health data access.
- **Invalid quantity type** — requesting a health type not available on device.
- **Background delivery not set up** — expecting updates without configuration.

## Common Causes

```swift
// Cause 1: Querying without authorization
let store = HKHealthStore()
let type = HKQuantityType.quantityType(forIdentifier: .stepCount)!
let query = HKStatisticsQuery(quantityType: type, quantitySamplePredicate: nil,
                               options: .cumulativeSum) { _, result, _ in
    // Fails if authorization not granted
}
store.execute(query)

// Cause 2: Authorization not requested first
store.requestAuthorization(toShare: [], read: [type]) { success, error in
    // Must check success before querying
}

// Cause 3: Health type not available on device
let type = HKQuantityType.quantityType(forIdentifier: .oxygenSaturation)
// May not be available on all devices

// Cause 4: Querying health store from background
// HealthKit has restrictions on background access
```

## How to Fix

### Fix 1: Always request authorization first

```swift
let store = HKHealthStore()
let types: Set<HKSampleType> = [
    HKQuantityType.quantityType(forIdentifier: .stepCount)!,
    HKQuantityType.quantityType(forIdentifier: .heartRate)!
]
store.requestAuthorization(toShare: [], read: types) { success, error in
    if success {
        // Now safe to query
    } else {
        print("Authorization failed: \(error?.localizedDescription ?? "")")
    }
}
```

### Fix 2: Check device capabilities

```swift
if HKHealthStore.isHealthDataAvailable() {
    // HealthKit available
    let store = HKHealthStore()
    // Request authorization and query
} else {
    print("HealthKit not available on this device")
}
```

### Fix 3: Handle HKError in queries

```swift
let query = HKSampleQuery(sampleType: type, predicate: nil, limit: 100,
                           sortDescriptors: nil) { query, results, error in
    if let error = error as? HKError {
        switch error.code {
        case .authorizationDenied:
            print("User denied access")
        case .dataUnavailable:
            print("Data not available")
        default:
            print("HealthKit error: \(error)")
        }
        return
    }
    // Process results
}
store.execute(query)
```

### Fix 4: Set up background delivery properly

```swift
store.enableBackgroundDelivery(for: type, frequency: .hourly) { success, error in
    if !success {
        print("Background delivery failed: \(error?.localizedDescription ?? "")")
    }
}
```

## Examples

```swift
// Example 1: Querying without checking authorization status
let store = HKHealthStore()
let type = HKQuantityType.quantityType(forIdentifier: .heartRate)!
let query = HKStatisticsQuery(quantityType: type, quantitySamplePredicate: nil,
                               options: .discreteAverage) { _, result, _ in
    if let result = result {
        print(result)
    }
}
store.execute(query) // May fail without authorization

// Example 2: Requesting unavailable health type
let type = HKQuantityType.quantityType(forIdentifier: .environmentalAudioExposure)
// Only available on certain devices with specific iOS versions
```

## Related Errors

- [Core Location Error]({{< relref "/languages/swift/corelocation-error" >}}) — similar permission/access pattern.
- [Keychain Error]({{< relref "/languages/swift/keychain-error" >}}) — security-related access error.
- [Security Error]({{< relref "/languages/swift/security-error" >}}) — OS-level security error.
