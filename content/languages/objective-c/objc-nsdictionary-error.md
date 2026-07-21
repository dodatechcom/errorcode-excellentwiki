---
title: "[Solution] Objective-C NSDictionary Error"
description: "NSDictionary errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C NSDictionary Error

NSDictionary errors.

### Common Causes
Key not found; wrong initialization

### How to Fix
```objc
NSDictionary *dict = @{@"key1": @"value1"};
NSString *val = dict[@"key1"];
```

### Examples
```objc
NSMutableDictionary *mutableDict = [NSMutableDictionary dictionary];
mutableDict[@"key"] = @"value";
```
