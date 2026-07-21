---
title: "[Solution] Xcode Error: Precompiled Header File Not Found"
description: "Fix missing precompiled header (PCH) file errors in Xcode."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Precompiled Header File Not Found

Precompiled header errors occur when Xcode cannot locate or generate the .pch file. This accelerates compilation by pre-including commonly used headers.

## Common Causes
- PCH file was deleted or moved
- GCC_PREFIX_HEADER build setting points to wrong path
- Header file referenced in PCH not found
- Prefix header not generated for new targets

## How to Fix
1. Verify GCC_PREFIX_HEADER path in Build Settings
2. Ensure the .pch file exists at the specified location
3. Check that all headers referenced in the PCH are available
4. Create a new PCH file if it was accidentally deleted

```swift
// Create a new precompiled header:
// File > New > File > iOS > Header File
// Name it: YourProject-Prefix.pch

// Add common imports:
// #ifdef __OBJC__
//     #import <UIKit/UIKit.h>
//     #import <Foundation/Foundation.h>
// #endif

// In Build Settings:
// Prefix Header = $(SRCROOT)/YourProject-Prefix.pch
// Precompile Prefix Header = YES
```

## Examples
```objc
// Example PCH file content:
#ifdef __OBJC__
    #import <UIKit/UIKit.h>
    #import <Foundation/Foundation.h>
    #import <CoreData/CoreData.h>

    // Custom macros
    #define IS_IPAD (UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPad)
    #define IS_IPHONE (UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPhone)
#endif
```
