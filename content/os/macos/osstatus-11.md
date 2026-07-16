---
title: "[Solution] macOS OSStatus -67000 (errCoreFoundationUnknown) — Core Foundation Unknown Error"
description: "Fix macOS OSStatus -67000 (errCoreFoundationUnknown). Resolve Core Foundation unknown errors in Cocoa and Core Services applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
tags: ["errcorefoundationunknown", "osstatus-67000", "core-foundation", "cocoa", "unknown-error"]
weight: 5
---

# macOS OSStatus -67000 (errCoreFoundationUnknown) — Core Foundation Unknown Error

OSStatus -67000 (errCoreFoundationUnknown) is a generic error code returned by the Core Foundation framework when an operation fails for an unspecified reason. This error typically occurs when a Core Foundation type conversion, property list operation, or data serialization task encounters an unexpected condition that does not map to a more specific error code.

## Common Causes

- A Core Foundation type conversion failed due to incompatible input data
- A property list serialization or deserialization encountered malformed data
- A Core Foundation object was in an unexpected state during the operation
- A CFString, CFData, or CFURL operation failed due to invalid input
- An internal Core Foundation error occurred that does not have a specific code

## How to Fix errCoreFoundationUnknown

### 1. Validate Input Data

Ensure input data is well-formed before passing it to Core Foundation:

```swift
// Validate data before CF operations
guard let plist = try? PropertyListSerialization.propertyList(from: data, format: nil) else {
    print("Data is not a valid property list")
    return
}
```

### 2. Check Type Compatibility

Verify that Core Foundation types are compatible before conversion:

```swift
// Check type before casting
if CFGetTypeID(cfObject) == CFStringGetTypeID() {
    let string = cfObject as! String
} else {
    print("Object is not a CFString")
}
```

### 3. Use Swift-Native APIs

Replace Core Foundation calls with Swift equivalents when possible:

```swift
// Instead of CFPropertyListCreateWithData
let plist = try PropertyListSerialization.propertyList(from: data, format: nil)

// Instead of CFStringCreateCopy
let copy = string as String
```

### 4. Enable Core Foundation Error Logging

Add logging around Core Foundation operations:

```swift
let result = CFURLCreateStringByAddingPercentEscapes(
    nil, url as CFString, nil, nil,
    CFStringBuiltInEncodings.UTF8.rawValue
)
if result == nil {
    print("CFURLCreateStringByAddingPercentEscapes failed")
}
```

### 5. Check for Nil Core Foundation Objects

Always verify Core Foundation objects are not nil before use:

```swift
let cfString = CFStringCreateWithCString(kCFAllocatorDefault, cString, CFStringBuiltInEncodings.UTF8.rawValue)
guard let string = cfString as String? else {
    print("Failed to create CFString")
    return
}
```

## Examples

This error commonly occurs when:

- Attempting to deserialize a corrupted or truncated property list file
- Converting between incompatible Core Foundation types (e.g., CFNumber to CFString)
- Using a CFString with an encoding that does not match the byte sequence
- A CFDictionary operation fails because a required key is missing

## Related Error Codes

- osLogicError (OSStatus -66) — [Logic Error](/os/macos/osstatus-8/)
- paramErr (OSStatus -50) — [Parameter Error](/os/macos/osstatus-9/)
- errNotImplemented (OSStatus -4) — [Not Implemented](/os/macos/osstatus-10/)
- errNoSuchName (OSStatus -41) — [No Such Name](/os/macos/osstatus-12/)
