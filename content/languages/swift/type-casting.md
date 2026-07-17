---
title: "[Solution] Swift Error — Could Not Cast Value of Type"
description: "Fix Swift type casting errors. Learn why unsafe type casts fail at runtime and how to use conditional casting safely."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Could Not Cast Value of Type

This error occurs when you force-cast (`as!`) an object to a type it doesn't actually conform to. The runtime detects the mismatch and crashes.

## Description

Swift provides `as?` (conditional cast) and `as!` (forced cast) for type casting. The forced cast `as!` will crash if the object isn't of the target type. This commonly happens with heterogeneous collections, `Any` typed values, and decoded JSON data.

Common patterns:

- **Force-casting `Any`** — casting `Any` to a specific type without checking.
- **Wrong generic type** — expecting one type but getting another from an API.
- **Core Data type mismatch** — entity attributes not matching expected types.
- **JSON deserialization** — array elements or dictionary values of unexpected types.

## Common Causes

```swift
// Cause 1: Force-casting Any
let value: Any = "hello"
let number = value as! Int // Fatal error: Could not cast String to Int

// Cause 2: Wrong type from collection
let mixed: [Any] = [1, "two", 3.0]
let str = mixed[1] as! Int // Fatal error: "two" is not Int

// Cause 3: Protocol conformance mismatch
let view: Any = UILabel()
let button = view as! UIButton // Fatal error

// Cause 4: Enum raw value cast
let num: Int = 256
let color = num as! UInt8 // Fatal error: overflow
```

## How to Fix

### Fix 1: Use conditional cast

```swift
let value: Any = "hello"

// Wrong
let number = value as! Int

// Correct
if let number = value as? Int {
    print(number)
} else {
    print("Not an Int")
}
```

### Fix 2: Use guard for early exit

```swift
func process(view: Any) {
    // Wrong
    let button = view as! UIButton

    // Correct
    guard let button = view as? UIButton else { return }
    button.isEnabled = true
}
```

### Fix 3: Use switch for multiple types

```swift
let value: Any = 42

// Wrong
let str = value as! String

// Correct
switch value {
case let str as String:
    print("String: \(str)")
case let num as Int:
    print("Int: \(num)")
default:
    print("Unknown type")
}
```

### Fix 4: Use typed dictionaries instead of `Any`

```swift
// Wrong
let dict: [String: Any] = ["name": "Alice", "age": 30]
let name = dict["name"]! as! String

// Correct — use Codable for structured data
struct User: Codable {
    let name: String
    let age: Int
}
```

## Examples

```swift
// Example 1: Force-casting wrong type
let items: [Any] = [1, 2, 3]
let str = items[0] as! String // Fatal error

// Example 2: Protocol casting
class Animal {}
class Dog: Animal {}
let animal: Animal = Animal()
let dog = animal as! Dog // Fatal error: Animal is not a Dog
```

## Related Errors

- [Unexpectedly Found Nil While Unwrapping]({{< relref "/languages/swift/nil-unwrapping" >}}) — nil unwrap crash.
- [DecodingError]({{< relref "/languages/swift/json-decoding" >}}) — JSON type casting failures.
- [Type Mismatch]({{< relref "/languages/swift/json-type-mismatch" >}}) — JSON type mismatch during decoding.
