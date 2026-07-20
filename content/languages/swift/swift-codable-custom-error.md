---
title: "[Solution] Swift Custom Codable Error — encode/init(from:)"
description: "Fix Swift custom Codable errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 120
---

Custom `Codable` errors occur when `encode(to:)` or `init(from:)` implementations are incorrect, nested containers are misused, or super encoding is missing.

## Common Causes

```swift
// Incorrect encoding order
struct Model: Codable {
    let name: String
    
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(name, forKey: .name)
        // Missing: encode other properties
    }
}
```

## How to Fix

**1. Complete custom encoding**

```swift
struct Event: Codable {
    let id: UUID
    let name: String
    let date: Date
    
    enum CodingKeys: String, CodingKey {
        case id, name, date
    }
    
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(id.uuidString, forKey: .id)
        try container.encode(name, forKey: .name)
        try container.encode(date.timeIntervalSince1970, forKey: .date)
    }
    
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        id = UUID(uuidString: try container.decode(String.self, forKey: .id)) ?? UUID()
        name = try container.decode(String.self, forKey: .name)
        let timestamp = try container.decode(Double.self, forKey: .date)
        date = Date(timeIntervalSince1970: timestamp)
    }
}
```

**2. Handle nested containers**

```swift
struct Address: Codable {
    let street: String
    let city: String
    
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        street = try container.decode(String.self, forKey: .street)
        city = try container.decode(String.self, forKey: .city)
    }
    
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(street, forKey: .street)
        try container.encode(city, forKey: .city)
    }
}
```

**3. Single value container**

```swift
extension Date: @retroactive Codable {
    func encode(to encoder: Encoder) throws {
        var container = encoder.singleValueContainer()
        try container.encode(timeIntervalSince1970)
    }
    
    init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        let timestamp = try container.decode(Double.self)
        self.init(timeIntervalSince1970: timestamp)
    }
}
```

**4. Unkeyed container for arrays**

```swift
struct Matrix: Codable {
    let values: [[Double]]
    
    func encode(to encoder: Encoder) throws {
        var container = encoder.unkeyedContainer()
        for row in values {
            var rowContainer = container.nestedUnkeyedContainer()
            for value in row {
                try rowContainer.encode(value)
            }
        }
    }
}
```

**5. Super encoder for class inheritance**

```swift
class Animal: Codable {
    let name: String
    
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(name, forKey: .name)
    }
    
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        name = try container.decode(String.self, forKey: .name)
    }
}
```

## Examples

Polymorphic Codable:
```swift
enum Shape: Codable {
    case circle(radius: Double)
    case rectangle(width: Double, height: Double)
    
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        switch self {
        case .circle(let radius):
            try container.encode("circle", forKey: .type)
            try container.encode(radius, forKey: .radius)
        case .rectangle(let width, let height):
            try container.encode("rectangle", forKey: .type)
            try container.encode(width, forKey: .width)
            try container.encode(height, forKey: .height)
        }
    }
    
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        let type = try container.decode(String.self, forKey: .type)
        switch type {
        case "circle":
            self = .circle(radius: try container.decode(Double.self, forKey: .radius))
        case "rectangle":
            self = .rectangle(
                width: try container.decode(Double.self, forKey: .width),
                height: try container.decode(Double.self, forKey: .height)
            )
        default:
            throw DecodingError.dataCorruptedError(
                forKey: .type,
                in: container,
                debugDescription: "Unknown shape type"
            )
        }
    }
}
```

## Related Errors

- [Codable Super Error](/languages/swift/swift-codable-super-error)
- [JSONDecoder Error](/languages/swift/swift-jsondecoder-error)
- [JSONEncoder Error](/languages/swift/swift-jsonencoder-error)
