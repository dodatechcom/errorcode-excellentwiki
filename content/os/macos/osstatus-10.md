---
title: "[Solution] macOS OSStatus -4 (errNotImplemented) — Not Implemented"
description: "Fix macOS OSStatus -4 (errNotImplemented). Resolve not implemented errors in Core Services, Carbon, and legacy Mac framework applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
tags: ["errnotimplemented", "osstatus-4", "not-implemented", "core-services", "carbon", "unavailable"]
weight: 5
---

# macOS OSStatus -4 (errNotImplemented) — Not Implemented

OSStatus -4 (errNotImplemented) indicates that the requested function or operation is not available in the current environment. This error is returned when code attempts to call a function that has not been implemented, or when an API is unavailable on the current platform, OS version, or hardware configuration.

## Common Causes

- The function is not implemented in the current version of macOS or the framework
- The API is platform-specific and not available on the current architecture (e.g., Intel vs. Apple Silicon)
- A driver or hardware abstraction layer does not support the requested operation
- The function is deprecated and has been removed from the current SDK
- A stub function returns this error because the feature was never completed

## How to Fix errNotImplemented

### 1. Check API Availability

Verify the function is available on the target platform:

```swift
// Check API availability
if #available(macOS 13.0, *) {
    // Use the new API
} else {
    // Fall back to an alternative approach
}
```

### 2. Use Runtime Checks

Detect unavailability at runtime:

```swift
guard NSClassFromString("SomeFramework.SomeClass") != nil else {
    print("Framework not available on this system")
    return
}
```

### 3. Review the SDK Version

Ensure the SDK and deployment target support the function:

```bash
# Check the current SDK version
xcrun --show-sdk-path
xcrun --show-sdk-version

# Check deployment target
sw_vers
```

### 4. Use Alternative Frameworks

Replace unavailable functions with modern equivalents:

```swift
// Instead of deprecated Core Services API
// Use FileManager
let fileManager = FileManager.default
let contents = try fileManager.contentsOfDirectory(at: directoryURL, includingPropertiesForKeys: nil)
```

### 5. Implement the Function Yourself

If the system does not provide the function, implement a custom version:

```swift
// Example: custom implementation of a missing function
func customFunctionality() -> Result<Data, Error> {
    // Your custom implementation here
    return .success(Data())
}
```

## Examples

This error commonly occurs when:

- Calling a 32-bit-only API from a 64-bit application
- Using a function that was removed in a recent macOS version
- Calling a Carbon-specific API from a Cocoa-only application
- Attempting to use a feature that requires hardware not present on the system

## Related Error Codes

- paramErr (OSStatus -50) — [Parameter Error](/os/macos/osstatus-9/)
- osLogicError (OSStatus -66) — [Logic Error](/os/macos/osstatus-8/)
- errCoreFoundationUnknown (OSStatus -67000) — [Core Foundation Unknown](/os/macos/osstatus-11/)
- noErr (OSStatus 0) — [No Error](/os/macos/osstatus-0/)
