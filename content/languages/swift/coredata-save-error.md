---
title: "[Solution] Swift CoreData Save Error Fix"
description: "Fix Swift CoreData save errors. Learn why CoreData save operations fail and how to handle persistence errors."
languages: ["swift"]
severities: ["error"]
error-types: ["database-error"]
tags: ["coredata", "save", "database", "swift"]
weight: 5
---

## What This Error Means

A CoreData save error occurs when `viewContext.save()` fails. This typically happens due to validation failures, constraint violations, or concurrency issues.

## Common Causes

- Validation rule violations
- Unique constraint violations
- Missing required fields
- Concurrency conflicts

## How to Fix

```swift
// WRONG: Not handling save errors
try viewContext.save()  // May throw validation error

// CORRECT: Handle all error types
do {
    try viewContext.save()
} catch let error as NSError {
    if error.domain == NSCocoaErrorDomain {
        switch error.code {
        case NSValidationMultipleErrorsError:
            let errors = error.userInfo[NSDetailedErrorsKey] as? [NSError]
            errors?.forEach { print($0.localizedDescription) }
        case NSValidationMissingMandatoryPropertyError:
            print("Missing required property")
        default:
            print("CoreData save error: \(error)")
        }
    }
    viewContext.rollback()
}
```

```swift
// WRONG: Ignoring constraint violations
class User: NSManagedObject {
    @NSManaged var email: String
}
// Unique constraint on email, but not handling duplicate

// CORRECT: Check before saving
func saveUser(email: String) throws {
    let request: NSFetchRequest<User> = User.fetchRequest()
    request.predicate = NSPredicate(format: "email == %@", email)
    let existing = try viewContext.fetch(request)
    if !existing.isEmpty {
        throw SaveError.duplicateEmail
    }
    let user = User(context: viewContext)
    user.email = email
    try viewContext.save()
}
```

## Examples

```swift
// Example 1: Save with rollback
func saveContext() {
    guard viewContext.hasChanges else { return }
    do {
        try viewContext.save()
    } catch {
        viewContext.rollback()
        print("Save failed: \(error)")
    }
}

// Example 2: Batch save
func saveAll(_ objects: [NSManagedObject]) {
    objects.forEach { viewContext.insert($0) }
    do {
        try viewContext.save()
    } catch {
        viewContext.rollback()
    }
}

// Example 3: Save with merge policy
viewContext.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy
try viewContext.save()
```

## Related Errors

- [CoreData persistence error](coredata-error) — persistence issues
- [CoreData fetch error](coredata-fetch-error) — fetch failed
- [CoreData validation error](coredata-validation-error) — validation failed
