---
title: "[Solution] macOS Universal Binary Error"
description: "Fix universal binary errors on Mac when apps crash on Intel or Apple Silicon, or lipo/fat binary issues occur."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# macOS Universal Binary Error Fix

Universal binary errors occur when a fat binary contains incompatible architectures, has corrupt slices, or lacks the expected architecture for the current hardware.

## What This Error Means

A universal binary contains multiple architecture slices (arm64 + x86_64). macOS selects the matching slice at launch. Errors happen when a required slice is missing, corrupt, or has incompatible linked frameworks.

## Common Causes

- Universal binary missing the required architecture
- One slice was built with different SDK or deployment target
- Corrupt binary due to incomplete build
- `lipo` extraction left a partial binary
- Framework dependency only available for one architecture

## How to Fix

### 1. Inspect the binary

```bash
# Check architectures in a binary
lipo -info /Applications/MyApp.app/Contents/MacOS/MyApp

# List detailed architecture info
lipo -detailed_info /Applications/MyApp.app/Contents/MacOS/MyApp
```

### 2. Create a proper universal binary

```bash
# Combine arm64 and x86_64 binaries
lipo -create arm64_binary x86_64_binary -output universal_binary

# Verify the result
lipo -info universal_binary
```

### 3. Extract a specific architecture

```bash
# Extract arm64 slice
lipo MyApp -thin arm64 -output MyApp_arm64

# Extract x86_64 slice
lipo MyApp -thin x86_64 -output MyApp_x86_64
```

### 4. Fix missing frameworks

```bash
# Check which architectures a framework supports
lipo -info /System/Library/Frameworks/SomeFramework.framework/SomeFramework

# Ensure all frameworks in your app support both architectures
find MyApp.app -name "*.framework" -exec lipo -info {} \;
```

## Related Errors

- [M1 Error](macos-m1-error) — Apple Silicon compatibility issues
- [Rosetta Error](macos-rosetta-error) — translation failures
- [Xcode Error](macos-xcode-error) — build configuration issues
