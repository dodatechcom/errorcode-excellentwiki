---
title: "[Solution] Swift Error — Core Data Error"
description: "Fix Swift Core Data errors. Learn about NSManagedObjectContext errors, save failures, and how to handle Core Data stack issues."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["coredata", "persistence", "database", "nsmanagedobject", "sqlite"]
weight: 5
---

# Core Data Error

Core Data errors occur during fetch, save, delete, or migration operations on the persistence stack. These errors are typically wrapped in `NSManagedObjectContext` or `NSPersistentContainer` methods.

## Description

Core Data is Apple's object-graph and persistence framework. Errors can occur at any level: model loading, context save, migration, or store access. Most Core Data errors are `NSError` instances with domain `NSCocoaErrorDomain` and specific error codes.

Common patterns:

- **Save conflicts** — multiple contexts modifying the same object.
- **Migration failures** — model changes without proper migration.
- **Validation failures** — violating constraints (unique, non-nil, min/max).
- **Store corruption** — SQLite database file becomes invalid.

## Common Causes

```swift
// Cause 1: Unhandled save error
let context = persistentContainer.viewContext
try context.save() // May throw with no catch

// Cause 2: Validation failure
let entity = User(context: context)
entity.name = "" // May violate non-empty constraint
try context.save() // ValidationError

// Cause 3: Concurrency violation
// Accessing context from wrong thread
context.perform {
    let fetchRequest = User.fetchRequest()
    let users = try? context.fetch(fetchRequest) // Must be on context queue
}

// Cause 4: Migration not configured
// Model changed but no mapping model or lightweight migration enabled
```

## How to Fix

### Fix 1: Always wrap saves in do/catch

```swift
let context = persistentContainer.viewContext
do {
    try context.save()
} catch {
    context.rollback()
    print("Save failed: \(error.localizedDescription)")
}
```

### Fix 2: Configure automatic migration

```swift
let description = NSPersistentStoreDescription()
description.shouldMigrateStoreAutomatically = true
description.shouldInferMappingModelAutomatically = true
persistentContainer.persistentStoreDescriptions = [description]
```

### Fix 3: Handle merge conflicts

```swift
context.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy
// This merges changes, preferring in-memory values for conflicts
```

### Fix 4: Validate before saving

```swift
func saveContext(_ context: NSManagedObjectContext) {
    guard context.hasChanges else { return }
    do {
        try context.save()
    } catch let error as NSError {
        switch error.code {
        case NSValidationErrorNumberTooLargeError:
            print("Number too large")
        case NSValidationMissingMandatoryPropertyError:
            print("Missing required property")
        default:
            print("Core Data error: \(error), \(error.userInfo)")
        }
    }
}
```

## Examples

```swift
// Example 1: Fetch without context queue
let context = persistentContainer.viewContext
let request = User.fetchRequest()
let users = try context.fetch(request) // May crash if not on context queue

// Example 2: Save after delete without proper handling
context.delete(user)
try context.save() // Fails if user has required relationships
```

## Related Errors

- [NSPersistentStore Error]({{< relref "/languages/swift/coredata-store" >}}) — persistent store issues.
- [File Permission Denied]({{< relref "/languages/swift/file-permission" >}}) — file access issues.
- [File Not Found]({{< relref "/languages/swift/file-not-found" >}}) — missing files.
