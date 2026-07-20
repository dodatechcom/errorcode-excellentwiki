---
title: "[Solution] Swift Codable Super Error — Class Inheritance"
description: "Fix Swift Codable super class errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 121
---

`Codable` super class errors occur when class inheritance chains don't properly call `super.init(from:)` or `super.encode(to:)`, causing missing properties.

## Common Causes

```swift
// Forgetting super.encode(to:)
class Vehicle: Codable {
    let make: String
}

class Car: Vehicle {
    let model: String
    
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(model, forKey: .model)
        // Missing: try super.encode(to: encoder)
    }
}
```

## How to Fix

**1. Call super in encode**

```swift
class Car: Vehicle {
    let model: String
    
    override func encode(to encoder: Encoder) throws {
        try super.encode(to: encoder)
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(model, forKey: .model)
    }
}
```

**2. Call super in decode**

```swift
required init(from decoder: Decoder) throws {
    let container = try decoder.container(keyedBy: CodingKeys.self)
    model = try container.decode(String.self, forKey: .model)
    try super.init(from: decoder)
}
```

**3. Use CodingKeys correctly**

```swift
class Base: Codable {
    let id: UUID
    
    enum CodingKeys: String, CodingKey {
        case id
    }
    
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(id, forKey: .id)
    }
    
    required init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        id = try container.decode(UUID.self, forKey: .id)
    }
}

class Subclass: Base {
    let name: String
    
    enum CodingKeys: String, CodingKey {
        case name
    }
    
    override func encode(to encoder: Encoder) throws {
        try super.encode(to: encoder)
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(name, forKey: .name)
    }
    
    required init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        name = try container.decode(String.self, forKey: .name)
        try super.init(from: decoder)
    }
}
```

**4. Handle stored properties**

```swift
class Person: Codable {
    let name: String
    let age: Int
    
    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }
    
    required init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        name = try container.decode(String.self, forKey: .name)
        age = try container.decode(Int.self, forKey: .age)
    }
}
```

**5. Complete inheritance example**

```swift
class Shape: Codable {
    let color: String
    
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(color, forKey: .color)
    }
    
    required init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        color = try container.decode(String.self, forKey: .color)
    }
}

class Circle: Shape {
    let radius: Double
    
    override func encode(to encoder: Encoder) throws {
        try super.encode(to: encoder)
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(radius, forKey: .radius)
    }
    
    required init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        radius = try container.decode(Double.self, forKey: .radius)
        try super.init(from: decoder)
    }
}
```

## Related Errors

- [Codable Custom Error](/languages/swift/swift-codable-custom-error)
- [JSONDecoder Error](/languages/swift/swift-jsondecoder-error)
- [JSONEncoder Error](/languages/swift/swift-jsonencoder-error)
