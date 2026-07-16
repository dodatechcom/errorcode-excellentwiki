---
title: "[Solution] macOS OSStatus 0 (noErr) — No Error"
description: "Understand macOS OSStatus 0 (noErr). Learn about the noErr constant in Core Services and how to handle successful operation results."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
tags: ["noerr", "osstatus-0", "core-services", "success"]
weight: 5
---

# macOS OSStatus 0 (noErr) — No Error

OSStatus 0 (noErr) is not actually an error — it is the success constant returned by Core Services, Carbon, and other legacy macOS frameworks to indicate that an operation completed without any issues. When you encounter `noErr` in your code, it means the function executed successfully and no error handling is required.

## Common Causes

- The operation completed successfully and returned the standard success code
- A legacy Carbon or Core Services API used `noErr` as its success return value
- The error variable was initialized to `noErr` and was never modified by the called function
- A function returns `noErr` by default when no error condition is detected

## How to Handle noErr

### 1. Check for noErr in Code

Use `noErr` to verify successful operation:

```swift
var error: OSStatus = noErr
SomeCoreServicesFunction(&error)
if error == noErr {
    print("Operation succeeded")
} else {
    print("Operation failed with error: \(error)")
}
```

### 2. Use Swift Error Handling

Modern Swift code typically throws rather than returning `OSStatus`:

```swift
do {
    try someOperation()
    // Success — equivalent to noErr
} catch {
    print("Error: \(error)")
}
```

### 3. Compare Against noErr in Objective-C

In Objective-C, compare the return value directly:

```objective-c
OSStatus status = SomeCoreServicesFunction();
if (status == noErr) {
    NSLog(@"Operation succeeded");
} else {
    NSLog(@"Error: %d", (int)status);
}
```

### 4. Use Modern Framework Equivalents

When possible, migrate from legacy Core Services APIs to modern equivalents that use `throws`:

```swift
// Instead of Core Services with OSStatus
// Use FileManager with throws
try FileManager.default.copyItem(at: source, to: destination)
```

## Examples

noErr is commonly encountered when:

- Checking the return value of a successfully completed `FSCreateFile` call
- Verifying that a `FSSetFinderInfo` operation succeeded
- The result of a `FSRef` or `FSSpec` manipulation that completed without issues
- Default initialization of an `OSStatus` error variable before calling a function

## Related Error Codes

- memFullErr (OSStatus -108) — [Memory Full](/os/macos/osstatus-1/)
- paramErr (OSStatus -50) — [Parameter Error](/os/macos/osstatus-9/)
- errNotImplemented (OSStatus -4) — [Not Implemented](/os/macos/osstatus-10/)
- osLogicError (OSStatus -66) — [Logic Error](/os/macos/osstatus-8/)
