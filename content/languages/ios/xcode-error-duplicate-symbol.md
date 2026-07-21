---
title: "[Solution] Xcode Error: Duplicate Symbol"
description: "Resolve duplicate symbol linker errors in Xcode projects."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Duplicate Symbol

Duplicate symbol errors happen when the same symbol is defined in multiple object files or libraries. The linker cannot determine which implementation to use.

## Common Causes
- Multiple libraries providing the same symbols
- Objective-C category conflicts between frameworks
- Including the same source file in multiple targets
- Static library linked more than once

## How to Fix
1. Use the -force_load flag to resolve specific duplicates
2. Check for overlapping library includes in build phases
3. Use -ObjC linker flag judiciously
4. Remove duplicate source file references from targets

```swift
// Use other linker flags to resolve:
// Build Settings > Other Linker Flags
// Add: -force_load $(BUILT_PRODUCTS_DIR)/libSomeLibrary.a

// Or selectively load symbols:
// -all_load  — load all symbols from all static libraries
// -ObjC      — load all Objective-C categories and classes
// -noall_load — disable all_load
```

## Examples
```swift
// Example: Finding duplicate symbols
// Build with verbose linker output:
// Build Settings > Other Linker Flags > -v

// Look for lines like:
// duplicate symbol '_someFunction' in:
//     libA.a(ObjectA.o)
//     libB.a(ObjectB.o)

// Fix: Remove one of the conflicting libraries
// or rename the symbol in one of the libraries
```
