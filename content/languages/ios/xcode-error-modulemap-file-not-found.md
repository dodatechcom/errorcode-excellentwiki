---
title: "[Solution] Xcode Error: Modulemap File Not Found"
description: "Fix missing modulemap file errors when importing frameworks in Xcode."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Modulemap File Not Found

This error appears when Xcode cannot locate the module.modulemap file for a framework. It is common when integrating third-party libraries or custom frameworks.

## Common Causes
- Framework not properly installed or linked
- Incorrect FRAMEWORK_SEARCH_PATHS configuration
- Missing or corrupted modulemap file in framework bundle
- Swift version mismatch between project and framework

## How to Fix
1. Verify FRAMEWORK_SEARCH_PATHS includes the framework location
2. Reinstall the framework using the package manager
3. Clean derived data and rebuild the project
4. Ensure the framework contains a valid modulemap

```swift
// Check your framework search paths in Build Settings
// FRAMEWORK_SEARCH_PATHS should include:
// $(inherited)
// $(PROJECT_DIR)/Pods/Frameworks
// $(SRCROOT)/Carthage/Build/iOS

// If using SPM, verify package dependencies are resolved
// File > Packages > Reset Package Caches
```

## Examples
```swift
// Example: Setting up framework search paths programmatically
let frameworkSearchPaths = [
    "$(inherited)",
    "$(PROJECT_DIR)/ThirdParty/Frameworks",
    "$(SDKROOT)/System/Library/Frameworks"
]
// Add these in Build Settings > Framework Search Paths
```
