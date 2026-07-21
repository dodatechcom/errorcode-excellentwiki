---
title: "Objective-C Swift Bridging Header Error"
description: "Fix Objective-C Swift bridging header errors when Objective-C classes are not visible in Swift code."
languages: ["objective-c"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Bridging header file not configured in build settings
- Header file not included in bridging header
- Objective-C class missing NS_SWIFT_NAME annotation
- Header contains C++ code without proper guards
- Circular imports between Swift and Objective-C

## How to Fix

```objc
// WRONG: Header not in bridging header
// MyBridgingHeader.h
// #import "MyClass.h"  -- commented out!

// CORRECT: Include the header
// MyBridgingHeader.h
#import "MyClass.h"
#import "MyModel.h"
```

```objc
// WRONG: C++ header without guards in bridging header
// MyBridgingHeader.h
#include "cppclass.h"  // Error in Swift context

// CORRECT: Wrap C++ in extern "C" or use module map
#ifdef __cplusplus
extern "C" {
#endif
#include "cppclass.h"
#ifdef __cplusplus
}
#endif
```

## Examples

```objc
// Example 1: Expose Objective-C class to Swift
// MyObjcClass.h
@interface MyObjcClass : NSObject
- (NSString *)greetingForName:(NSString *)name;
@property (nonatomic, readonly) NSString *version;
@end

// MyBridgingHeader.h
#import "MyObjcClass.h"

// Swift usage
let objc = MyObjcClass()
let greeting = objc.greeting(forName: "World")

// Example 2: Rename for Swift
// MyClass.h
@interface MyClass : NSObject
- (void)doWorkWithCompletion:(void(^)(BOOL))completion
    NS_SWIFT_NAME(doWork(completion:));
@end

// Example 3: Enum bridging
typedef NS_ENUM(NSInteger, MyState) {
    MyStateActive NS_SWIFT_NAME(active),
    MyStateInactive NS_SWIFT_NAME(inactive)
};
```

## Related Errors

- [Swift bridging error](objc-swift-bridging) -- Swift interop issues
- [Compiler error](objc-compiler-error) -- compilation problems
