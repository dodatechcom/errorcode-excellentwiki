---
title: "[Solution] CloudKit Server Record Error Fix"
description: "Fix CloudKit server record errors when saving or fetching records fails."
languages: ["swift"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# CloudKit: Server Record Error Fix

A CloudKit server record error occurs when CKRecord operations fail due to server-side conflicts, permission issues, or network problems.

## What This Error Means

CloudKit syncs data to iCloud servers. Server record errors happen when there's a record conflict (another device modified the same record), the record type doesn't exist, or the user lacks permission.

## Common Causes

- Record conflict from concurrent modifications
- Record type not defined in CloudKit schema
- User not signed into iCloud
- Record exceeds size limits
- Network connectivity issues

## How to Fix

### 1. Handle record conflicts

```swift
// CORRECT: Handle CKError.serverRecordChanged
func saveRecord(_ record: CKRecord) {
    container.privateCloudDatabase.save(record) { _, error in
        if let ckError = error as? CKError {
            switch ckError.code {
            case .serverRecordChanged:
                if let serverRecord = ckError.serverRecord {
                    // Merge changes and retry
                    self.mergeAndSave(serverRecord, localRecord: record)
                }
            case .unknownItem:
                // Record type doesn't exist in schema
                print("Record type not found in CloudKit schema")
            default:
                print("CKError: \(ckError.localizedDescription)")
            }
        }
    }
}
```

### 2. Check iCloud account status

```swift
// CORRECT: Verify iCloud availability
CKAccount.default.accountStatus { status, error in
    switch status {
    case .available:
        self.startCloudKitOperations()
    case .noAccount:
        print("User not signed into iCloud")
    case .restricted:
        print("iCloud restricted")
    case .couldNotDetermine:
        print("Could not determine iCloud status")
    @unknown default:
        break
    }
}
```

### 3. Use batch operations

```swift
// CORRECT: Use CKModifyRecordsOperation
let operation = CKModifyRecordsOperation(recordsToSave: [record], recordIDsToDelete: nil)
operation.modifyRecordsResultBlock = { result in
    switch result {
    case .success:
        print("Records saved")
    case .failure(let error):
        print("Batch save failed: \(error)")
    }
}
container.privateCloudDatabase.add(operation)
```

### 4. Retry with exponential backoff

```swift
// CORRECT: Retry failed operations
func saveWithRetry(_ record: CKRecord, attempts: Int = 3) {
    container.privateCloudDatabase.save(record) { _, error in
        if let ckError = error as? CKError, attempts > 0 {
            let delay = Double(4 - attempts) * 2.0
            DispatchQueue.global().asyncAfter(deadline: .now() + delay) {
                self.saveWithRetry(record, attempts: attempts - 1)
            }
        }
    }
}
```

## Related Errors

- [CloudKit Error]({{< relref "/languages/swift/cloudkit-error" >}}) — general CloudKit errors
- [HealthKit Error](healthkit-error-v2) — HealthKit authorization
- [Push Notification Error](push-notification-error-v2) — APNs issues
