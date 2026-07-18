---
title: "[Solution] Objective-C CoreData Save Validation Error"
description: "Fix Objective-C CoreData save failed and validation errors. Handle managed object context save issues."
languages: ["objective-c"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

CoreData save errors occur when the managed object context cannot persist changes to the store. Validation errors indicate that managed objects do not meet the model constraints.

## Why It Happens

- Required attributes are nil: A required property has no value.
- Attribute values violate uniqueness constraints: A unique constraint is violated.
- Relationship integrity violations: Required relationships are missing.
- Store file is locked or inaccessible: The SQLite file is locked by another process.
- Concurrency conflicts between contexts: Multiple contexts modified the same object.

## How to Fix It

Handle save errors with detailed logging:

```objectivec
NSError *error = nil;
if (![self.managedObjectContext save:&error]) {
    NSLog(@"Save error: %@", error.localizedDescription);
    NSLog(@"Details: %@", error.userInfo);
    [self.managedObjectContext rollback];
}
```

Implement validation in managed object subclasses:

```objectivec
- (BOOL)validateForInsert:(NSError **)error {
    if (self.name == nil || self.name.length == 0) {
        if (error) {
            *error = [NSError errorWithDomain:@"com.app" 
                code:1001 
                userInfo:@{NSLocalizedDescriptionKey: @"Name required"}];
        }
        return NO;
    }
    return [super validateForInsert:error];
}
```

Use merge policy for conflicts:

```objectivec
self.managedObjectContext.mergePolicy = 
    NSMergeByPropertyObjectTrumpMergePolicy;
```

Save in background context:

```objectivec
NSManagedObjectContext *bgContext = 
    [[NSManagedObjectContext alloc] 
    initWithConcurrencyType:NSPrivateQueueConcurrencyType];
bgContext.parentContext = self.managedObjectContext;

[bgContext performBlock:^{
    [bgContext save:nil];
    [self.managedObjectContext performBlock:^{
        [self.managedObjectContext save:nil];
    }];
}];
```

Handle specific validation errors:

```objectivec
NSError *error = nil;
if (![context save:&error]) {
    if ([error.domain isEqualToString:NSCocoaErrorDomain]) {
        switch (error.code) {
            case NSValidationMissingMandatoryPropertyError:
                NSLog(@"Required property is nil");
                break;
            case NSValidationDuplicateNSErrorCode:
                NSLog(@"Duplicate value for unique constraint");
                break;
            case NSValidationRelationshipLacksMinimumCountError:
                NSLog(@"Relationship has too few objects");
                break;
        }
    }
}
```

Use performBlock for thread safety:

```objectivec
[context performBlock:^{
    NSError *error = nil;
    [context save:&error];
}];
```

## Common Mistakes

- Not checking save return value. The save method returns a boolean indicating success.
- Ignoring validation errors during save. Check error.userInfo for details.
- Using wrong merge policy for concurrent writes. Choose the appropriate merge strategy.
- Not handling store migration requirements. Core Data may need lightweight migration.
- Saving too frequently causing performance issues. Batch saves when possible.
- Not calling processPendingChanges before save. This ensures all changes are committed.

## Related Pages

- [objc-coredata-fetch-error]({{< relref "/languages/objective-c/objc-coredata-fetch-error" >}}) - CoreData fetch errors
- [objc-nsinternalinconsistency]({{< relref "/languages/objective-c/objc-nsinternalinconsistency" >}}) - internal inconsistency
- [objc-coreanimation-error]({{< relref "/languages/objective-c/objc-coreanimation-error" >}}) - Core Animation errors
- [objc-nsfetchedresults]({{< relref "/languages/objective-c/objc-nsfetchedresults" >}}) - FRC errors
