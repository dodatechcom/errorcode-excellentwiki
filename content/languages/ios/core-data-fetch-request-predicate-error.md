---
title: "[Solution] Core Data Fetch Request Predicate Error"
description: "Fix NSFetchRequest predicate errors causing incorrect results or crashes."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Core Data Fetch Request Predicate Error

Predicate errors occur when the predicate format string does not match the data types, when key paths are invalid, or when predicate syntax is incorrect.

## Common Causes
- Predicate format key path does not exist in entity
- Type mismatch in predicate comparison
- Incorrect predicate format syntax
- Missing argument substitution values

## How to Fix
1. Verify key paths exist in the Core Data model
2. Match predicate comparison types to attribute types
3. Use NSPredicate(predicateFormat:) for complex predicates
4. Provide all substitution variables

```swift
// Correct predicate usage:
let request: NSFetchRequest<Item> = Item.fetchRequest()
request.predicate = NSPredicate(format: "name CONTAINS %@", searchText)
request.sortDescriptors = [NSSortDescriptor(key: "name", ascending: true)]

// With multiple conditions:
request.predicate = NSPredicate(format: "name CONTAINS %@ AND age > %d", "John", 25)
```

## Examples
```swift
// Common predicate patterns:
// Equals:
NSPredicate(format: "name == %@", "John")
// Contains:
NSPredicate(format: "name CONTAINS[cd] %@", "jo")
// Between:
NSPredicate(format: "age BETWEEN {18, 65}")
// IN:
NSPredicate(format: "status IN %@", ["active", "pending"])
// NULL check:
NSPredicate(format: "email != nil")
// Compound:
NSCompoundPredicate(andPredicateWithSubpredicates: [pred1, pred2])
```
