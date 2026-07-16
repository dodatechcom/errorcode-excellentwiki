---
title: "[Solution] Swift Error — EXC_BAD_ACCESS"
description: "Fix Swift EXC_BAD_ACCESS memory errors. Learn why EXC_BAD_ACCESS occurs and how to fix memory safety issues in Swift code."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["exc-bad-access", "memory", "dangling-pointer", "use-after-free", "deallocation"]
weight: 5
---

# EXC_BAD_ACCESS

`EXC_BAD_ACCESS` occurs when your program attempts to access memory that it is not allowed to use. This is one of the most serious runtime errors in Swift.

## Description

`EXC_BAD_ACCESS` is an operating system signal (Mach exception on macOS/iOS) indicating an illegal memory access. In Swift, this typically happens due to unsafe memory operations, dangling pointers, or use-after-free. While Swift's memory safety prevents most of these, `unsafe` code, Objective-C interop, and concurrency bugs can still cause them.

Common patterns:

- **Dangling pointer** — accessing memory after the object was deallocated.
- **Use-after-free** — referencing an object after it's been released.
- **Unsafe pointer misuse** — incorrect pointer arithmetic or bounds.
- **Concurrency race condition** — simultaneous access to deallocated memory.

## Common Causes

```swift
// Cause 1: Unsafe pointer after deallocation
let ptr = UnsafeMutablePointer<Int>.allocate(capacity: 1)
ptr.initialize(to: 42)
ptr.deallocate()
let value = ptr.pointee // EXC_BAD_ACCESS

// Cause 2: Unowned reference to deallocated object
class Owner {
    unowned let managed: Managed?
    init(_ m: Managed) { managed = m }
}
class Managed {}
var managed: Managed? = Managed()
var owner: Owner? = Owner(managed!)
managed = nil // deallocated
owner?.managed?.description // EXC_BAD_ACCESS

// Cause 3: Unsafe buffer overflow
let buffer = UnsafeMutableBufferPointer<Int>.allocate(capacity: 3)
buffer[10] = 42 // EXC_BAD_ACCESS — out of bounds

// Cause 4: Thread safety with deallocated objects
class SharedObject {
    var data = [Int]()
}
let obj = SharedObject()
DispatchQueue.global().async {
    obj.data.append(1) // May access deallocated memory
}
```

## How to Fix

### Fix 1: Use strong references instead of unowned

```swift
class Container {
    // Wrong
    unowned let child: Child?

    // Correct
    weak var child: Child?
}
```

### Fix 2: Keep references alive during pointer access

```swift
var value = 42
withUnsafePointer(to: &value) { ptr in
    // ptr is only valid inside this closure
    print(ptr.pointee)
}
```

### Fix 3: Validate pointer bounds

```swift
let count = 3
let buffer = UnsafeMutableBufferPointer<Int>.allocate(capacity: count)

// Wrong
buffer[10] = 42

// Correct
for i in 0..<count {
    buffer[i] = i
}
```

### Fix 4: Use actors or locks for shared state

```swift
// Wrong — data race
class Counter {
    var count = 0
    func increment() { count += 1 }
}

// Correct — use actor
actor Counter {
    var count = 0
    func increment() { count += 1 }
}
```

## Examples

```swift
// Example 1: Unowned reference crash
class Parent {
    unowned var child: Child
    init(_ c: Child) { child = c }
}
class Child {}
var child: Child? = Child()
var parent: Parent? = Parent(child!)
child = nil
parent?.child // EXC_BAD_ACCESS

// Example 2: Unsafe pointer from string buffer
let str = "Hello"
str.withCString { cStr in
    let ptr = UnsafeRawPointer(cStr)
    // Accessing after str goes out of scope = EXC_BAD_ACCESS
}
```

## Related Errors

- [Stack Overflow]({{< relref "/languages/swift/stack-overflow" >}}) — stack memory exhaustion.
- [Thread Sanitizer Error]({{< relref "/languages/swift/thread-sanitizer" >}}) — data race detection.
- [Division by Zero]({{< relref "/languages/swift/division-by-zero" >}}) — related runtime crash.
