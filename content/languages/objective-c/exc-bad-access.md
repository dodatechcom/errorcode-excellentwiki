---
title: "EXC_BAD_ACCESS"
description: "An EXC_BAD_ACCESS occurs when accessing memory that has been freed or is invalid."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `EXC_BAD_ACCESS` exception occurs when your program tries to access memory that has already been freed, or memory that it doesn't have permission to access. This is one of the most common and difficult-to-debug crashes in Objective-C.

## Common Causes

- Accessing a deallocated object (dangling pointer)
- Over-releasing an object
- Double free
- Buffer overflow

## How to Fix

```objc
// WRONG: Accessing freed object
NSString *str = [[NSString alloc] initWithFormat:@"hello"];
[str release];  // if using manual reference counting
NSLog(@"%@", str);  // EXC_BAD_ACCESS

// CORRECT: Use ARC or check before accessing
#ifdef __has_feature(objc_arc)
// ARC handles memory management
NSString *str = [[NSString alloc] initWithFormat:@"hello"];
NSLog(@"%@", str);
#endif
```

```objc
// WRONG: Accessing released delegate
@interface MyController ()
@property (nonatomic, weak) id<MyDelegate> delegate;
@end

// If delegate is released but delegate pointer still valid

// CORRECT: Use weak and check nil
if (self.delegate) {
    [self.delegate didSomething];
}
```

## Examples

```objc
// Example 1: Dangling pointer
NSObject *obj = [[NSObject alloc] init];
[obj release];
[obj description];  // EXC_BAD_ACCESS

// Example 2: Accessing freed array element
NSMutableArray *arr = [NSMutableArray arrayWithObjects:@"a", @"b", nil];
[arr release];
[arr count];  // EXC_BAD_ACCESS

// Example 3: Over-released object
NSString *str = @"hello";
[str release];  // over-release (string literals are retained)
[str release];  // EXC_BAD_ACCESS
```

## Related Errors

- [unrecognized selector sent to instance](/languages/objective-c/unrecognized-selector)
- [Memory warning](/languages/objective-c/memory-warning)
