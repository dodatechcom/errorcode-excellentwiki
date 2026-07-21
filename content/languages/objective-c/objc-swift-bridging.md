---
title: "[Solution] Objective-C/Swift Bridging"
description: "Swift-ObjC interop errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C/Swift Bridging

Swift-ObjC interop errors.

### Common Causes
Missing bridging header; wrong types

### How to Fix
```objc
// In bridging header
#import "MyObjCClass.h"
```

### Examples
```objc
// Make ObjC visible to Swift
// Class must inherit from NSObject or be @objc
@interface SwiftBridgedClass : NSObject
- (void)myMethod;
@end
```
