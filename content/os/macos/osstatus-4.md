---
title: "[Solution] macOS OSStatus -109 (dsHeapErr) — Heap Error"
description: "Fix macOS OSStatus -109 (dsHeapErr). Resolve heap errors in Core Services, Carbon, and legacy Mac framework applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# macOS OSStatus -109 (dsHeapErr) — Heap Error

OSStatus -109 (dsHeapErr) indicates that the system heap or application heap is corrupted or has encountered an invalid state. This error is returned by legacy Core Services and Carbon memory management APIs when heap integrity checks fail, such as when a corrupted heap header is detected or when a block cannot be found in the expected heap zone.

## Common Causes

- The application heap has been corrupted by a buffer overflow or dangling pointer
- A heap block's header has been overwritten, causing integrity check failures
- The heap zone was deallocated or invalidated before the operation
- A misaligned pointer was used to access a heap block
- Multiple heaps were accessed in an unsafe manner from different threads

## How to Fix dsHeapErr

### 1. Enable Heap Checking

Use macOS debugging tools to validate heap integrity:

```bash
# Run with Guard Malloc to detect heap corruption
DYLD_INSERT_LIBRARIES=/usr/lib/libgmalloc.dylib ./YourApp

# Enable Malloc Scribble to detect use-after-free
sudo sysctl -w malloc_scribble=1
```

### 2. Use Instruments for Heap Analysis

Analyze heap usage with Xcode Instruments:

```bash
# Open Instruments with the Allocations template
open -a Instruments --args YourApp -template "Allocations"

# Or use the Leaks template
open -a Instruments --args YourApp -template "Leaks"
```

### 3. Validate Heap State Before Operations

Check heap integrity in critical code paths:

```c
THz appZone = AppZone();
if (appZone == NULL) {
    // App zone is invalid
    return dsHeapErr;
}
```

### 4. Avoid Cross-Heap Access

Ensure memory operations use the correct heap zone:

```c
// Allocate in the correct zone
THz currentZone = GetZone();
SetZone(GetAppZone());
Ptr ptr = NewPtr(blockSize);
SetZone(currentZone);
```

### 5. Migrate to Modern Memory Management

Replace legacy heap operations with ARC-managed objects:

```swift
// Use classes managed by ARC instead of manual heap allocation
class HeapObject {
    private var buffer: UnsafeMutableRawPointer?
    
    init(size: Int) {
        buffer = UnsafeMutableRawPointer.allocate(byteCount: size, alignment: MemoryLayout<UInt8>.alignment)
    }
    
    deinit {
        buffer?.deallocate()
    }
}
```

## Examples

This error commonly occurs when:

- A legacy application writes past the end of a heap-allocated buffer
- A heap block is used after being freed (use-after-free)
- The application tries to allocate memory after the heap has been destroyed
- A thread-safety issue causes concurrent modification of the heap structure

## Related Error Codes

- memFullErr (OSStatus -108) — [Memory Full](/os/macos/osstatus-1/)
- memErr (OSStatus -10) — [Memory Error](/os/macos/osstatus-3/)
- dsMemoryError (OSStatus -110) — [Memory Error](/os/macos/osstatus-7/)
- dsBusError (OSStatus -2) — [Bus Error](/os/macos/osstatus-5/)
