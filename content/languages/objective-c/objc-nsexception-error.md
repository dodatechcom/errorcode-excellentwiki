---
title: "[Solution] Objective-C NSException Error"
description: "NSException handling errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C NSException Error

NSException handling errors.

### Common Causes
Wrong throw syntax; not catching

### How to Fix
```objc
@throw [NSException exceptionWithName:@"InvalidOperation"
    reason:@"Cannot divide by zero"
    userInfo:nil];
```

### Examples
```objc
@try {
    // risky code
} @catch (NSException *exception) {
    NSLog(@"Exception: %@", exception.reason);
} @finally {
    // cleanup
}
```
