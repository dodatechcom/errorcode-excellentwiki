---
title: "[Solution] Swift Out of Memory Error Fix"
description: "Fix Swift out of memory errors. Learn why memory exhaustion occurs and how to optimize memory usage in Swift apps."
languages: ["swift"]
severities: ["error"]
error-types: ["memory-error"]
tags: ["out-of-memory", "memory", "allocation", "swift"]
weight: 5
---

## What This Error Means

An out of memory error occurs when your Swift app exhausts available memory. This typically happens due to large data allocations, memory leaks, or retain cycles that prevent memory from being freed.

## Common Causes

- Loading very large data sets into memory
- Retain cycles in closures
- Unbounded cache growth
- Large image/data processing without streaming

## How to Fix

```swift
// WRONG: Loading all data into memory
let hugeData = try Data(contentsOf: largeFileURL)  // Memory spike

// CORRECT: Stream data instead
let handle = try FileHandle(forReadingFrom: largeFileURL)
while let chunk = handle.readData(ofLength: 1024) {
    processChunk(chunk)
}
```

```swift
// WRONG: Retain cycle in closure
class ViewController: UIViewController {
    var handler: (() -> Void)?
    func setup() {
        handler = {
            self.updateUI()  // Strong reference to self
        }
    }
}

// CORRECT: Use weak self
class ViewController: UIViewController {
    var handler: (() -> Void)?
    func setup() {
        handler = { [weak self] in
            self?.updateUI()
        }
    }
}
```

```swift
// WRONG: Unbounded cache
var cache: [String: Data] = [:]
func cacheData(_ key: String, data: Data) {
    cache[key] = data  // Grows forever
}

// CORRECT: Limit cache size
class LRUCache<Key: Hashable, Value> {
    var cache: [Key: Value] = [:]
    let maxSize: Int
    init(maxSize: Int) { self.maxSize = maxSize }
    func set(_ key: Key, value: Value) {
        if cache.count >= maxSize {
            cache.removeValue(forKey: cache.keys.first!)
        }
        cache[key] = value
    }
}
```

## Examples

```swift
// Example 1: Monitor memory
func memoryUsage() -> UInt64 {
    var info = mach_task_basic_info()
    var count = mach_msg_type_number_t(MemoryLayout<mach_task_basic_info>.size) / 4
    let result = withUnsafeMutablePointer(to: &info) {
        $0.withMemoryRebound(to: integer_t.self, capacity: 1) {
            task_info(mach_task_self_, task_flavor_t(MACH_TASK_BASIC_INFO), $0, &count)
        }
    }
    return result == KERN_SUCCESS ? info.resident_size : 0
}

// Example 2: Lazy loading
lazy var expensiveView: UIView = {
    let view = UIView()
    // Expensive setup
    return view
}()

// Example 3: Autorelease pool for loops
for i in 0..<10000 {
    autoreleasepool {
        let image = processImage(at: i)
    }
}
```

## Related Errors

- [Memory access error](memory-access-error) — EXC_BAD_ACCESS
- [Stack overflow](stack-overflow-swift) — recursion limit
- [Integer overflow](integer-overflow-swift) — arithmetic overflow
