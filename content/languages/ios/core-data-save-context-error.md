---
title: "[Solution] Core Data Save Context Error"
description: "Fix Core Data NSManagedObjectContext save errors preventing data persistence."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Core Data Save Context Error

Context save fails when managed object validation rules are violated or the context has unresolvable conflicts.

## Common Causes
- Required properties left nil
- Validation rules violated (uniqueness, value ranges)
- Concurrency violations accessing context from wrong thread
- Parent context not saved before child context

## How to Fix
1. Check all required properties are set before saving
2. Implement validation methods in your NSManagedObject subclass
3. Use perform block for thread-safe context access
4. Save child contexts before parent

```swift
// Thread-safe save:
context.perform {
    let item = MyEntity(context: context)
    item.name = "Test"
    do {
        try context.save()
    } catch {
        print("Save failed: \(error)")
    }
}
```

## Examples
```swift
// Proper Core Data save with error handling:
func saveContext() {
    let context = persistentContainer.viewContext
    guard context.hasChanges else { return }
    do {
        try context.save()
    } catch {
        let nsError = error as NSError
        fatalError("Unresolved error \(nsError), \(nsError.userInfo)")
    }
}
```
