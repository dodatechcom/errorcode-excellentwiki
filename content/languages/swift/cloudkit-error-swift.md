---
title: "[Solution] Swift CloudKit Operation Error Fix"
description: "Fix Swift CloudKit operation errors. Learn why CloudKit operations fail and how to handle iCloud sync issues."
languages: ["swift"]
severities: ["error"]
error-types: ["network-error"]
tags: ["cloudkit", "icloud", "sync", "swift"]
weight: 5
---

## What This Error Means

A CloudKit operation error occurs when CloudKit database operations fail. This can happen due to network issues, quota exceeded, permission errors, or record conflicts.

## Common Causes

- Network unavailable
- iCloud quota exceeded
- Permission denied for record type
- Record conflict during save

## How to Fix

```swift
// WRONG: Not handling CloudKit errors
let database = CKContainer.default().privateCloudDatabase
database.save(record) { record, error in
    // Ignoring error
}

// CORRECT: Handle CloudKit errors
database.save(record) { record, error in
    if let error = error as? CKError {
        switch error.code {
        case .serverRecordChanged:
            // Handle conflict
            break
        case .quotaExceeded:
            // Show quota error
            break
        default:
            print("CloudKit error: \(error)")
        }
    }
}
```

```swift
// WRONG: Not checking iCloud availability
let container = CKContainer.default()

// CORRECT: Check account status
container.accountStatus { status, error in
    switch status {
    case .available:
        // iCloud available
        break
    case .noAccount:
        // No iCloud account
        break
    case .restricted:
        // iCloud restricted
        break
    default:
        break
    }
}
```

## Examples

```swift
// Example 1: Basic CloudKit usage
import CloudKit

let container = CKContainer.default()
let database = container.privateCloudDatabase

let record = CKRecord(recordType: "Note")
record["title"] = "My Note" as CKRecordValue
record["content"] = "Hello, CloudKit!" as CKRecordValue

database.save(record) { result in
    switch result {
    case .success(let savedRecord):
        print("Saved: \(savedRecord)")
    case .failure(let error):
        print("Failed: \(error)")
    }
}

// Example 2: Query
let predicate = NSPredicate(format: "title == %@", "My Note")
let query = CKQuery(recordType: "Note", predicate: predicate)
database.fetch(withQuery: query) { result in
    // Handle results
}

// Example 3: Batch operations
let operation = CKModifyRecordsOperation(recordsToSave: [record], recordIDsToDelete: nil)
operation.modifyRecordsResultBlock = { result in
    // Handle result
}
database.add(operation)
```

## Related Errors

- [URLError network error](url-error-swift) — network error
- [HealthKit error](healthkit-error) — HealthKit error
- [HomeKit error](homekit-error) — HomeKit error
