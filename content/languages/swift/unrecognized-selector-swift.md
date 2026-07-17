---
title: "[Solution] Swift Unrecognized Selector Crash Fix"
description: "Fix Swift unrecognized selector crashes. Learn why this Objective-C runtime error occurs and how to prevent it with type safety."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Unrecognized Selector — Unrecognized Selector Crash

An unrecognized selector crash occurs when you call a method that doesn't exist on an Objective-C object.

## Description

This error originates from Objective-C's dynamic dispatch system. When you call a method on an NSObject subclass that doesn't implement that method, the runtime raises this fatal error. Swift's type system prevents most cases, but it can still happen with Objective-C interop.

Common causes:

- **Selector typo** — misspelling selector in `perform(_:with:)`
- **Missing method implementation** — method declared but not implemented
- **KVO issues** — observing key paths that don't exist
- **Notification center** — calling selector that doesn't exist

## Common Causes

```swift
// Cause 1: Selector typo
let button = UIButton()
button.addTarget(self, action: #selector(tappped), for: .touchUpInside)  // Typo

// Cause 2: Missing method
class MyController: UIViewController {
    @objc func handleTap() {}  // Implementation exists
    // But calling #selector(missingMethod) crashes
}

// Cause 3: KVO without proper key path
class Person: NSObject {
    var name: String = ""
}
let person = Person()
person.addObserver(self, forKeyPath: "nme", options: .new, context: nil)  // Typo

// Cause 4: perform selector
let object = NSObject()
object.perform(Selector(("nonexistentMethod")))
```

## How to Fix

### Fix 1: Use compiler-checked selectors

```swift
// Wrong
button.addTarget(self, action: #selector(tappped), for: .touchUpInside)  // Typo

// Correct
@objc func tapped() {}
button.addTarget(self, action: #selector(tapped), for: .touchUpInside)
```

### Fix 2: Check responds to selector

```swift
// Wrong
object.perform(Selector(("method")))

// Correct
if object.responds(to: Selector(("method"))) {
    object.perform(Selector(("method")))
}
```

### Fix 3: Use #selector with type safety

```swift
// Wrong
let selector = NSSelectorFromString("handleTap")
controller.perform(selector)

// Correct
@objc func handleTap() {}
let selector = #selector(handleTap)
controller.perform(selector)
```

### Fix 4: Use proper KVO

```swift
// Wrong
person.addObserver(self, forKeyPath: "nme", options: .new, context: nil)

// Correct
person.addObserver(self, forKeyPath: #keyPath(Person.name), options: .new, context: nil)
```

## Examples

```swift
// Example 1: Safe selector usage
class ViewController: UIViewController {
    @objc func buttonTapped() {
        print("Button tapped")
    }
    
    func setupButton() {
        let button = UIButton()
        button.addTarget(self, action: #selector(buttonTapped), for: .touchUpInside)
    }
}

// Example 2: Responds to selector check
if myObject.responds(to: #selector(myMethod)) {
    myObject.perform(#selector(myMethod))
}
```

## Related Errors

- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}}) — undefined method (Ruby equivalent)
- [Thread Sanitizer]({{< relref "/languages/swift/thread-sanitizer" >}}) — data race detection
- [Memory Error]({{< relref "/languages/swift/memory-error-swift" >}}) — memory corruption
