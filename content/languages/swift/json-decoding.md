---
title: "[Solution] Swift Error — DecodingError"
description: "Fix Swift DecodingError in JSON decoding. Learn about JSONDecoder errors, why decoding fails, and how to handle malformed JSON gracefully."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# DecodingError

A `DecodingError` is thrown by `JSONDecoder` when the input JSON doesn't match the expected `Decodable` type structure. The error provides details about what went wrong.

## Description

`DecodingError` is an enum with cases like `.keyNotFound`, `.typeMismatch`, `.valueNotFound`, and `.dataCorrupted`. Each case provides context about the failure including the key path and expected type. These errors are common when API responses change or when the Swift model doesn't exactly match the JSON structure.

Common patterns:

- **Missing keys** — JSON missing a required key in the Swift model.
- **Type mismatches** — JSON has a string where Swift expects an Int.
- **Null vs missing** — JSON has `null` where Swift expects a non-optional value.
- **Nested structure mismatch** — deeply nested JSON not matching nested structs.

## Common Causes

```swift
// Cause 1: Missing required key
struct User: Codable {
    let name: String
    let email: String
}
let json = #"{"name": "Alice"}"#.data(using: .utf8)!
let user = try JSONDecoder().decode(User.self, from: json)
// DecodingError.keyNotFound

// Cause 2: Type mismatch
struct Config: Codable {
    let port: Int
}
let json = #"{"port": "8080"}"#.data(using: .utf8)!
let config = try JSONDecoder().decode(Config.self, from: json)
// DecodingError.typeMismatch

// Cause 3: Null value for non-optional
struct Item: Codable {
    let id: Int
}
let json = #"{"id": null}"#.data(using: .utf8)!
let item = try JSONDecoder().decode(Item.self, from: json)
// DecodingError.valueNotFound

// Cause 4: Data corruption
let json = #"{"invalid json"#.data(using: .utf8)!
let data = try JSONDecoder().decode([String: String].self, from: json)
// DecodingError.dataCorrupted
```

## How to Fix

### Fix 1: Make properties optional or provide defaults

```swift
struct User: Codable {
    let name: String
    let email: String? // Optional — won't fail if missing
}

struct Config: Codable {
    let port: Int
    let host: String = "localhost" // Default — won't fail if missing from JSON
}
```

### Fix 2: Use CustomDecodable for flexible parsing

```swift
struct FlexibleUser: Codable {
    let name: String
    let email: String

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        name = try container.decode(String.self, forKey: .name)
        email = try container.decodeIfPresent(String.self, forKey: .email) ?? "unknown"
    }
}
```

### Fix 3: Use try/catch with detailed error info

```swift
do {
    let user = try JSONDecoder().decode(User.self, from: data)
} catch let DecodingError.keyNotFound(key, context) {
    print("Missing key '\(key.stringValue)': \(context.debugDescription)")
} catch let DecodingError.typeMismatch(type, context) {
    print("Type mismatch for \(type): \(context.debugDescription)")
} catch {
    print("Decoding error: \(error)")
}
```

### Fix 4: Use a helper extension for diagnostics

```swift
extension DecodingError {
    var prettyDescription: String {
        switch self {
        case .keyNotFound(let key, let context):
            return "Missing key: \(key.stringValue) — \(context.debugDescription)"
        case .typeMismatch(let type, let context):
            return "Type mismatch: expected \(type) — \(context.debugDescription)"
        case .valueNotFound(let type, let context):
            return "Nil value: expected \(type) — \(context.debugDescription)"
        case .dataCorrupted(let context):
            return "Corrupted data: \(context.debugDescription)"
        @unknown default:
            return "Unknown decoding error"
        }
    }
}
```

## Examples

```swift
// Example 1: API response changed
struct Product: Codable {
    let id: Int
    let title: String
    let price: Double
}
// API adds "discount" field and renames "title" to "name"
let json = #"{"id": 1, "name": "Widget", "price": 9.99, "discount": 0.1}"#
// Decoding fails: key "title" not found

// Example 2: Nested decoding failure
struct Response: Codable {
    let data: [User]
}
let json = #"{"data": [{"name": "Alice", "email": null}]}"#
// DecodingError.valueNotFound if email is non-optional String
```

## Related Errors

- [Key Not Found]({{< relref "/languages/swift/json-key-not-found" >}}) — specific missing key error.
- [Type Mismatch]({{< relref "/languages/swift/json-type-mismatch" >}}) — specific type mismatch error.
- [Encodable/Decodable Error]({{< relref "/languages/swift/codable-error" >}}) — general Codable issues.
