---
title: "[Solution] macOS OSStatus -109 (memBadSize) — Bad Memory Size Error"
description: "Fix macOS OSStatus -109 (memBadSize). Resolve bad memory size errors in Core Services, Carbon, and legacy Mac framework applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
tags: ["membadsize", "osstatus-109", "memory", "core-services", "carbon", "invalid-size"]
weight: 5
---

# macOS OSStatus -109 (memBadSize) — Bad Memory Size Error

OSStatus -109 (memBadSize) indicates that an invalid or unsupported memory block size was passed to a memory allocation or deallocation function. This error is returned by legacy Core Services and Carbon memory management APIs when the requested size is negative, zero, or exceeds the maximum allowable allocation for the current memory zone.

## Common Causes

- A negative or zero value was passed as the size parameter to `NewPtr`, `NewHandle`, or similar functions
- The requested allocation size exceeds the maximum allowed by the current heap zone
- Integer overflow in size calculations produced an unexpectedly large value
- A corrupted handle or pointer was passed to a memory management function
- The memory zone was deallocated before the allocation was attempted

## How to Fix memBadSize

### 1. Validate Size Parameters

Ensure all size values are positive and within valid ranges before calling allocation functions:

```c
Size blockSize = CalculateBlockSize();
if (blockSize <= 0) {
    // Handle invalid size
    return paramErr;
}
Ptr ptr = NewPtr(blockSize);
if (ptr == NULL) {
    return memFullErr;
}
```

### 2. Check for Integer Overflow

Verify that size calculations do not overflow:

```c
// Safe size calculation
if (count > 0 && count <= SIZE_MAX / elementSize) {
    Size totalSize = count * elementSize;
    Ptr buffer = NewPtr(totalSize);
} else {
    return paramErr;
}
```

### 3. Verify Handle and Pointer Validity

Check that handles and pointers are valid before use:

```c
if (myHandle == NULL || *myHandle == NULL) {
    // Handle is invalid
    return memBadSize;
}
```

### 4. Use Modern Memory Management

Replace legacy Carbon memory APIs with modern Objective-C or Swift equivalents:

```swift
// Instead of NewPtr
var buffer = [UInt8](repeating: 0, count: Int(blockSize))

// Instead of NewHandle
let data = NSMutableData(length: Int(blockSize))
```

### 5. Inspect Heap Zone Integrity

Check that the memory zone is valid:

```c
THz zone = GetZone();
if (zone == NULL) {
    // Zone is invalid
    return memBadSize;
}
```

## Examples

This error commonly occurs when:

- A legacy application passes a calculated size that overflowed to zero
- A negative offset or size is computed from user input
- A function receives a handle that was already disposed
- A size calculation using `GetHandleSize` returns an unexpected value due to corruption

## Related Error Codes

- memFullErr (OSStatus -108) — [Memory Full](/os/macos/osstatus-1/)
- memErr (OSStatus -10) — [Memory Error](/os/macos/osstatus-3/)
- dsHeapErr (OSStatus -109) — [Heap Error](/os/macos/osstatus-4/)
- paramErr (OSStatus -50) — [Parameter Error](/os/macos/osstatus-9/)
