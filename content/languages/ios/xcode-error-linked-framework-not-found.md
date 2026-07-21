---
title: "[Solution] Xcode Error: Linked Framework Not Found"
description: "Fix Xcode errors about missing linked frameworks in your iOS project."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Linked Framework Not Found

Xcode reports a missing framework when a required framework is referenced in build settings but cannot be located on disk. This prevents the linker from resolving symbols.

## Common Causes
- Framework was deleted or moved from expected location
- Incorrect path in Framework Search Paths
- Framework not added to the project properly
- Derived data contains stale references

## How to Fix
1. Remove the framework from Link Binary With Libraries
2. Re-add the framework using the correct path
3. Update Framework Search Paths to point to the correct location
4. Clean build folder and rebuild

```swift
// Remove stale framework references
// 1. Go to Target > Build Phases > Link Binary With Libraries
// 2. Remove the missing framework entry
// 3. Re-add it from the correct location

// Or use Xcode's "Add Frameworks" via File > Add Files
// Make sure "Copy items if needed" is checked
```

## Examples
```swift
// Example: Properly adding a framework
// After dragging framework into project, verify these settings:

// Build Settings:
// - Always Search User Paths = NO
// - Framework Search Paths = $(inherited) $(SRCROOT)/Frameworks
// - Header Search Paths = $(inherited) $(SRCROOT)/Frameworks

// Build Phases > Link Binary With Libraries:
// - Ensure the framework appears here
```
