---
title: "[Solution] Swift Core Data Derived Attribute & Transient Error"
description: "Fix Swift Core Data derived attributes and transient properties. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 136
---

Core Data derived attribute and transient property errors occur when computed properties aren't properly configured, undo manager isn't set up, or derived values don't update.

## Common Causes

```swift
// Transient property not marked as transient in model
// Derived attribute not recalculating

// Missing undo manager
context.undoManager = nil // No undo support
```

## How to Fix

**1. Derived attributes**

```swift
// In .xcdatamodeld:
// Set attribute as "Derived" with expression:
// SELF.firstName + " " + SELF.lastName

// Programmatic derived value
class Person: NSManagedObject {
    @NSManaged var firstName: String
    @NSManaged var lastName: String
    
    var fullName: String {
        "\(firstName) \(lastName)"
    }
}
```

**2. Transient properties**

```swift
class Item: NSManagedObject {
    @NSManaged var name: String
    @NSManaged transient var cachedImage: UIImage? // Transient
}
```

**3. Undo manager setup**

```swift
context.undoManager = UndoManager()

// Undo
context.undoManager?.undo()

// Redo
context.undoManager?.redo()
```

**4. Custom computed properties**

```swift
extension Item {
    var formattedDate: String {
        let formatter = DateFormatter()
        formatter.dateStyle = .medium
        return formatter.string(from: date ?? Date())
    }
}
```

**5. Fault handling**

```swift
// Accessing properties triggers fault
let item: Item = // fault
print(item.name) // Fires fault, fetches data

// Refresh object
context.refresh(item, mergeChanges: true)
```

## Examples

Complete derived attribute setup:
```swift
class Invoice: NSManagedObject {
    @NSManaged var items: NSSet?
    @NSManaged var taxRate: Double
    
    var subtotal: Double {
        let itemSet = items as? Set<InvoiceItem> ?? []
        return itemSet.reduce(0) { $0 + $1.price * Double($1.quantity) }
    }
    
    var total: Double {
        subtotal * (1 + taxRate)
    }
    
    var formattedTotal: String {
        NumberFormatter.currency.string(from: NSNumber(value: total)) ?? "$0.00"
    }
}
```

## Related Errors

- [NSPersistentContainer Error](/languages/swift/swift-nspersistentcontainer-error)
- [CoreData Fetch Error](/languages/swift/swift-coredata-fetch-request)
- [CoreData iCloud Error](/languages/swift/swift-coredata-icloud)
