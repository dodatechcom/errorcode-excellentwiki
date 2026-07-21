---
title: "[Solution] Xcode Build Error: Missing Required Architecture"
description: "Fix Xcode missing required architecture build errors for arm64 and x86_64 simulators."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Build Error: Missing Required Architecture

This error occurs when Xcode cannot find a required architecture slice for a target device or simulator. It typically appears as "missing required architecture arm64" or similar during the build process.

## Common Causes
- Building for simulator with device-only frameworks
- Invalid architecture settings in build configuration
- Third-party libraries compiled for wrong architectures
- Mixing arm64 and x86_64 slices incorrectly

## How to Fix
1. Check VALID_ARCHS and ARCHS build settings in your target
2. Ensure all frameworks support both architectures
3. Clean the build folder with Shift+Cmd+K
4. Remove VALID_ARCHS and let Xcode auto-resolve architectures

```swift
// In your Podfile, ensure excluded architectures are correct
post_install do |installer|
  installer.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      config.build_settings['EXCLUDED_ARCHS[sdk=iphonesimulator*]'] = 'arm64'
    end
  end
end
```

## Examples
```swift
// If you see this during build:
// "missing required architecture arm64 in file"
// Check your project's build settings:

// Go to Build Settings > Architectures
// Set Architectures to: $(ARCHS_STANDARD)

// For Xcode 12+ with M1 Macs:
// Build Settings > Excluded Architectures
// Set: Any SDK = arm64 (for simulator builds only)
```
