---
title: "[Solution] Swift NSFetchRequest Error — Sort & Predicate"
description: "Fix Swift Core Data fetch request errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 135
---

NSFetchRequest errors occur when sort descriptors are missing, predicate format strings are invalid, or fetch limits cause unexpected behavior.

## Common Causes

```swift
// Missing sort descriptor
let request: NSFetchRequest<Item> = Item.fetchRequest()
// No sortDescriptor - undefined order

// Invalid predicate format
let predicate = NSPredicate(format: "name == %@", argumentArray: [])
```

## How to Fix

**1. Proper fetch request**

```swift
let request: NSFetchRequest<Item> = Item.fetchRequest()
request.sortDescriptors = [NSSortDescriptor(keyPath: \Item.name, ascending: true)]
request.predicate = NSPredicate(format: "age > %d", 18)
```

**2. Fetch with context**

```swift
let context = persistentContainer.viewContext
do {
    let items = try context.fetch(request)
    print("Found \(items.count) items")
} catch {
    print("Fetch failed: \(error)")
}
```

**3. Fetch limit**

```swift
let request: NSFetchRequest<Item> = Item.fetchRequest()
request.fetchLimit = 20
request.fetchOffset = 0
```

**4. Predicate examples**

```swift
// String contains
let predicate = NSPredicate(format: "name CONTAINS[cd] %@", searchText)

// Date range
let predicate = NSPredicate(format: "date BETWEEN {%@, %@}", startDate, endDate)

// IN clause
let predicate = NSPredicate(format: "id IN %@", ids)
```

**5. Batch fetching**

```swift
let request: NSFetchRequest<Item> = Item.fetchRequest()
request.fetchBatchSize = 20
```

## Examples

Advanced fetch request:
```swift
func searchItems(query: String, category: String?) -> [Item] {
    let request: NSFetchRequest<Item> = Item.fetchRequest()
    
    var predicates: [NSPredicate] = []
    predicates.append(NSPredicate(format: "name CONTAINS[cd] %@", query))
    
    if let category = category {
        predicates.append(NSPredicate(format: "category == %@", category))
    }
    
    request.predicate = NSCompoundPredicate(andPredicateWithSubpredicates: predicates)
    request.sortDescriptors = [
        NSSortDescriptor(keyPath: \Item.name, ascending: true),
        NSSortDescriptor(keyPath: \Item.date, ascending: false)
    ]
    request.fetchLimit = 50
    
    return (try? context.fetch(request)) ?? []
}
```

## Related Errors

- [NSPersistentContainer Error](/languages/swift/swift-nspersistentcontainer-error)
- [CoreData Derived Data Error](/languages/swift/swift-coredata-derived-data)
- [CoreData iCloud Error](/languages/swift/swift-coredata-icloud)
