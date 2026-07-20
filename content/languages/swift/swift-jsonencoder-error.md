---
title: "[Solution] Swift JSONEncoder Error — Date Strategy & Encoding"
description: "Fix Swift JSONEncoder errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 116
---

`JSONEncoder` errors occur when date encoding strategies are misconfigured, key strategies produce invalid keys, or encoding fails due to type incompatibilities.

## Common Causes

```swift
// Default date encoding produces incorrect format
let encoder = JSONEncoder()
let data = try encoder.encode(event) // Date as number

// Key strategy mismatch
encoder.keyEncodingStrategy = .convertToSnakeCase
// Expects snake_case keys but model uses camelCase
```

## How to Fix

**1. Configure date encoding strategy**

```swift
let encoder = JSONEncoder()
encoder.dateEncodingStrategy = .iso8601
encoder.keyEncodingStrategy = .convertToSnakeCase

let data = try encoder.encode(model)
```

**2. Use custom date encoding**

```swift
encoder.dateEncodingStrategy = .custom { date, encoder in
    var container = encoder.singleValueContainer()
    let formatter = DateFormatter()
    formatter.dateFormat = "yyyy-MM-dd"
    try container.encode(formatter.string(from: date))
}
```

**3. Handle encoding errors**

```swift
do {
    let data = try encoder.encode(model)
    let json = String(data: data, encoding: .utf8)
    print(json ?? "Invalid encoding")
} catch let encodingError as EncodingError {
    switch encodingError {
    case .invalidValue(let value, let context):
        print("Invalid \(value) at \(context.debugDescription)")
    @unknown default:
        print("Unknown encoding error")
    }
}
```

**4. Output formatting**

```swift
encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
let data = try encoder.encode(model)
```

**5. Encode nested containers**

```swift
struct CustomEncodable: Encodable {
    let name: String
    
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(name, forKey: .name)
    }
}
```

## Examples

Complete encoder setup:
```swift
func makeEncoder() -> JSONEncoder {
    let encoder = JSONEncoder()
    encoder.dateEncodingStrategy = .iso8601
    encoder.keyEncodingStrategy = .convertToSnakeCase
    encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
    encoder.nonConformingFloatEncodingStrategy = .convertToString(
        positiveInfinity: "Infinity",
        negativeInfinity: "-Infinity",
        nan: "NaN"
    )
    return encoder
}
```

## Related Errors

- [JSONDecoder Error](/languages/swift/swift-jsondecoder-error)
- [Codable Custom Error](/languages/swift/swift-codable-custom-error)
- [Codable Super Error](/languages/swift/swift-codable-super-error)
