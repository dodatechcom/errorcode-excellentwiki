---
title: "[Solution] Xcode Error: Linker Command Failed with Exit Code 1"
description: "Resolve linker command failures with exit code 1 in Xcode builds."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Linker Command Failed with Exit Code 1

The linker command failed with exit code 1 when the linker cannot resolve all symbols or find required libraries. This is one of the most common Xcode build errors.

## Common Causes
- Missing frameworks in Link Binary With Libraries
- Incorrect architecture builds being linked together
- Stale build artifacts in DerivedData
- CocoaPods or SPM dependencies not properly resolved

## How to Fix
1. Check the full error message for specific undefined symbols
2. Add missing frameworks to Link Binary With Libraries
3. Clean build folder and derived data
4. Run `pod install` or resolve packages again

```swift
// Clean derived data:
// Xcode > Preferences > Locations > DerivedData > click arrow
// Delete the folder for your project

// Or via terminal:
// $ rm -rf ~/Library/Developer/Xcode/DerivedData/YourProject-*

// For CocoaPods, also run:
// $ pod deintegrate
// $ pod install
```

## Examples
```swift
// Example: Common linker errors and fixes
// Error: Undefined symbols:
//   "_OBJC_CLASS_$_SomeClass"
// Fix: Add SomeFramework.framework to Link Binary With Libraries

// Error: ld: framework not found SomeFramework
// Fix: Add framework to Framework Search Paths
// Build Settings > Framework Search Paths > $(inherited) $(SRCROOT)/Frameworks
```
