---
title: "[Solution] Xcode Error: No Such Module"
description: "Fix Xcode no such module errors when importing frameworks or modules."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: No Such Module

This error occurs when Xcode cannot find a module you are trying to import. The compiler has no knowledge of the module at the specified import path.

## Common Causes
- Module not installed or properly configured
- Missing modulemap or module not built yet
- Incorrect import statement syntax
- Framework search paths not covering the module location

## How to Fix
1. Verify the module is in your project dependencies
2. Check that FRAMEWORK_SEARCH_PATHS includes the module
3. Ensure the module is built before your target
4. Try importing the framework directly instead of the module

```swift
// Instead of module import, try direct framework import:
// WRONG:
import MyModule

// RIGHT:
import MyFramework  // Use the framework name directly

// Or check that the module is properly exposed:
// Ensure the framework has a module.modulemap file
```

## Examples
```swift
// Example: Troubleshooting module imports
// 1. Verify the module exists in DerivedData
ls ~/Library/Developer/Xcode/DerivedData/YourProject-*/Build/Products/

// 2. Check if modulemap is present
ls ~/Library/Developer/Xcode/DerivedData/YourProject-*/Build/Products/Debug-iphoneos/MyFramework.framework/Modules/

// 3. If missing, create a module.modulemap:
module MyFramework {
    umbrella header "MyFramework.h"
    export *
    module * { export * }
}
```
