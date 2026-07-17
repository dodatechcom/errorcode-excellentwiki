---
title: "[Solution] macOS Core Data Errors"
description: "Fix macOS Core Data errors. Causes and solutions for persistence, migration, and fetch request failures."
platforms: ["macos"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["core-data", "persistence", "migration", "sqlite", "xcdatamodel"]
weight: 5
---

# macOS Core Data Errors

Core Data errors (`NSCocoaErrorDomain` in the 134000–134999 range) indicate failures in the persistence layer, including SQLite database issues, migration failures, and fetch request problems.

## What This Error Means

Key Core Data error codes:

- `NSCoreDataError (134060)` — General Core Data error
- `NSMigrationManagerError (134110)` — Migration manager failed
- `NSInferredMappingModelError (134190)` — Inferred mapping model could not be created
- `NSPersistentStoreIncompleteSaveError (134020)` — Save operation partially failed
- `NSSQLiteError (134110)` — SQLite database error

## Common Causes

- Data model version mismatch between code and database
- SQLite database corruption
- Missing or invalid migration mapping model
- Managed object context has stale data references

## How to Fix

### Validate Data Model

```bash
# Check model versions
ls -la MyApp.xcdatamodeld/

# Verify model compilation
xcrun xcdatamodelc --compile CompiledModel.momd MyApp.xcdatamodeld
```

### Handle Migration Errors

```swift
let options = [
    NSMigratePersistentStoresAutomaticallyOption: true,
    NSInferMappingModelAutomaticallyOption: true
]

do {
    let store = try persistentStoreCoordinator.addPersistentStore(
        ofType: NSSQLiteStoreType,
        configurationName: nil,
        at: storeURL,
        options: options
    )
} catch {
    print("Migration failed: \(error)")
    // Fall back: delete database and start fresh
    try? FileManager.default.removeItem(at: storeURL)
}
```

### Reset Core Data Stack

```swift
// Delete the persistent store and recreate
let storeURL = applicationSupportURL.appendingPathComponent("MyApp.sqlite")
try? FileManager.default.removeItem(at: storeURL)
// Reinitialize the Core Data stack
```

### Validate SQLite Database

```bash
# Check SQLite database integrity
sqlite3 path/to/database.sqlite "PRAGMA integrity_check;"
```

## Related Errors

- [Cocoa Error Codes]({{< relref "/os/macos/cocoa-error" >}}) — General Cocoa framework errors
- [NSFileError]({{< relref "/os/macos/nsfileerror" >}}) — File system errors affecting database files
- [CloudKit Errors]({{< relref "/os/macos/cloudkit-error" >}}) — iCloud sync errors related to Core Data
