---
title: "[Solution] Objective-C NSFileManager Error"
description: "File manager operation errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C NSFileManager Error

File manager operation errors.

### Common Causes
Wrong path; permissions; not checking

### How to Fix
```objc
NSFileManager *fm = [NSFileManager defaultManager];
if ([fm fileExistsAtPath:path]) {
    NSError *error = nil;
    [fm removeItemAtPath:path error:&error];
}
```

### Examples
```objc
NSError *error = nil;
BOOL success = [fm copyItemAtPath:src toPath:dst error:&error];
if (!success) {
    NSLog(@"Copy failed: %@", error);
}
```
