---
title: "[Solution] Core Data Migration Error"
description: "Fix Core Data lightweight and heavyweight migration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Core Data Migration Error

Migration fails when the data model changes are not compatible with lightweight migration, when mapping models are incorrect, or when the persistent store cannot be opened after migration.

## Common Causes
- Model changes too complex for lightweight migration
- Missing mapping model for heavyweight migration
- Persistent store coordinator fails to add store
- Versioned model not properly configured

## How to Fix
1. Use lightweight migration for simple changes (additive only)
2. Create mapping models for complex changes
3. Configure options for automatic migration
4. Handle migration errors in persistent container setup

```swift
// Enable automatic migration:
let description = NSPersistentStoreDescription()
description.type = NSSQLiteStoreType
description.setOption(true as NSNumber, forKey: NSMigratePersistentStoresAutomaticallyOption)
description.setOption(true as NSNumber, forKey: NSInferMappingModelAutomaticallyOption)
persistentContainer.persistentStoreDescriptions = [description]
```

## Examples
```swift
// Persistent container with migration:
lazy var persistentContainer: NSPersistentContainer = {
    let container = NSPersistentContainer(name: "Model")
    let description = NSPersistentStoreDescription()
    description.type = NSSQLiteStoreType
    description.setOption(true as NSNumber, forKey: NSMigratePersistentStoresAutomaticallyOption)
    description.setOption(true as NSNumber, forKey: NSInferMappingModelAutomaticallyOption)
    container.persistentStoreDescriptions = [description]
    container.loadPersistentStores { _, error in
        if let error = error { fatalError("Migration failed: \(error)") }
    }
    return container
}()
```
