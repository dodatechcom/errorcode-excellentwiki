---
title: "[Solution] Swift Error — NSPersistentStore Error"
description: "Fix Swift NSPersistentStore errors. Learn about persistent store loading failures, migration issues, and SQLite corruption."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["coredata", "persistent-store", "sqlite", "migration", "store"]
weight: 5
---

# NSPersistentStore Error

NSPersistentStore errors occur when the persistent store cannot be loaded, opened, or migrated. This includes SQLite database corruption, incompatible store types, and migration failures.

## Description

The persistent store is the on-disk representation of your Core Data stack. Errors at this level prevent the entire stack from functioning. Common issues include corrupted SQLite files, incompatible store versions, iCloud sync conflicts, and permission issues on the store file.

Common patterns:

- **Store type mismatch** — store was created with one type, loading with another.
- **Migration needed** — model changed but store not migrated.
- **Corrupted store file** — SQLite file damaged by crash or interruption.
- **iCloud conflicts** — conflicting versions from multiple devices.

## Common Causes

```swift
// Cause 1: Store type mismatch
let description = NSPersistentStoreDescription()
description.type = NSSQLiteStoreType
// Store was created with NSInMemoryStoreType

// Cause 2: Model version mismatch
let model = NSManagedObjectModel()
// Model changed without migration configuration
let coordinator = NSPersistentStoreCoordinator(managedObjectModel: model)
try coordinator.addPersistentStore(ofType: NSSQLiteStoreType,
                                    configurationName: nil,
                                    at: storeURL,
                                    options: nil) // Fails without migration

// Cause 3: Corrupted store file
let storeURL = applicationSupportDir.appendingPathComponent("Store.sqlite")
// File corrupted from force-kill during write

// Cause 4: Missing store file
try coordinator.addPersistentStore(ofType: NSSQLiteStoreType,
                                    configurationName: nil,
                                    at: nil, // Store file doesn't exist
                                    options: nil)
```

## How to Fix

### Fix 1: Enable automatic lightweight migration

```swift
let options: [AnyHashable: Any] = [
    NSMigratePersistentStoresAutomaticallyOption: true,
    NSInferMappingModelAutomaticallyOption: true
]
try coordinator.addPersistentStore(ofType: NSSQLiteStoreType,
                                    configurationName: nil,
                                    at: storeURL,
                                    options: options)
```

### Fix 2: Delete and recreate store on corruption

```swift
func loadStore() {
    do {
        try coordinator.addPersistentStore(ofType: NSSQLiteStoreType,
                                            configurationName: nil,
                                            at: storeURL,
                                            options: migrationOptions)
    } catch {
        // Delete corrupted store
        try? FileManager.default.removeItem(at: storeURL)
        // Recreate
        try? coordinator.addPersistentStore(ofType: NSSQLiteStoreType,
                                             configurationName: nil,
                                             at: storeURL,
                                             options: migrationOptions)
    }
}
```

### Fix 3: Use NSPersistentContainer with proper configuration

```swift
let container = NSPersistentContainer(name: "MyApp")
container.persistentStoreDescriptions.first?.setOption(
    true as NSNumber,
    forKey: NSMigratePersistentStoresAutomaticallyOption
)
container.persistentStoreDescriptions.first?.setOption(
    true as NSNumber,
    forKey: NSInferMappingModelAutomaticallyOption
)
container.loadPersistentStores { _, error in
    if let error = error {
        print("Store load error: \(error)")
    }
}
```

### Fix 4: Handle iCloud sync conflicts

```swift
let options: [AnyHashable: Any] = [
    NSPersistentStoreUbiquitousContentNameKey: "MyAppStore",
    NSPersistentStoreUbiquitousContentURLKey: cloudStoreDirectory
]
```

## Examples

```swift
// Example 1: Loading store without migration options
let coordinator = NSPersistentStoreCoordinator(managedObjectModel: model)
try coordinator.addPersistentStore(ofType: NSSQLiteStoreType,
                                    configurationName: nil,
                                    at: storeURL,
                                    options: nil) // Fails if model changed

// Example 2: Force-deleting store
let storeURL = docsDir.appendingPathComponent("Store.sqlite")
try FileManager.default.removeItem(at: storeURL) // Deletes all data
```

## Related Errors

- [Core Data Error]({{< relref "/languages/swift/coredata-error" >}}) — general Core Data issues.
- [File Not Found]({{< relref "/languages/swift/file-not-found" >}}) — missing store file.
- [File Permission Denied]({{< relref "/languages/swift/file-permission" >}}) — can't access store file.
