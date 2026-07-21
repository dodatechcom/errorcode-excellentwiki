---
title: "[Solution] Objective-C Plist Error"
description: "Property list errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Plist Error

Property list errors.

### Common Causes
Wrong format; not serializable

### How to Fix
```objc
NSDictionary *plist = @{@"key": @"value"};
[plist writeToFile:@"file.plist" atomically:YES];
```

### Examples
```objc
NSDictionary *plist = [NSDictionary dictionaryWithContentsOfFile:@"file.plist"];
```
