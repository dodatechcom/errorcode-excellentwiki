---
title: "Objective-C KVO Observation Not Removed Error"
description: "Fix Objective-C KVO observation errors when observers are not properly removed before deallocation."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Observer not removed in dealloc or viewWillDisappear
- Removing observer that was never added
- Adding same observer multiple times
- Key path typo does not match property name
- Using KVO on non-KVO compliant properties

## How to Fix

```objc
// WRONG: Not removing observer
- (void)viewDidLoad {
    [super viewDidLoad];
    [self.model addObserver:self forKeyPath:@"status" options:0 context:nil];
}
// Missing dealloc -- crash when model changes after controller is gone

// CORRECT: Remove in dealloc
- (void)dealloc {
    [self.model removeObserver:self forKeyPath:@"status"];
}
```

```objc
// WRONG: Removing observer that was never added
- (void)dealloc {
    [self.model removeObserver:self forKeyPath:@"nonExistentKey"]; // crash
}

// CORRECT: Track observation state
@property (nonatomic) BOOL isObserving;

- (void)startObserving {
    if (!self.isObserving) {
        [self.model addObserver:self forKeyPath:@"status" options:0 context:nil];
        self.isObserving = YES;
    }
}

- (void)stopObserving {
    if (self.isObserving) {
        [self.model removeObserver:self forKeyPath:@"status"];
        self.isObserving = NO;
    }
}
```

## Examples

```objc
// Example 1: Basic KVO
- (void)viewDidLoad {
    [super viewDidLoad];
    [self.player addObserver:self
                  forKeyPath:@"isPlaying"
                     options:NSKeyValueObservingOptionNew
                     context:&playerContext];
}

- (void)observeValueForKeyPath:(NSString *)keyPath
                      ofObject:(id)object
                        change:(NSDictionary *)change
                       context:(void *)context {
    if (context == &playerContext) {
        BOOL playing = [change[NSKeyValueChangeNewKey] boolValue];
        [self updatePlayButton:playing];
    }
}

- (void)dealloc {
    [self.player removeObserver:self forKeyPath:@"isPlaying" context:&playerContext];
}
```

## Related Errors

- [KVO error](objc-kvo-error) -- key-value observing issues
- [Memory leak error](objc-memory-leak) -- memory management problems
