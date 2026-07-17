---
title: "[Solution] Swift Memory Access Error Fix"
description: "Fix Swift EXC_BAD_ACCESS memory errors. Learn why memory access fails and how to prevent memory safety issues."
languages: ["swift"]
severities: ["error"]
error-types: ["memory-error"]
weight: 5
---

## What This Error Means

An EXC_BAD_ACCESS memory error occurs when your program tries to access memory that it does not have permission to access. This is one of the most severe runtime errors in Swift.

## Common Causes

- Use-after-free (accessing deallocated object)
- Double-free (freeing memory twice)
- Uninitialized pointer access
- Unsafe pointer misuse

## How to Fix

```swift
// WRONG: Use after free
var pointer: UnsafeMutableRawPointer?
pointer = UnsafeMutableRawPointer.allocate(byteCount: 100, alignment: 8)
pointer?.deallocate()
pointer?.storeBytes(of: 0, as: UInt8.self)  // EXC_BAD_ACCESS

// CORRECT: Set to nil after deallocation
pointer?.deallocate()
pointer = nil
```

```swift
// WRONG: Uninitialized pointer
let pointer = UnsafeMutablePointer<Int>.allocate(capacity: 1)
pointer.pointee  // EXC_BAD_ACCESS

// CORRECT: Initialize before use
let pointer = UnsafeMutablePointer<Int>.allocate(capacity: 1)
pointer.initialize(to: 42)
let value = pointer.pointee
pointer.deinitialize(count: 1)
pointer.deallocate()
```

## Examples

```swift
// Example 1: Safe pointer usage
let buffer = UnsafeMutableBufferPointer<Int>.allocate(capacity: 10)
defer { buffer.deallocate() }
for i in 0..<10 {
    buffer[i] = i
}

// Example 2: withUnsafeMutablePointer
withUnsafeMutablePointer(to: &value) { pointer in
    pointer.pointee = 42
}

// Example 3: Enable Address Sanitizer in Xcode
// Edit Scheme > Diagnostics > Enable Address Sanitizer
```

## Related Errors

- [Stack overflow](stack-overflow-swift) — recursion limit
- [Integer overflow](integer-overflow-swift) — arithmetic overflow
- [Out of memory](out-of-memory-swift) — memory exhaustion
