---
title: "unrecognized selector sent to instance"
description: "An unrecognized selector error occurs when calling a method that the object doesn't implement."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `unrecognized selector sent to instance` error occurs when you try to call a method on an object that doesn't implement it. The Objective-C runtime throws an `NSInvalidArgumentException` and terminates the application.

## Common Causes

- Wrong object type for method call
- Missing protocol implementation
- Typos in method names
- Category not linked

## How to Fix

```objc
// WRONG: Calling method on wrong type
NSString *str = @123;
[str nonExistentMethod];  // unrecognized selector

// CORRECT: Use respondsToSelector before calling
if ([str respondsToSelector:@selector(integerValue)]) {
    NSLog(@"%ld", [str integerValue]);
}
```

```objc
// WRONG: Missing protocol method
@protocol DataSource
- (NSInteger)numberOfItems;
@end

@interface MyController : NSObject <DataSource>
@end

// If numberOfItems is not implemented, calling it crashes

// CORRECT: Implement required protocol methods
@implementation MyController
- (NSInteger)numberOfItems {
    return 0;
}
@end
```

## Examples

```objc
// Example 1: Typo in method name
[myObject settName:@"Alice"];  // typo: should be setName:

// Example 2: Wrong object type
NSNumber *num = @42;
[num length];  // unrecognized selector

// Example 3: Missing category
// If NSString+Utilities.h declares a method but isn't imported
```

## Related Errors

- [EXC_BAD_ACCESS](/languages/objective-c/exc-bad-access)
- [message sent to nil](/languages/objective-c/nil-message)
