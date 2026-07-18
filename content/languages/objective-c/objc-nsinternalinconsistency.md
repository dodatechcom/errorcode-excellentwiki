---
title: "[Solution] Objective-C NSInternalInconsistencyException"
description: "Fix Objective-C NSInternalInconsistencyException. Resolve framework contract violations and invalid state errors."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

`NSInternalInconsistencyException` indicates that the internal state of a framework class has become inconsistent. This is typically caused by violating framework contracts or calling methods in the wrong order.

## Why It Happens

- Modifying collection during enumeration: The collection is mutated while being iterated.
- Updating UI from background thread: UIKit operations must occur on the main thread.
- Not calling super methods in lifecycle callbacks: Superclass implementations perform essential setup.
- Invalid state transitions in state machines: The object enters an unexpected state.
- Missing required delegate methods: The delegate does not implement methods the framework expects.

## How to Fix It

Use proper enumeration patterns:

```objectivec
// WRONG: Modifying during enumeration
for (NSString *item in mutableArray) {
    if ([item shouldRemove]) {
        [mutableArray removeObject:item];  // Exception
    }
}

// CORRECT: Collect and remove after
NSMutableArray *toRemove = [NSMutableArray array];
for (NSString *item in mutableArray) {
    if ([item shouldRemove]) {
        [toRemove addObject:item];
    }
}
[mutableArray removeObjectsInArray:toRemove];
```

Ensure UI updates on main thread:

```objectivec
dispatch_async(dispatch_get_main_queue(), ^{
    [self updateUI];
});
```

Call super in lifecycle methods:

```objectivec
- (void)viewDidLoad {
    [super viewDidLoad];  // Required
    // Additional setup
}

- (void)tableView:(UITableView *)tableView 
    commitEditingStyle:(UITableViewCellEditingStyle)editingStyle 
    forRowAtIndexPath:(NSIndexPath *)indexPath {
    // Must call super if overriding
}
```

Use proper collection mutation:

```objectivec
// Use mutableCopy for safe mutation
NSMutableArray *safeCopy = [mutableArray mutableCopy];
[safeCopy removeObject:target];
[mutableArray setArray:safeCopy];
```

Use proper state management:

```objectivec
typedef NS_ENUM(NSInteger, ViewState) {
    ViewStateLoading,
    ViewStateLoaded,
    ViewStateError
};

- (void)transitionToState:(ViewState)newState {
    if (self.currentState == ViewStateLoading && 
        newState == ViewStateError) {
        // Valid transition
    } else {
        NSLog(@"Invalid state transition");
    }
    self.currentState = newState;
}
```

Handle thread-safe UI updates:

```objectivec
- (void)updateUI {
    if ([NSThread isMainThread]) {
        [self doUpdateUI];
    } else {
        dispatch_async(dispatch_get_main_queue(), ^{
            [self doUpdateUI];
        });
    }
}
```

## Common Mistakes

- Forgetting to call super in overridden methods. Super performs essential setup.
- Updating UI from background queues. UIKit is not thread-safe.
- Not implementing all required delegate methods. Check delegate documentation.
- Using mutating operations during fast enumeration. Use enumerateObjectsUsingBlock: instead.
- Not handling state transitions properly in view controllers. Use state machines for complex flows.
- Not handling memory warnings in view controllers. Override didReceiveMemoryWarning:.

## Related Pages

- [objc-coredata-save-error]({{< relref "/languages/objective-c/objc-coredata-save-error" >}}) - CoreData save error
- [objc-thread-error]({{< relref "/languages/objective-c/objc-thread-error" >}}) - threading errors
- [objc-notification-leak]({{< relref "/languages/objective-c/objc-notification-leak" >}}) - notification leak
- [objc-nsfetchedresults]({{< relref "/languages/objective-c/objc-nsfetchedresults" >}}) - FRC errors
