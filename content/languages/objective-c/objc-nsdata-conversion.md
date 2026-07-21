---
title: "[Solution] Objective-C NSData Conversion"
description: "NSData to/from string conversion errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C NSData Conversion

NSData to/from string conversion errors.

### Common Causes
Wrong encoding; nil data

### How to Fix
```objc
NSData *data = [str dataUsingEncoding:NSUTF8StringEncoding];
NSString *str = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
```

### Examples
```objc
// JSON data
NSError *error = nil;
NSDictionary *dict = [NSJSONSerialization JSONObjectWithData:data options:0 error:&error];
```
