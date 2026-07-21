---
title: "[Solution] Xcode Error: Command Ld Failed"
description: "Fix linker command (ld) failures in Xcode iOS builds."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Command Ld Failed

The ld command failure indicates the linker encountered an error while combining object files. This is a general linker error with many possible specific causes.

## Common Causes
- Undefined symbols from missing frameworks
- Architecture mismatches between libraries
- Duplicate symbols across linked libraries
- Framework search paths misconfigured

## How to Fix
1. Examine the full error output for specific symbol names
2. Add any missing frameworks to the link phase
3. Verify all architectures are consistent across libraries
4. Use verbose linker output to diagnose the issue

```swift
// Enable verbose linker output:
// Build Settings > Other Linker Flags > -v

// For specific symbol issues, use:
// Build Settings > Other Linker Flags > -u _symbolName

// This forces the linker to include a specific symbol
```

## Examples
```swift
// Example: Common ld errors and solutions
// ld: warning: directory not found for option '-F/path/to/Frameworks'
// Fix: Update Framework Search Paths in Build Settings

// ld: framework not found SomeFramework
// Fix: Add the framework to your project or update search paths

// ld: Undefined symbols:
// Fix: Add the missing framework to Link Binary With Libraries
```
