---
title: "[Solution] Deprecated Function Migration: NSObject subclassing to Swift structs"
description: "Migrate from deprecated NSObject subclassing to Swift structs and protocols."
deprecated_function: "NSObject subclass"
replacement_function: "struct / protocol"
languages: ["swift"]
deprecated_since: "Swift 1.0+"
---

# [Solution] Deprecated Function Migration: NSObject subclassing to Swift structs

The `NSObject subclass` has been deprecated in favor of `struct / protocol`.

## Migration Guide

Swift structs provide value semantics, better performance, and thread safety.

## Before (Deprecated)

```swift
class UserModel: NSObject {
    @objc dynamic var name: String
    @objc dynamic var age: Int

    init(name: String, age: Int) {
        self.name = name
        self.age = age
        super.init()
    }
}
```

## After (Modern)

```swift
struct UserModel {
    let name: String
    let age: Int
}

protocol Displayable {
    var displayName: String { get }
}

extension UserModel: Displayable {
    var displayName: String { name }
}
```

## Key Differences

- Structs are value types (no shared state)
- No need for @objc dynamic
- Use protocols for shared behavior
- Only use NSObject for Obj-C interop
