---
title: "[Solution] Objective-C NSData Error"
description: "NSData reading/writing errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C NSData Error

NSData reading/writing errors.

### Common Causes
File not found; encoding issues

### How to Fix
```objc
NSData *data = [NSData dataWithContentsOfFile:@"file.txt"];
```

### Examples
```objc
NSError *error = nil;
NSData *data = [NSData dataWithContentsOfFile:@"file.txt" options:0 error:&error];
if (!data) {
    NSLog(@"Error: %@", error);
}
```
