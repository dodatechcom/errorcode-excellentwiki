---
title: "[Solution] Objective-C NSFetchedResultsController Delegate Error"
description: "Fix Objective-C NSFetchedResultsController delegate errors. Handle controller delegate callbacks and state."
languages: ["objective-c"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

NSFetchedResultsController delegate errors occur when the delegate does not properly handle change notifications or the controller is used incorrectly with CoreData.

## Why It Happens

- Delegate not set before performFetch: The controller cannot notify changes without a delegate.
- Controller used with wrong managed object context: The context does not match the fetch request.
- Changing fetch request after initialization: The fetch request is immutable after init.
- Not handling all delegate callbacks: Missing delegate methods cause incomplete table updates.
- Context save not triggered before delegate updates: The context must be saved to trigger updates.

## How to Fix It

Set delegate before fetching:

```objectivec
NSFetchedResultsController *frc = 
    [[NSFetchedResultsController alloc] 
    initWithFetchRequest:fetchRequest
    managedObjectContext:context
    sectionNameKeyPath:@"category"
    cacheName:@"Root"];

frc.delegate = self;

NSError *error = nil;
if (![frc performFetch:&error]) {
    NSLog(@"Fetch error: %@", error);
}
```

Implement all required delegate methods:

```objectivec
- (void)controllerWillChangeContent:(NSFetchedResultsController *)controller {
    [self.tableView beginUpdates];
}

- (void)controllerDidChangeContent:(NSFetchedResultsController *)controller {
    [self.tableView endUpdates];
}

- (void)controller:(NSFetchedResultsController *)controller 
    didChangeObject:(id)anObject 
    atIndexPath:(NSIndexPath *)indexPath 
    forChangeType:(NSFetchedResultsChangeType)type 
    newIndexPath:(NSIndexPath *)newIndexPath {
    switch (type) {
        case NSFetchedResultsChangeInsert:
            [self.tableView insertRowsAtIndexPaths:@[newIndexPath]
                withRowAnimation:UITableViewRowAnimationFade];
            break;
        case NSFetchedResultsChangeDelete:
            [self.tableView deleteRowsAtIndexPaths:@[indexPath]
                withRowAnimation:UITableViewRowAnimationFade];
            break;
        case NSFetchedResultsChangeUpdate:
            [self.tableView reloadRowsAtIndexPaths:@[indexPath]
                withRowAnimation:UITableViewRowAnimationFade];
            break;
        case NSFetchedResultsChangeMove:
            [self.tableView deleteRowsAtIndexPaths:@[indexPath]
                withRowAnimation:UITableViewRowAnimationFade];
            [self.tableView insertRowsAtIndexPaths:@[newIndexPath]
                withRowAnimation:UITableViewRowAnimationFade];
            break;
    }
}
```

Save context to trigger updates:

```objectivec
NSError *error = nil;
if (![self.managedObjectContext save:&error]) {
    NSLog(@"Save error: %@", error);
}
```

Handle section changes:

```objectivec
- (void)controller:(NSFetchedResultsController *)controller 
    didChangeSection:(id<NSFetchedResultsSectionInfo>)sectionInfo 
    atIndex:(NSUInteger)sectionIndex 
    forChangeType:(NSFetchedResultsChangeType)type {
    switch (type) {
        case NSFetchedResultsChangeInsert:
            [self.tableView insertSections:
                [NSIndexSet indexSetWithIndex:sectionIndex]
                withRowAnimation:UITableViewRowAnimationFade];
            break;
        case NSFetchedResultsChangeDelete:
            [self.tableView deleteSections:
                [NSIndexSet indexSetWithIndex:sectionIndex]
                withRowAnimation:UITableViewRowAnimationFade];
            break;
    }
}
```

Handle cache properly:

```objectivec
// Clear cache when fetch request changes
[NSFetchedResultsController deleteCacheWithName:frc.cacheName];

// Or disable caching
frc.cacheName = nil;
```

Use section name key path correctly:

```objectivec
NSFetchedResultsController *frc = 
    [[NSFetchedResultsController alloc] 
    initWithFetchRequest:request
    managedObjectContext:context
    sectionNameKeyPath:@"category.name"  // Key path for sections
    cacheName:@"Root"];
```

Handle fetch errors in delegate:

```objectivec
- (void)controllerDidChangeContent:(NSFetchedResultsController *)controller {
    NSError *error = nil;
    if (![controller performFetch:&error]) {
        NSLog(@"Refetch error: %@", error);
    }
    [self.tableView endUpdates];
}
```

## Common Mistakes

- Not setting delegate before performFetch. The delegate is required for change notifications.
- Forgetting to handle all change types. Each type requires specific table view operations.
- Not using beginUpdates/endUpdates. This ensures atomic table view updates.
- Changing fetch request after initialization. Create a new controller instead.
- Not clearing the cache when the fetch request changes. Stale cache causes incorrect results.
- Not implementing controller:didChangeSection:atIndex:forChangeType:. Section changes require handling.
- Using the wrong managed object context. The context must match the fetch request.

## Related Pages

- [objc-coredata-fetch-error]({{< relref "/languages/objective-c/objc-coredata-fetch-error" >}}) - CoreData fetch errors
- [objc-coredata-save-error]({{< relref "/languages/objective-c/objc-coredata-save-error" >}}) - CoreData save errors
- [objc-nsinternalinconsistency]({{< relref "/languages/objective-c/objc-nsinternalinconsistency" >}}) - internal inconsistency
- [objc-thread-error]({{< relref "/languages/objective-c/objc-thread-error" >}}) - threading issues
