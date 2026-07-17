---
title: "[Solution] Objective-C Exception"
description: "Fix Objective-C NSException handling and uncaught exception errors"
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["high"]
tags: ["cocoa-touch", "exception-handling", "objective-c-runtime"]
weight: 5
---

## What This Error Means
Objective-C exceptions are thrown for serious runtime errors that cannot be recovered from gracefully, often leading to application termination.

## Common Causes
- NSRangeException from invalid index access
- NSInvalidArgumentException from invalid method arguments
- NSInternalInconsistencyException from framework contract violations
- Uncaught exceptions reaching main()
- Throwing exceptions in dealloc or init methods

## How to Fix
```objectivec
// Use @try/@catch for exception handling
@try {
    NSArray *array = @[@"a", @"b"];
    NSString *element = array[5]; // Throws NSRangeException
} @catch (NSException *exception) {
    NSLog(@"Caught: %@", exception.name);
    NSLog(@"Reason: %@", exception.reason);
} @finally {
    // Cleanup code
}

// Set up exception handler for uncaught exceptions
NSSetUncaughtExceptionHandler(&handleException);
```