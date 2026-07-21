---
title: "[Solution] Objective-C Copy Error"
description: "Copy property not implemented correctly."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Copy Error

Copy property not implemented correctly.

### Common Causes
Missing NSCopying; mutable copy issues

### How to Fix
```objc
@property (nonatomic, copy) NSString *name;
```

### Examples
```objc
NSMutableString *mutableStr = [NSMutableString stringWithString:@"hello"];
NSString *immutableCopy = [mutableStr copy];
```
