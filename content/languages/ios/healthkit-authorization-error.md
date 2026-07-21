---
title: "[Solution] HealthKit Authorization Error"
description: "Fix HealthKit authorization failures preventing health data access in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# HealthKit Authorization Error

HealthKit authorization fails when the required capabilities are not enabled or the user denies permission.

## Common Causes
- HealthKit capability not enabled in project
- Requesting write and read permissions simultaneously
- Invalid health data type for the device
- User denied HealthKit access

## How to Fix
1. Enable HealthKit capability in your target
2. Request read and write permissions separately
3. Verify data types are available on the device
4. Handle authorization denial gracefully

```swift
let healthStore = HKHealthStore()
let readTypes: Set<HKObjectType> = [HKObjectType.quantityType(forIdentifier: .stepCount)!]
healthStore.requestAuthorization(toShare: nil, read: readTypes) { success, error in
    if success {
        // Access granted
    }
}
```

## Examples
```swift
// HealthKit authorization with error handling:
func requestHealthKitAccess() {
    guard HKHealthStore.isHealthDataAvailable() else { return }
    let store = HKHealthStore()
    let types: Set<HKSampleType> = [
        HKObjectType.quantityType(forIdentifier: .stepCount)!,
        HKObjectType.quantityType(forIdentifier: .heartRate)!
    ]
    store.requestAuthorization(toShare: nil, read: types) { success, error in
        DispatchQueue.main.async {
            if success { self.enableHealthFeatures() }
            else { self.showHealthKitDeniedAlert() }
        }
    }
}
```
