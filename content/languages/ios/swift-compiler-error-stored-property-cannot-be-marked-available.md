---
title: "[Solution] Swift Compiler Error: Stored Property Cannot Be Marked @available"
description: "Fix @available attribute errors on stored properties in Swift."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Stored Property Cannot Be Marked @available

The @available attribute cannot be used on stored properties. It is only valid on types, functions, and other declarations.

## Common Causes
- Attempting to mark stored property with @available
- Misunderstanding @available scope
- Using @available on computed properties (also not allowed)
- @available on global variables (not supported on stored)

## How to Fix
1. Remove @available from stored properties
2. Use @available on the entire type or method instead
3. Check availability at runtime using if #available
4. Move the availability check to the usage site

```swift
// WRONG: @available on stored property
class MyClass {
    @available(iOS 16.0, *)
    var newFeature: String = "value"  // Error

// RIGHT: @available on method or type
class MyClass {
    @available(iOS 16.0, *)
    func useNewFeature() {
        let value = "value"
    }
}

// Or check at runtime:
if #available(iOS 16.0, *) {
    // Use iOS 16+ API
}
```

## Examples
```swift
// Example: Proper @available usage
@available(iOS 15.0, *)
class ModernView: UIView { }

class LegacyView: UIView {
    @available(iOS 15.0, *)
    func configureModern() { }

    func configureLegacy() {
        if #available(iOS 15.0, *) {
            configureModern()
        }
    }
}
```
