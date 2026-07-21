---
title: "[Solution] Objective-C NSString Error"
description: "NSString operation errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C NSString Error

NSString operation errors.

### Common Causes
Wrong encoding; format string issues

### How to Fix
```objc
NSString *str = [NSString stringWithFormat:@"Hello %@, age %d", name, age];
```

### Examples
```objc
NSData *data = [str dataUsingEncoding:NSUTF8StringEncoding];
NSString *decoded = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
```
