---
title: "[Solution] Objective-C NSError Error"
description: "NSError creation and handling errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C NSError Error

NSError creation and handling errors.

### Common Causes
Wrong domain; missing userInfo

### How to Fix
```objc
NSError *error = [NSError errorWithDomain:@"MyDomain"
    code:42
    userInfo:@{NSLocalizedDescriptionKey: @"Something went wrong"}];
```

### Examples
```objc
NSError *error = nil;
BOOL success = [data writeToFile:path options:0 error:&error];
if (!success) {
    NSLog(@"Error: %@", error.localizedDescription);
}
```
