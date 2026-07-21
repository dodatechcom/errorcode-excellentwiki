---
title: "Objective-C Core Data Fetch Request Error"
description: "Fix Objective-C Core Data NSFetchRequest errors when predicate syntax or sort descriptors are malformed."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Predicate format string has wrong placeholder or format
- Sort descriptor references non-existent property
- Fetch request on wrong managed object context
- Relationship key path not accessible in predicate
- Batch size set too high causing memory pressure

## How to Fix

```objc
// WRONG: Predicate with wrong format
NSFetchRequest *request = [NSFetchRequest fetchRequestWithEntityName:@"User"];
request.predicate = [NSPredicate predicateWithFormat:@"name == %@", @"Alice"];
// If name is not a property of User entity, this crashes at runtime

// CORRECT: Verify property exists in model
NSFetchRequest *request = [NSFetchRequest fetchRequestWithEntityName:@"User"];
request.predicate = [NSPredicate predicateWithFormat:@"userName == %@", @"Alice"];
```

```objc
// WRONG: Sort descriptor on non-existent key
NSSortDescriptor *sort = [NSSortDescriptor sortDescriptorWithKey:@"nonExistent"
                                                        ascending:YES];
request.sortDescriptors = @[sort]; // crash when fetch executes

// CORRECT: Use valid property name
NSSortDescriptor *sort = [NSSortDescriptor sortDescriptorWithKey:@"createdAt"
                                                        ascending:NO];
request.sortDescriptors = @[sort];
```

## Examples

```objc
// Example 1: Basic fetch
NSFetchRequest *request = [NSFetchRequest fetchRequestWithEntityName:@"Product"];
request.predicate = [NSPredicate predicateWithFormat:@"price > %f", 10.0];
request.sortDescriptors = @[[NSSortDescriptor sortDescriptorWithKey:@"name"
                                                          ascending:YES]];
request.fetchLimit = 100;

NSError *error = nil;
NSArray *results = [context executeFetchRequest:request error:&error];

// Example 2: Fetch with relationship
NSFetchRequest *request = [NSFetchRequest fetchRequestWithEntityName:@"Order"];
request.predicate = [NSPredicate predicateWithFormat:
    @"customer.name == %@", @"Alice"];

// Example 3: Batch fetching
NSBatchFetchRequest *batchRequest = [[NSBatchFetchRequest alloc]
    initWithEntityName:@"Log"];
batchRequest.fetchBatchSize = 20;
```

## Related Errors

- [CoreData error](objc-coredata-error) -- Core Data stack issues
- [CoreData fetch error](objc-coredata-fetch-error) -- fetch request problems
