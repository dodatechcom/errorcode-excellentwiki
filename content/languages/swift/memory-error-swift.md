---
title: "[Solution] Swift Memory Error — Heap Corruption Fix"
description: "Fix Swift memory errors and heap corruption. Learn how to identify and resolve memory management issues in Swift."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Memory Error — Heap Corruption / Memory Error

Memory errors occur when Swift's memory management is violated, leading to crashes, corruption, or unexpected behavior.

## Description

Swift uses Automatic Reference Counting (ARC) for memory management. Memory errors happen when references are incorrectly managed, leading to use-after-free, double-free, or heap corruption.

Common causes:

- **Retain cycles** — strong reference cycles between objects
- **Use after free** — accessing deallocated memory
- **Unmanaged memory** — unsafe pointer operations
- **Buffer overflow** — writing beyond allocated memory

## Common Causes

```swift
// Cause 1: Retain cycle
class ViewController {
    var closure: (() -> Void)?
    func setup() {
        closure = {
            self.doSomething()  // Strong capture of self
        }
    }
}

// Cause 2: Unsafe pointer
let ptr = UnsafeMutablePointer<Int>.allocate(capacity: 1)
ptr.pointee = 42
ptr.deallocate()
print(ptr.pointee)  // Use after free

// Cause 3: Buffer overflow
let buffer = UnsafeMutableBufferPointer<Int>.allocate(capacity: 3)
buffer[0] = 1
buffer[1] = 2
buffer[2] = 3
buffer[3] = 4  // Buffer overflow

// Cause 4: Double free
let ptr = UnsafeMutablePointer<Int>.allocate(capacity: 1)
ptr.deallocate()
ptr.deallocate()  // Double free
```

## How to Fix

### Fix 1: Use weak self

```swift
// Wrong
class ViewController {
    var closure: (() -> Void)?
    func setup() {
        closure = {
            self.doSomething()
        }
    }
}

// Correct
class ViewController {
    var closure: (() -> Void)?
    func setup() {
        closure = { [weak self] in
            self?.doSomething()
        }
    }
}
```

### Fix 2: Use unowned for non-optional references

```swift
// Wrong
class ViewController {
    var closure: (() -> Void)?
    func setup() {
        closure = {
            self.doSomething()
        }
    }
}

// Correct
class ViewController {
    var closure: (() -> Void)?
    func setup() {
        closure = { [unowned self] in
            self.doSomething()
        }
    }
}
```

### Fix 3: Use defer for cleanup

```swift
// Wrong
let ptr = UnsafeMutablePointer<Int>.allocate(capacity: 1)
ptr.pointee = 42
// Use ptr
ptr.deallocate()

// Correct
let ptr = UnsafeMutablePointer<Int>.allocate(capacity: 1)
defer { ptr.deallocate() }
ptr.pointee = 42
// Use ptr
```

### Fix 4: Use withUnsafeMutableBufferPointer

```swift
// Wrong
let buffer = UnsafeMutableBufferPointer<Int>.allocate(capacity: 3)
buffer[0] = 1
buffer.deallocate()

// Correct
let count = 3
let result = [Int](unsafeUninitializedCapacity: count) { buffer, initializedCount in
    buffer[0] = 1
    buffer[1] = 2
    buffer[2] = 3
    initializedCount = 3
}
```

## Examples

```swift
// Example 1: Avoiding retain cycle
class NetworkManager {
    var completionHandler: ((Data?) -> Void)?
    
    func fetchData() {
        completionHandler = { [weak self] data in
            guard let self = self else { return }
            self.processData(data)
        }
    }
}

// Example 2: Safe memory management
class Buffer {
    private let pointer: UnsafeMutableBufferPointer<UInt8>
    
    init(size: Int) {
        pointer = UnsafeMutableBufferPointer<UInt8>.allocate(capacity: size)
    }
    
    deinit {
        pointer.deallocate()
    }
}
```

## Related Errors

- [Thread Sanitizer]({{< relref "/languages/swift/thread-sanitizer" >}}) — data race detection
- [Unrecognized Selector]({{< relref "/languages/swift/unrecognized-selector-swift" >}}) — Objective-C method not found
- [Nil Unwrap]({{< relref "/languages/swift/nil-unwrap" >}}) — force unwrapping nil
