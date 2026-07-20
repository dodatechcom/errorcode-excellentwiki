---
title: "[Solution] Swift JSONDecoder Error — dataCorrupted & typeMismatch"
description: "Fix Swift JSONDecoder errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 117
---

`JSONDecoder` errors include `dataCorrupted`, `typeMismatch`, `keyNotFound`, and `valueNotFound` when JSON structure doesn't match the expected model.

## Common Causes

```swift
// Key not in JSON
struct User: Decodable {
    let name: String
    let email: String // JSON has "email_address" instead
}

// Type mismatch
struct Config: Decodable {
    let count: Int // JSON has "count": "five" as string
}
```

## How to Fix

**1. Use CodingKeys for key mapping**

```swift
struct User: Decodable {
    let name: String
    let email: String
    
    enum CodingKeys: String, CodingKey {
        case name
        case email = "email_address"
    }
}
```

**2. Make properties optional**

```swift
struct Config: Decodable {
    let name: String
    let count: Int? // Optional handles missing keys
}
```

**3. Custom decoding**

```swift
struct Model: Decodable {
    let items: [String]
    
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        
        if let single = try? container.decode(String.self, forKey: .items) {
            items = [single]
        } else {
            items = try container.decode([String].self, forKey: .items)
        }
    }
}
```

**4. Handle decode errors gracefully**

```swift
do {
    let model = try decoder.decode(Model.self, from: data)
} catch let DecodingError.keyNotFound(key, context) {
    print("Missing key: \(key.stringValue) at \(context.codingPath)")
} catch let DecodingError.typeMismatch(type, context) {
    print("Type mismatch: expected \(type) at \(context.codingPath)")
} catch let DecodingError.valueNotFound(type, context) {
    print("Nil value for: \(type) at \(context.codingPath)")
} catch let DecodingError.dataCorrupted(context) {
    print("Corrupted data: \(context)")
}
```

**5. Flexible type decoding**

```swift
struct FlexibleInt: Decodable {
    let value: Int
    
    init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        if let int = try? container.decode(Int.self) {
            value = int
        } else if let string = try? container.decode(String.self),
                  let int = Int(string) {
            value = int
        } else {
            throw DecodingError.typeMismatch(
                Int.self,
                DecodingError.Context(
                    codingPath: container.codingPath,
                    debugDescription: "Expected Int or String"
                )
            )
        }
    }
}
```

## Examples

Robust JSON decoding:
```swift
func safeDecode<T: Decodable>(_ type: T.Type, from data: Data) -> Result<T, DecodeError> {
    let decoder = JSONDecoder()
    decoder.keyDecodingStrategy = .convertFromSnakeCase
    decoder.dateDecodingStrategy = .iso8601
    
    do {
        return .success(try decoder.decode(type, from: data))
    } catch {
        return .failure(.decodingFailed(error))
    }
}
```

## Related Errors

- [JSONEncoder Error](/languages/swift/swift-jsonencoder-error)
- [Codable Custom Error](/languages/swift/swift-codable-custom-error)
- [Property List Error](/languages/swift/swift-property-list-error)
