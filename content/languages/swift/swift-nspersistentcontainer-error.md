---
title: "[Solution] Swift NSPersistentContainer Error — Load & Migration"
description: "Fix Swift NSPersistentContainer errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 134
---

NSPersistentContainer errors occur when store loading fails, lightweight migration is needed but not configured, or store types are incorrect.

## Common Causes

```swift
// Missing loadPersistentStores handler
let container = NSPersistentContainer(name: "Model")
container.loadPersistentStores { _, error in
    // Not handling error
}

// Migration not configured
// Model changed but no migration options
```

## How to Fix

**1. Proper store loading**

```swift
let container = NSPersistentContainer(name: "MyModel")
container.loadPersistentStores { description, error in
    if let error = error {
        print("Store load failed: \(error)")
        fatalError("Unresolved error \(error)")
    }
}
```

**2. Enable lightweight migration**

```swift
let description = NSPersistentStoreDescription()
description.shouldMigrateStoreAutomatically = true
description.shouldInferMappingModelAutomatically = true

let container = NSPersistentContainer(name: "MyModel")
container.persistentStoreDescriptions = [description]

container.loadPersistentStores { _, error in
    if let error = error {
        print("Migration failed: \(error)")
    }
}
```

**3. Background context**

```swift
let context = container.newBackgroundContext()
context.perform {
    // Background work
    let items = try? context.fetch(Item.fetchRequest())
}
```

**4. Save context**

```swift
func save() {
    let context = container.viewContext
    guard context.hasChanges else { return }
    
    do {
        try context.save()
    } catch {
        print("Save failed: \(error)")
        context.rollback()
    }
}
```

**5. Store type configuration**

```swift
let description = NSPersistentStoreDescription()
description.type = NSSQLiteStoreType
// Or NSSQLiteStoreType for SQLite
```

## Examples

Complete Core Data stack:
```swift
class CoreDataStack {
    static let shared = CoreDataStack()
    
    lazy var container: NSPersistentContainer = {
        let container = NSPersistentContainer(name: "MyApp")
        
        let description = NSPersistentStoreDescription()
        description.shouldMigrateStoreAutomatically = true
        description.shouldInferMappingModelAutomatically = true
        container.persistentStoreDescriptions = [description]
        
        container.loadPersistentStores { _, error in
            if let error = error {
                fatalError("Core Data store failed: \(error)")
            }
        }
        
        container.viewContext.automaticallyMergesChangesFromParent = true
        return container
    }()
    
    func save() {
        let context = container.viewContext
        guard context.hasChanges else { return }
        try? context.save()
    }
}
```

## Related Errors

- [CoreData Fetch Error](/languages/swift/swift-coredata-fetch-request)
- [CoreData Derived Data Error](/languages/swift/swift-coredata-derived-data)
- [CoreData iCloud Error](/languages/swift/swift-coredata-icloud)
