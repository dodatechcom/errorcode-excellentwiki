---
title: "[Solution] Swift Thread Sanitizer — Data Race Fix"
description: "Fix Swift Thread Sanitizer data race errors. Learn how to identify and fix concurrent access issues in Swift applications."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["thread-sanitizer", "data-race", "concurrency", "threading", "swift"]
weight: 5
---

# Thread Sanitizer — Data Race Detected

A data race occurs when two or more threads access shared data concurrently, and at least one access is a write.

## Description

Thread Sanitizer (TSan) is a runtime tool that detects data races. A data race is undefined behavior in Swift and can cause crashes, corrupted data, and unpredictable results. This error appears when TSan is enabled and detects concurrent access violations.

Common causes:

- **Unsynchronized shared state** — multiple threads accessing same variable
- **Missing locks** — no synchronization on mutable shared data
- **Collection mutation** — concurrent array/dictionary modification
- **UI updates from background** — updating UI from non-main thread

## Common Causes

```swift
// Cause 1: Unsynchronized counter
class Counter {
    var count = 0
    func increment() {
        count += 1  // Data race if called from multiple threads
    }
}

// Cause 2: Shared dictionary
class Cache {
    var data: [String: Any] = [:]
    func set(_ value: Any, forKey key: String) {
        data[key] = value  // Data race
    }
}

// Cause 3: Background UI update
DispatchQueue.global().async {
    self.label.text = "Updated"  // Data race: UI update from background
}

// Cause 4: Collection mutation
var array: [Int] = []
DispatchQueue.concurrentPerform(iterations: 100) { _ in
    array.append(1)  // Data race
}
```

## How to Fix

### Fix 1: Use serial queue

```swift
// Wrong
class Counter {
    var count = 0
    func increment() {
        count += 1
    }
}

// Correct
class Counter {
    private var count = 0
    private let queue = DispatchQueue(label: "counter")
    func increment() {
        queue.sync {
            count += 1
        }
    }
}
```

### Fix 2: Use actors (Swift 5.5+)

```swift
// Wrong
class Cache {
    var data: [String: Any] = [:]
    func set(_ value: Any, forKey key: String) {
        data[key] = value
    }
}

// Correct
actor Cache {
    var data: [String: Any] = [:]
    func set(_ value: Any, forKey key: String) {
        data[key] = value
    }
}
```

### Fix 3: Dispatch to main for UI

```swift
// Wrong
DispatchQueue.global().async {
    self.label.text = "Updated"
}

// Correct
DispatchQueue.global().async {
    DispatchQueue.main.async {
        self.label.text = "Updated"
    }
}
```

### Fix 4: Use lock for synchronization

```swift
// Wrong
var array: [Int] = []
DispatchQueue.concurrentPerform(iterations: 100) { _ in
    array.append(1)
}

// Correct
let lock = NSLock()
var array: [Int] = []
DispatchQueue.concurrentPerform(iterations: 100) { _ in
    lock.lock()
    array.append(1)
    lock.unlock()
}
```

## Examples

```swift
// Example 1: Thread-safe property wrapper
@propertyWrapper
class ThreadSafe<T> {
    private var value: T
    private let queue = DispatchQueue(label: "threadsafe")
    
    init(wrappedValue: T) {
        self.value = wrappedValue
    }
    
    var wrappedValue: T {
        get { queue.sync { value } }
        set { queue.sync { value = newValue } }
    }
}

class MyClass {
    @ThreadSafe var counter = 0
}

// Example 2: Actor-based thread safety
actor BankAccount {
    var balance: Double = 0
    
    func deposit(_ amount: Double) {
        balance += amount
    }
    
    func withdraw(_ amount: Double) -> Bool {
        guard balance >= amount else { return false }
        balance -= amount
        return true
    }
}
```

## Related Errors

- [Unrecognized Selector]({{< relref "/languages/swift/unrecognized-selector-swift" >}}) — Objective-C method not found
- [Memory Error]({{< relref "/languages/swift/memory-error-swift" >}}) — memory corruption
- [URL Session Error]({{< relref "/languages/swift/url-error-swift" >}}) — network request failed
