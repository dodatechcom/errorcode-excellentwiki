---
title: "[Solution] Objective-C Archiving Error"
description: "NSKeyedArchiver/Unarchiver errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Archiving Error

NSKeyedArchiver/Unarchiver errors.

### Common Causes
Missing NSCoding; wrong key

### How to Fix
```objc
NSData *data = [NSKeyedArchiver archivedDataWithRootObject:obj requiringSecureCoding:NO error:nil];
```

### Examples
```objc
NSSet *classes = [NSSet setWithObjects:[MyClass class], nil];
MyClass *obj = [NSKeyedUnarchiver unarchivedObjectOfClasses:classes fromData:data error:nil];
```
