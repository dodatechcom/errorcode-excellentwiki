---
title: "[Solution] macOS CloudKit Errors"
description: "Fix macOS CloudKit errors. Causes and solutions for iCloud sync, record operations, and database failures."
platforms: ["macos"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["cloudkit", "icloud", "sync", "ckerror", "database"]
weight: 5
---

# macOS CloudKit Errors

CloudKit errors (`CKErrorDomain`) indicate failures in iCloud data synchronization, record operations, and database interactions. These errors affect applications using iCloud for storage and sync.

## What This Error Means

Common CloudKit error codes:

- `CKErrorInternalError (1)` — Internal server error
- `CKErrorPartialFailure (2)` — Some operations failed, others succeeded
- `CKErrorNetworkUnavailable (3)` — Network is not available
- `CKErrorQuotaExceeded (25)` — iCloud storage quota exceeded
- `CKErrorServerRecordChanged (14)` — Record was modified on the server
- `CKErrorAssetFileNotFound (26)` — Referenced asset file not found locally

## Common Causes

- iCloud account is not signed in or has been locked
- Network connectivity issues preventing sync
- iCloud storage quota has been exceeded
- Record conflicts between local and server versions

## How to Fix

### Verify iCloud Sign-In Status

```bash
# Check iCloud account status
brctl status
```

### Handle Record Conflicts

```swift
import CloudKit

let database = CKContainer.default().privateCloudDatabase
let record = CKRecord(recordType: "MyRecord")

database.save(record) { savedRecord, error in
    if let ckError = error as? CKError {
        switch ckError.code {
        case .serverRecordChanged:
            // Resolve conflict by merging changes
            if let serverRecord = ckError.serverRecord {
                // Apply local changes to server record
            }
        case .quotaExceeded:
            print("iCloud storage full — free up space in Settings > iCloud")
        default:
            print("CKError: \(ckError.localizedDescription)")
        }
    }
}
```

### Clear CloudKit Cache

```bash
# Reset CloudKit local cache
rm -rf ~/Library/Caches/CloudKit/*
```

### Monitor Storage Usage

```swift
CKContainer.default().requestApplicationPermission(.userDiscoverability) { status, error in
    if status == .granted {
        // Permission granted, proceed with operations
    }
}
```

## Related Errors

- [OSStatus Authentication Errors]({{< relref "/os/macos/osstatus-auth" >}}) — iCloud authentication failures
- [NSURLError]({{< relref "/os/macos/nsurlerror" >}}) — Network errors affecting CloudKit sync
- [Core Data Errors]({{< relref "/os/macos/core-data" >}}) — Local persistence errors related to iCloud sync
