---
title: "[Solution] macOS OSStatus -50 (paramErr) — Parameter Error"
description: "Fix macOS OSStatus -50 (paramErr). Resolve parameter errors in Core Services, Carbon, and legacy Mac framework applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# macOS OSStatus -50 (paramErr) — Parameter Error

OSStatus -50 (paramErr) indicates that one or more parameters passed to a function are invalid, out of range, or incorrectly formatted. This is one of the most common error codes returned by Core Services and Carbon APIs, and it corresponds to the POSIX `EINVAL` error. The function detected that the supplied arguments do not meet the required conditions for successful execution.

## Common Causes

- A required parameter was NULL or nil when the function expects a valid value
- A numeric parameter is outside the valid range for the function
- A parameter has the wrong type or format for the expected input
- A parameter combination is logically inconsistent (e.g., offset beyond data length)
- The function was called before required initialization was completed

## How to Fix paramErr

### 1. Validate All Parameters

Check every parameter before calling the function:

```swift
// Validate parameters before calling a system function
guard let sourceURL = sourceURL else {
    print("Source URL must not be nil")
    return paramErr
}

guard offset >= 0 && offset <= dataLength else {
    print("Offset must be between 0 and \(dataLength)")
    return paramErr
}
```

### 2. Check Parameter Types

Ensure parameters match the expected types:

```c
// Verify parameter types
CFStringRef string = (CFStringRef)parameter;
if (CFGetTypeID(string) != CFStringGetTypeID()) {
    return paramErr;
}
```

### 3. Review Documentation

Consult Apple's documentation for the specific API to understand parameter constraints:

```bash
# Open documentation for a function
open "https://developer.apple.com/documentation"
# Search for the specific function name
```

### 4. Use Defensive Programming

Add precondition checks to catch parameter errors early:

```swift
precondition(offset >= 0, "Offset must be non-negative")
precondition(offset <= data.count, "Offset must not exceed data length")
precondition(!path.isEmpty, "Path must not be empty")
```

### 5. Log Parameter Values

Add logging to diagnose which parameter is causing the error:

```swift
func performOperation(source: URL?, offset: Int, length: Int) -> OSStatus {
    print("source: \(source?.absoluteString ?? "nil")")
    print("offset: \(offset)")
    print("length: \(length)")
    
    guard let source = source else { return paramErr }
    guard offset >= 0, length > 0 else { return paramErr }
    
    return noErr
}
```

## Examples

This error commonly occurs when:

- Passing NULL to a function that requires a valid pointer
- Providing a negative offset to a file read operation
- Calling `FSCreateFile` with an empty filename
- Passing an empty `FSRef` to a file manipulation function
- Supplying mismatched buffer sizes between input and output parameters

## Related Error Codes

- errNotImplemented (OSStatus -4) — [Not Implemented](/os/macos/osstatus-10/)
- osLogicError (OSStatus -66) — [Logic Error](/os/macos/osstatus-8/)
- errNoSuchName (OSStatus -41) — [No Such Name](/os/macos/osstatus-12/)
- noErr (OSStatus 0) — [No Error](/os/macos/osstatus-0/)
