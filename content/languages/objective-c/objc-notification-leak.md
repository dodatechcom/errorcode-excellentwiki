---
title: "[Solution] Objective-C Notification Observer Not Removed Leak"
description: "Fix Objective-C notification observer leak. Properly remove observers in dealloc and manage notification center."
languages: ["objective-c"]
error-types: ["memory-error"]
severities: ["warning"]
weight: 5
---

## What This Error Means

Notification observer not removed errors occur when observers are not properly cleaned up, leading to crashes when notifications are posted to deallocated observers.

## Why It Happens

- Observer not removed in dealloc: The observer was added but never removed.
- Adding observer multiple times: The same observer is registered multiple times.
- Using block-based observers without storing token: The token is needed to remove the observer.
- Object deallocated while notification pending: A notification is posted after the observer is deallocated.
- Not removing observers before deallocation: The observer remains registered after the object is freed.

## How to Fix It

Store observer tokens for block-based observers:

```objectivec
@interface MyController ()
@property (nonatomic, strong) id observerToken;
@end

@implementation MyController
- (void)viewDidLoad {
    [super viewDidLoad];
    self.observerToken = [[NSNotificationCenter defaultCenter] 
        addObserverForName:@"MyNotification" 
        object:nil 
        queue:nil 
        usingBlock:^(NSNotification *note) {
            [self handleNotification:note];
        }];
}

- (void)dealloc {
    [[NSNotificationCenter defaultCenter] 
        removeObserver:self.observerToken];
}
@end
```

Use modern cleanup in dealloc:

```objectivec
- (void)dealloc {
    [[NSNotificationCenter defaultCenter] removeObserver:self];
}
```

Avoid adding observer multiple times:

```objectivec
- (void)setupNotifications {
    [[NSNotificationCenter defaultCenter] 
        removeObserver:self name:@"Update" object:nil];
    [[NSNotificationCenter defaultCenter] 
        addObserver:self 
        selector:@selector(handleNotification:) 
        name:@"Update" 
        object:nil];
}
```

Use weak references in notification blocks:

```objectivec
__weak typeof(self) weakSelf = self;
self.observerToken = [[NSNotificationCenter defaultCenter] 
    addObserverForName:@"Update" 
    object:nil 
    queue:nil 
    usingBlock:^(NSNotification *note) {
        __strong typeof(weakSelf) strongSelf = weakSelf;
        if (strongSelf) {
            [strongSelf handleUpdate];
        }
    }];
```

Use weak references in notification blocks:

```objectivec
__weak typeof(self) weakSelf = self;
self.observerToken = [[NSNotificationCenter defaultCenter] 
    addObserverForName:@"Update" 
    object:nil 
    queue:nil 
    usingBlock:^(NSNotification *note) {
        __strong typeof(weakSelf) strongSelf = weakSelf;
        if (strongSelf) {
            [strongSelf handleUpdate];
        }
    }];
```

Check if observer is still registered:

```objectivec
if (self.observerToken) {
    [[NSNotificationCenter defaultCenter] 
        removeObserver:self.observerToken];
    self.observerToken = nil;
}
```

## Common Mistakes

- Forgetting dealloc cleanup. Always remove observers in dealloc.
- Adding observer in init but removing in viewWillDisappear. This is inconsistent.
- Not handling block observer token properly. Store the token for later removal.
- Using postNotificationName on background thread. Notifications are delivered on the posting thread.
- Not considering that NSNotificationCenter holds strong references to observers.
- Not removing observers before object deallocation. This causes zombie object crashes.

## Related Pages

- [objc-block-cycle]({{< relref "/languages/objective-c/objc-block-cycle" >}}) - retain cycle
- [objc-memory-error]({{< relref "/languages/objective-c/objc-memory-error" >}}) - memory errors
- [objc-nsinternalinconsistency]({{< relref "/languages/objective-c/objc-nsinternalinconsistency" >}}) - internal inconsistency
- [objc-excbadaccess]({{< relref "/languages/objective-c/objc-excbad-access" >}}) - EXC_BAD_ACCESS
