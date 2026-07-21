---
title: "[Solution] Objective-C JSON Serialization"
description: "NSJSONSerialization errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C JSON Serialization

NSJSONSerialization errors.

### Common Causes
Invalid JSON; writing fails

### How to Fix
```objc
NSData *data = [NSJSONSerialization dataWithJSONObject:dict options:0 error:&error];
```

### Examples
```objc
NSDictionary *dict = @{@"key": @"value"};
NSData *json = [NSJSONSerialization dataWithJSONObject:dict
    options:NSJSONWritingPrettyPrinted
    error:&error];
NSString *jsonStr = [[NSString alloc] initWithData:json encoding:NSUTF8StringEncoding];
```
