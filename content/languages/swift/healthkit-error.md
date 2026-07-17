---
title: "[Solution] Swift HealthKit Error Fix"
description: "Fix Swift HealthKit errors. Learn why HealthKit operations fail and how to handle health data issues."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A HealthKit error occurs when HealthKit operations fail. This can happen due to missing permissions, unavailable health data types, or authorization issues.

## Common Causes

- HealthKit not available on device
- Missing health permission
- Health data type not supported
- Authorization not requested

## How to Fix

```swift
// WRONG: Not checking HealthKit availability
let healthStore = HKHealthStore()
healthStore.requestAuthorization(toShare: [], read: []) { success, error in
    // Ignoring error
}

// CORRECT: Check availability first
guard HKHealthStore.isHealthDataAvailable() else {
    print("HealthKit not available")
    return
}
```

```swift
// WRONG: Not requesting authorization
func readHeartRate() {
    let type = HKQuantityType.quantityType(forIdentifier: .heartRate)!
    // May fail without authorization
}

// CORRECT: Request authorization first
func requestAuthorization(completion: @escaping (Bool, Error?) -> Void) {
    let typesToRead: Set<HKObjectType> = [
        HKQuantityType.quantityType(forIdentifier: .heartRate)!,
        HKQuantityType.quantityType(forIdentifier: .stepCount)!
    ]
    healthStore.requestAuthorization(toShare: [], read: typesToRead, completion: completion)
}
```

## Examples

```swift
// Example 1: Read health data
import HealthKit

let healthStore = HKHealthStore()
let type = HKQuantityType.quantityType(forIdentifier: .heartRate)!

let query = HKSampleQuery(sampleType: type, predicate: nil, limit: 10, sortDescriptors: nil) { query, results, error in
    guard let samples = results as? [HKQuantitySample] else { return }
    for sample in samples {
        print("Heart rate: \(sample.quantity)")
    }
}
healthStore.execute(query)

// Example 2: Write health data
let type = HKQuantityType.quantityType(forIdentifier: .stepCount)!
let quantity = HKQuantity(unit: .count(), doubleValue: 1000)
let sample = HKQuantitySample(type: type, quantity: quantity, start: Date(), end: Date())
healthStore.save(sample) { success, error in
    // Handle result
}

// Example 3: Observer query
let type = HKQuantityType.quantityType(forIdentifier: .heartRate)!
let query = HKObserverQuery(sampleType: type, predicate: nil) { query, completionHandler, error in
    // New data available
    completionHandler()
}
healthStore.execute(query)
```

## Related Errors

- [HomeKit error](homekit-error) — HomeKit error
- [CloudKit operation error](cloudkit-error-swift) — CloudKit error
- [MapKit error](mapkit-error) — MapKit error
