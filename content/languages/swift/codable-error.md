---
title: "[Solution] Swift Error — Encodable/Decodable Error"
description: "Fix Swift Codable errors. Learn about common Encodable and Decodable issues, custom coding keys, and complex serialization patterns."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Encodable/Decodable Error

Errors related to Swift's `Codable` protocol occur during encoding (serialization) or decoding (deserialization) of data. These errors can happen with `JSONEncoder`, `JSONDecoder`, `PropertyListEncoder`, or any `Codable` conformance.

## Description

The `Codable` protocol combines `Encodable` and `Decodable`. Errors can occur at compile time (missing conformances) or runtime (encoding/decoding failures). Runtime errors are most common when model types have complex structures, enums with associated values, or when data formats change.

Common patterns:

- **Missing Codable conformance** — using a type with `JSONEncoder` without conforming.
- **Enum encoding issues** — encoding enums with associated values.
- **Date encoding** — default date encoding doesn't match expected format.
- **Nested type encoding** — complex nested structures failing to encode.

## Common Causes

```swift
// Cause 1: Type not Codable
class CustomView: UIView {} // UIView is not Codable
let data = try JSONEncoder().encode(CustomView()) // Compile error

// Cause 2: Enum with associated values — default encoding fails
enum Result: Codable {
    case success(String)
    case failure(Int)
}
let data = try JSONEncoder().encode(Result.success("ok"))
// Runtime error: enums with associated values need custom encoding

// Cause 3: Date encoding format mismatch
struct Event: Codable {
    let date: Date
}
let encoder = JSONEncoder()
let data = try encoder.encode(Event(date: Date()))
// Default encodes as number — API expects string

// Cause 4: Protocol type encoding
func encode<T: Encodable>(_ value: T) throws -> Data {
    return try JSONEncoder().encode(value)
}
let view = UIButton() // UIButton doesn't conform to Encodable
try encode(view) // Compile error
```

## How to Fix

### Fix 1: Add Codable conformance to custom types

```swift
// Wrong — no conformance
class User {
    var name: String
}

// Correct
struct User: Codable {
    let name: String
}
```

### Fix 2: Implement custom encoding for enums

```swift
enum Result: Codable {
    case success(String)
    case failure(Int)

    enum CodingKeys: String, CodingKey {
        case success, failure
    }

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        if let value = try container.decodeIfPresent(String.self, forKey: .success) {
            self = .success(value)
        } else if let value = try container.decodeIfPresent(Int.self, forKey: .failure) {
            self = .failure(value)
        } else {
            throw DecodingError.dataCorrupted(.init(codingPath: [], debugDescription: "Invalid enum"))
        }
    }

    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        switch self {
        case .success(let value):
            try container.encode(value, forKey: .success)
        case .failure(let code):
            try container.encode(code, forKey: .failure)
        }
    }
}
```

### Fix 3: Configure date encoding strategy

```swift
let encoder = JSONEncoder()
encoder.dateEncodingStrategy = .iso8601 // "2024-01-15T10:30:00Z"
let decoder = JSONDecoder()
decoder.dateDecodingStrategy = .iso8601
```

### Fix 4: Use property wrappers for complex encoding

```swift
@propertyWrapper struct StringInt: Codable {
    var wrappedValue: Int

    init(wrappedValue: Int) { self.wrappedValue = wrappedValue }

    init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        let str = try container.decode(String.self)
        wrappedValue = Int(str) ?? 0
    }

    func encode(to encoder: Encoder) throws {
        var container = encoder.singleValueContainer()
        try container.encode(String(wrappedValue))
    }
}
```

## Examples

```swift
// Example 1: Encoding fails on non-Codable property
struct Config: Codable {
    let name: String
    let callback: (String) -> Void // Not Codable
}

// Example 2: Plist encoding with incompatible types
struct Data: Codable {
    let raw: UnsafeRawPointer // Not Codable
}
```

## Related Errors

- [DecodingError]({{< relref "/languages/swift/json-decoding" >}}) — JSON decoding failures.
- [JSON Key Not Found]({{< relref "/languages/swift/json-key-not-found" >}}) — missing keys.
- [JSON Type Mismatch]({{< relref "/languages/swift/json-type-mismatch" >}}) — type mismatches.
