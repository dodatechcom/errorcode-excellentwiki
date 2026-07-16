---
title: "[Solution] Swift Error — CKError"
description: "Fix Swift CloudKit errors. Learn about CKError codes, iCloud sync failures, and how to handle CloudKit database and zone errors."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["cloudkit", "icloud", "sync", "database", "push"]
weight: 5
---

# CKError

`CKError` is thrown by CloudKit operations when record operations fail, zones encounter issues, or iCloud sync problems occur. CloudKit has specific error codes for quota limits, server errors, and conflict resolution.

## Description

CloudKit provides iCloud-based data storage with public and private databases. `CKError` indicates failures in record saves, fetches, subscriptions, and zone operations. Quota limits and server-side issues are common in production.

Common patterns:

- **Quota exceeded** — user's iCloud storage full.
- **Server record changed** — concurrent modifications to the same record.
- **Rate limiting** — too many API calls per second.
- **Zone not found** — querying a non-existent custom zone.

## Common Causes

```swift
// Cause 1: Saving without iCloud account
let container = CKContainer.default()
let database = container.privateCloudDatabase
let record = CKRecord(recordType: "Note")
record["text"] = "Hello" as CKRecordValue
database.save(record) { _, error in
    if let error = error as? CKError {
        if error.code == .notAuthenticated {
            print("No iCloud account")
        }
    }
}

// Cause 2: Quota exceeded
database.save(record) { _, error in
    if let error = error as? CKError, error.code == .quotaExceeded {
        print("iCloud storage full")
    }
}

// Cause 3: Server record conflict
database.save(record) { _, error in
    if let error = error as? CKError, error.code == .serverRecordChanged {
        let serverRecord = error.userInfo[CKPartialErrorsByItemIDKey] as? CKRecord
        // Need to merge changes
    }
}

// Cause 4: Rate limiting
for i in 0..<1000 {
    let record = CKRecord(recordType: "Item")
    database.save(record) { _, error in
        // CKError.requestRateLimited after too many calls
    }
}
```

## How to Fix

### Fix 1: Handle CKError with specific codes

```swift
func handleCKError(_ error: Error) {
    guard let ckError = error as? CKError else { return }
    switch ckError.code {
    case .notAuthenticated:
        print("Sign in to iCloud")
    case .quotaExceeded:
        print("iCloud storage full")
    case .requestRateLimited:
        if let retryAfter = ckError.retryAfterSeconds {
            DispatchQueue.main.asyncAfter(deadline: .now() + retryAfter) {
                // Retry the operation
            }
        }
    case .serverRecordChanged:
        // Handle conflict
        break
    case .zoneNotFound:
        print("Zone does not exist")
    default:
        print("CloudKit error: \(ckError.localizedDescription)")
    }
}
```

### Fix 2: Implement retry logic for rate limiting

```swift
func saveWithRetry(record: CKRecord, database: CKDatabase, retries: Int = 3) {
    database.save(record) { _, error in
        if let error = error as? CKError, error.code == .requestRateLimited {
            if retries > 0, let retryAfter = error.retryAfterSeconds {
                DispatchQueue.main.asyncAfter(deadline: .now() + retryAfter) {
                    saveWithRetry(record: record, database: database, retries: retries - 1)
                }
            }
        }
    }
}
```

### Fix 3: Handle record conflicts

```swift
func saveWithConflictResolution(record: CKRecord, database: CKDatabase) {
    database.save(record) { _, error in
        if let error = error as? CKError, error.code == .serverRecordChanged {
            if let conflictingRecord = error.userInfo[CKPartialErrorsByItemIDKey] as? CKRecord {
                // Merge changes from conflictingRecord
                record["lastModified"] = Date() as CKRecordValue
                database.save(record) { _, _ in }
            }
        }
    }
}
```

### Fix 4: Batch operations to avoid rate limits

```swift
let operation = CKModifyRecordsOperation(recordsToSave: records)
operation.savePolicy = .ifServerRecordUnchanged
operation.modifyRecordsResultBlock = { result in
    switch result {
    case .success:
        print("Batch save successful")
    case .failure(let error):
        print("Batch save failed: \(error)")
    }
}
database.add(operation)
```

## Examples

```swift
// Example 1: Fetching from non-existent zone
let zoneID = CKRecordZone.ID(zoneName: "NonExistent", ownerName: CKCurrentUserDefaultName)
let predicate = NSPredicate(format: "TRUEPREDICATE")
let query = CKQuery(recordType: "Note", predicate: predicate)
database.fetch(withQuery: query) { result in
    // May fail with .zoneNotFound if zone doesn't exist
}

// Example 2: Subscription error
let subscription = CKDatabaseSubscription(recordType: "Note")
database.save(subscription) { _, error in
    // May fail if push notification entitlement missing
}
```

## Related Errors

- [APNS Error]({{< relref "/languages/swift/push-notification" >}}) — push notification errors.
- [Keychain Error]({{< relref "/languages/swift/keychain-error" >}}) — security-related errors.
- [URLError]({{< relref "/languages/swift/url-session-error" >}}) — network errors affecting CloudKit.
