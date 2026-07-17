---
title: "message sent to nil"
description: "A message sent to nil occurs when calling a method on a nil object reference."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

In Objective-C, sending a message to nil is technically allowed and returns nil/0/NO, but this can cause unexpected behavior when the return value is used without checking for nil. This is different from a crash but can lead to subtle bugs.

## Common Causes

- Object not initialized
- Failed initialization returning nil
- Wrong object reference
- Deallocated object

## How to Fix

```objc
// WRONG: Not checking nil return
NSString *name = [self getUserName];
NSString *upper = [name uppercaseString];  // nil if name is nil

// CORRECT: Check for nil
NSString *name = [self getUserName];
if (name) {
    NSString *upper = [name uppercaseString];
}
```

```objc
// WRONG: Passing nil to method expecting non-nil
NSString *result = [NSString stringWithFormat:@"%@", nil];
// May produce unexpected output

// CORRECT: Validate before passing
id value = [self getValue];
if (value) {
    NSString *result = [NSString stringWithFormat:@"%@", value];
}
```

## Examples

```objc
// Example 1: Nil return value
NSString *str = [self findString:@"missing"];
[str length];  // returns 0 (nil message)

// Example 2: Nil object
NSObject *obj = nil;
[obj description];  // nil (no crash, but returns nil)

// Example 3: Unexpected nil in chain
NSString *result = [[self getArray] firstObject];
// If getArray returns nil, result is nil
```

## Related Errors

- [unrecognized selector sent to instance](/languages/objective-c/unrecognized-selector)
- [EXC_BAD_ACCESS](/languages/objective-c/exc-bad-access)
