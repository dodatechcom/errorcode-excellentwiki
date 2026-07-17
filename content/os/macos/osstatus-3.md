---
title: "[Solution] macOS OSStatus -10 (memErr) — General Memory Error"
description: "Fix macOS OSStatus -10 (memErr). Resolve general memory errors in Core Services, Carbon, and legacy Mac framework applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# macOS OSStatus -10 (memErr) — General Memory Error

OSStatus -10 (memErr) is a general-purpose memory error code returned by legacy Core Services and Carbon APIs. Unlike `memFullErr` (out of memory) or `memBadSize` (invalid size), `memErr` indicates that a memory management operation failed for an unspecified reason — such as a corrupted pointer, invalid handle, or a failure in the memory zone itself.

## Common Causes

- A corrupted or dangling pointer was passed to a memory management function
- The memory zone or heap has become corrupted
- A handle was locked when it should have been unlocked, or vice versa
- A memory deallocation was attempted on an already-freed block
- The memory manager encountered an internal inconsistency

## How to Fix memErr

### 1. Validate Pointers and Handles

Ensure all pointers and handles are valid before performing memory operations:

```c
Ptr ptr = GetPointerFromSomewhere();
if (ptr == NULL) {
    // Pointer is invalid
    return memErr;
}

// For handles
Handle h = GetHandleFromSomewhere();
if (h == NULL || *h == NULL) {
    return memErr;
}
```

### 2. Check Lock State

Verify the lock state of handles before operations:

```c
if (HGetState(h) & 0x80) {
    // Handle is locked — unlock before disposal
    HUnlock(h);
}
DisposeHandle(h);
```

### 3. Use Memory Debugging Tools

Run the application with memory debugging tools to identify corruption:

```bash
# Enable Guard Malloc (helps detect memory errors)
DYLD_INSERT_LIBRARIES=/usr/lib/libgmalloc.dylib ./YourApp

# Use Instruments Allocations and Leaks
open -a Instruments YourApp
```

### 4. Switch to Modern Memory Management

Replace legacy Carbon memory APIs with ARC-managed Objective-C or Swift objects:

```swift
// Instead of manual Ptr/Handle management
class DataBuffer {
    var data: [UInt8]
    init(size: Int) {
        data = [UInt8](repeating: 0, count: size)
    }
}
```

### 5. Enable Address Sanitizer

Build and run with Address Sanitizer to catch memory errors:

```bash
# In Xcode, add to Other C Flags
-fsanitize=address -fsanitize-address-use-after-scope

# Or via command line
clang -fsanitize=address -g YourFile.c -o YourApp
```

## Examples

This error commonly occurs when:

- A legacy Carbon application uses a disposed handle
- Memory corruption from a buffer overflow corrupts the heap
- A double-free is attempted on a previously deallocated block
- The memory manager's internal state becomes inconsistent after a crash

## Related Error Codes

- memFullErr (OSStatus -108) — [Memory Full](/os/macos/osstatus-1/)
- memBadSize (OSStatus -109) — [Bad Memory Size](/os/macos/osstatus-2/)
- dsHeapErr (OSStatus -109) — [Heap Error](/os/macos/osstatus-4/)
- dsMemoryError (OSStatus -110) — [Memory Error](/os/macos/osstatus-7/)
