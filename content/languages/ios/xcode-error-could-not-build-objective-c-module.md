---
title: "[Solution] Xcode Error: Could Not Build Objective-C Module"
description: "Fix Objective-C module build failures in mixed Swift/ObjC projects."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Could Not Build Objective-C Module

This error appears when Xcode cannot build an Objective-C module that your Swift code imports. It is common in projects mixing Swift and Objective-C.

## Common Causes
- Bridging header not properly configured
- Missing modulemap for the Objective-C framework
- Circular imports between Swift and Objective-C
- Incompatible Objective-C compiler flags

## How to Fix
1. Verify the bridging header path in Build Settings
2. Ensure all Objective-C headers are properly exposed
3. Use @objc and @objcMembers annotations where needed
4. Create a module.modulemap for custom Objective-C frameworks

```swift
// In Build Settings, verify:
// Objective-C Bridging Header = $(SRCROOT)/YourProject-Bridging-Header.h

// In your bridging header:
#import <UIKit/UIKit.h>
#import "YourObjCClass.h"

// For the ObjC class to be visible:
// .h file must be marked as public in the framework
// or included in the bridging header
```

## Examples
```swift
// Example: Exposing Objective-C class to Swift
// YourClass.h
@interface MyClass : NSObject
@property (nonatomic, strong) NSString *name;
- (void)doSomething;
@end

// YourClass.m
@implementation MyClass
- (void)doSomething {
    NSLog(@"Doing something with %@", self.name);
}
@end

// In Swift:
let obj = MyClass()
obj.name = "Hello"
obj.doSomething()
```
