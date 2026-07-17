---
title: "[Solution] CoreData Persistent Store Error Fix"
description: "Fix CoreData errors when the persistent store cannot be loaded or migrated."
languages: ["swift"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# CoreData: Persistent Store Error Fix

A CoreData persistent store error occurs when the persistent store coordinator fails to load, migrate, or access the underlying SQLite store.

## What This Error Means

CoreData uses a persistent store (usually SQLite) to persist objects. Errors occur when the store file is corrupted, schema migration is needed, or the store type is incompatible.

## Common Causes

- Schema changed without migration
- Store file corrupted
- Lightweight migration not configured
- Store type mismatch
- File permissions issue

## How to Fix

### 1. Enable automatic lightweight migration

```swift
// CORRECT: Configure migration options
let description = NSPersistentStoreDescription()
description.type = NSSQLiteStoreType
description.setOption(true as NSNumber, forKey: NSMigratePersistentStoresAutomaticallyOption)
description.setOption(true as NSNumber, forKey: NSInferMappingModelAutomaticallyOption)
container.persistentStoreDescriptions = [description]
```

### 2. Handle store loading errors

```swift
// CORRECT: Handle persistent store errors
container.loadPersistentStores { description, error in
    if let error = error {
        print("CoreData store error: \(error)")
        // Optionally: delete and recreate store
        self.deleteStoreAndRetry(container: self.container)
    }
}
```

### 3. Add mapping models for complex migrations

```swift
// CORRECT: Create .xcmappingmodel for non-lightweight migrations
// In Xcode: File > New > Mapping Model
// Then reference it:
let model = NSManagedObjectModel.mergedModel(from: [Bundle.main])!
let mapping = NSMappingModel(named: "MyModelMapping", in: Bundle.main, forSourceModel: model, destinationModel: model)
```

### 4. Reset store as last resort

```swift
// CORRECT: Delete corrupted store
func deleteStoreAndRetry(container: NSPersistentContainer) {
    let store = container.persistentStoreCoordinator.persistentStores.first
    if let storeURL = store?.url {
        try? FileManager.default.removeItem(at: storeURL)
    }
    container.loadPersistentStores { _, error in
        if let error = error {
            fatalError("Failed to load store: \(error)")
        }
    }
}
```

## Related Errors

- [CoreData Fetch Error](coredata-fetch-error) — fetch request issues
- [CoreData Save Error](coredata-save-error) — save failures
- [CoreData Validation Error](coredata-validation-error) — validation issues
