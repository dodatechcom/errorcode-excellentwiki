---
title: "[Solution] Swift Error — Unexpectedly Found Nil"
description: "Fix Swift unexpectedly found nil errors. Learn when nil appears unexpectedly and how to handle optional values defensively."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Unexpectedly Found Nil

This error occurs when a nil value is encountered in a context that expects a non-nil value, typically during force-unwrapping or forced type casting.

## Description

Swift's type system uses optionals to represent the absence of a value. When you bypass nil-checking with `!` or `as!`, you risk a runtime crash if the value is actually nil. This error message can appear in various force-unwrap contexts including dictionary access, optional chaining failures, and API response handling.

Common patterns:

- **API responses** — force-unwrapping optional fields from JSON.
- **Outlets** — accessing `@IBOutlet` before `viewDidLoad`.
- **Core Data** — force-casting optional entity attributes.
- **Notification userInfo** — force-extracting values from `userInfo` dictionary.

## Common Causes

```swift
// Cause 1: Force-unwrapping optional from function
func findUser(id: Int) -> String? {
    return nil
}
let name = findUser(id: 1)! // Fatal error

// Cause 2: Force-casting nil
let value: String? = nil
let text = value as! String // Fatal error

// Cause 3: Force-unwrapping notification info
NotificationCenter.default.post(name: .init("event"), object: nil)
NotificationCenter.default.addObserver(forName: .init("event"), object: nil, queue: nil) { note in
    let data = note.userInfo!["data"]! // Fatal error
}

// Cause 4: Force-unwrapping outlet
class ViewController: UIViewController {
    @IBOutlet var label: UILabel! // nil until view loads
    func setup() {
        label.text = "Hello" // Fatal error if called before load
    }
}
```

## How to Fix

### Fix 1: Use optional chaining

```swift
func findUser(id: Int) -> String? {
    return nil
}

// Wrong
let name = findUser(id: 1)!

// Correct
if let name = findUser(id: 1) {
    print(name)
}
```

### Fix 2: Use guard for early returns

```swift
func process(data: String?) {
    // Wrong
    let d = data!

    // Correct
    guard let d = data else {
        print("No data")
        return
    }
    print(d)
}
```

### Fix 3: Use safe defaults

```swift
let value: String? = nil

// Wrong
let text = value!

// Correct
let text = value ?? "fallback"
```

### Fix 4: Use weak/unowned references properly

```swift
class Manager {
    weak var delegate: Delegate?
    func doWork() {
        // Wrong: delegate?.process()!
        // Correct:
        delegate?.process()
    }
}
```

## Examples

```swift
// Example 1: Force-unwrapping result of optional chain
let dict: [String: [String]] = ["a": ["1", "2"]]
let first = dict["b"]![0] // Fatal error: key "b" not found

// Example 2: Force-unwrapping in interpolation
let name: String? = nil
print("Hello, \(name!)") // Fatal error
```

## Related Errors

- [Unexpectedly Found Nil While Unwrapping]({{< relref "/languages/swift/nil-unwrapping" >}}) — nil during unwrap.
- [Force Unwrap]({{< relref "/languages/swift/force-unwrap" >}}) — force unwrap crash.
- [Could Not Cast Value of Type]({{< relref "/languages/swift/type-casting" >}}) — cast failure.
