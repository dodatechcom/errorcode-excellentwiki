---
title: "[Solution] Xcode Build Error: Undefined Symbol"
description: "Resolve undefined symbol linker errors in Xcode iOS projects."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Build Error: Undefined Symbol

An undefined symbol error means the linker cannot find the implementation for a referenced symbol. This is common when linking against libraries that are not properly included.

## Common Causes
- Missing framework or library in Link Binary With Libraries
- Objective-C symbol not exposed in bridging header
- Framework built for different platform or architecture
- C++ symbols with name mangling issues

## How to Fix
1. Add the missing framework to Link Binary With Libraries
2. Verify the bridging header includes all required headers
3. Check that framework matches your deployment target
4. Ensure C functions are marked with extern "C" if needed

```swift
// For Objective-C symbols, add to bridging header:
// YourProject-Bridging-Header.h
#import <SomeFramework/SomeHeader.h>

// For C functions, ensure proper declaration:
// In your C header file:
#ifdef __cplusplus
extern "C" {
#endif
void myFunction(void);
#ifdef __cplusplus
}
#endif
```

## Examples
```swift
// Common fix: Adding missing system framework
// If you get: Undefined symbols for architecture arm64:
//   "_OBJC_CLASS_$_CLLocationManager", referenced from:

// Solution: Add CoreLocation.framework
// Target > Build Phases > Link Binary With Libraries
// Click + > Search "CoreLocation" > Add
```
