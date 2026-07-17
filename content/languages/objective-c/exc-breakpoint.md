---
title: "EXC_BREAKPOINT"
description: "An EXC_BREAKPOINT occurs when an assertion failure or breakpoint instruction is encountered."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `EXC_BREAKPOINT` exception is triggered when the program encounters a breakpoint instruction, an assertion failure, or an unexpected condition. In Objective-C, this often indicates an unhandled exception or an assertion failure.

## Common Causes

- NSAssert failure
- Unhandled exceptions reaching main
- Swift forced unwrap of nil (bridged)
- Debugger breakpoint left in code

## How to Fix

```objc
// WRONG: Assertion that may fail
NSAssert(value != nil, @"Value must not be nil");
// If value is nil, EXC_BREAKPOINT

// CORRECT: Handle gracefully instead of asserting
if (value == nil) {
    NSLog(@"Error: Value is nil");
    return;
}
```

```objc
// WRONG: Not handling exception boundaries
@try {
    [self performRiskyOperation];
}
@catch (NSException *exception) {
    // Exception not properly handled
}

// CORRECT: Proper exception handling
@try {
    [self performRiskyOperation];
}
@catch (NSException *exception) {
    NSLog(@"Exception: %@", exception.reason);
    // Handle or re-throw
}
```

## Examples

```objc
// Example 1: NSAssert failure
NSAssert(NO, @"This should never happen");
// EXC_BREAKPOINT

// Example 2: Unhandled exception
@throw [NSException exceptionWithName:@"Test"
                               reason:@"testing"
                             userInfo:nil];

// Example 3: Array index out of bounds
NSArray *arr = @[@"a", @"b"];
NSString *s = arr[5];  // NSRangeException -> EXC_BREAKPOINT
```

## Related Errors

- [EXC_BAD_ACCESS](/languages/objective-c/exc-bad-access)
- [unrecognized selector sent to instance](/languages/objective-c/unrecognized-selector)
