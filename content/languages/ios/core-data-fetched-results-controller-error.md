---
title: "[Solution] Core Data Fetched Results Controller Error"
description: "Fix NSFetchedResultsController delegate and data source errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Core Data Fetched Results Controller Error

FetchedResultsControllers fail when the fetch request is misconfigured, when the managed object context changes are not properly propagated, or when the delegate is not set.

## Common Causes
- Fetch request entity type does not match
- Sort descriptor key does not exist in entity
- Delegate not set before performing fetch
- Section name key path causes incorrect grouping

## How to Fix
1. Verify fetch request entity matches the data model
2. Check sort descriptor key paths exist
3. Set delegate before calling performFetch
4. Verify sectionNameKeyPath data is consistent

```swift
// Setup fetched results controller:
let request: NSFetchRequest<Item> = Item.fetchRequest()
request.sortDescriptors = [NSSortDescriptor(key: "name", ascending: true)]

let frc = NSFetchedResultsController(
    fetchRequest: request,
    managedObjectContext: context,
    sectionNameKeyPath: nil,
    cacheName: "ItemCache"
)
frc.delegate = self
try? frc.performFetch()
```

## Examples
```swift
// FRC delegate methods:
func controllerWillChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {
    tableView.beginUpdates()
}

func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>, didChange sectionInfo: NSFetchedResultsSectionInfo, atSectionIndex sectionIndex: Int, for type: NSFetchedResultsChangeType) {
    let indexSet = IndexSet(integer: sectionIndex)
    switch type {
    case .insert: tableView.insertSections(indexSet, with: .fade)
case .delete: tableView.deleteSections(indexSet, with: .fade)
default: break
    }
}

func controllerDidChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {
    tableView.endUpdates()
}
```
