---
title: "Memory warning"
description: "A memory warning indicates the system is running low on memory and may terminate the application."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["memory", "warning", "ios", "objc"]
weight: 5
---

## What This Error Means

A memory warning is sent by the system when the device is running low on memory. On iOS, if the application doesn't release enough memory, it may be terminated. This is indicated by the `didReceiveMemoryWarning` method being called.

## Common Causes

- Large image or data caching
- Memory leaks from retained objects
- Circular references (strong reference cycles)
- Loading too many objects at once

## How to Fix

```objc
// WRONG: Not handling memory warnings
- (void)viewDidLoad {
    [super viewDidLoad];
    self.largeImage = [UIImage imageNamed:@"large_image.png"];
}

// CORRECT: Handle memory warnings
- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    self.largeImage = nil;
    [self clearCaches];
}
```

```objc
// WRONG: Strong reference cycle
@interface MyController ()
@property (nonatomic, strong) NSArray *items;
@property (nonatomic, strong) void (^callback)(void);
@end

// Block retains self, self retains block

// CORRECT: Use weak reference
__weak typeof(self) weakSelf = self;
self.callback = ^{
    __strong typeof(weakSelf) strongSelf = weakSelf;
    if (strongSelf) {
        // use strongSelf
    }
};
```

## Examples

```objc
// Example 1: Large data in memory
NSMutableArray *hugeArray = [NSMutableArray array];
for (int i = 0; i < 10000000; i++) {
    [hugeArray addObject:@(i)];  // Memory warning
}

// Example 2: Image caching
UIImage *bigImage = [UIImage imageNamed:@"huge.png"];
// If many large images cached, memory warning

// Example 3: Missing dealloc
- (void)dealloc {
    [[NSNotificationCenter defaultCenter] removeObserver:self];
    // cleanup to prevent leaks
}
```

## Related Errors

- [EXC_BAD_ACCESS](/languages/objective-c/exc-bad-access)
- [key not found](/languages/objective-c/key-not-found)
