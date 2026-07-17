---
title: "[Solution] Swift Error — JSON Type Mismatch"
description: "Fix Swift JSON type mismatch errors. Learn why JSONDecoder fails when JSON types don't match Swift property types."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# JSON Type Mismatch

This error occurs when `JSONDecoder` finds a value in the JSON that doesn't match the expected Swift type. For example, finding a string where the struct expects an `Int`.

## Description

`DecodingError.typeMismatch` indicates the JSON has a value, but its type doesn't match what the Swift model expects. This commonly happens when APIs return numbers as strings, booleans as integers, or when the JSON structure changes between API versions.

Common patterns:

- **Number as string** — API returns `"42"` instead of `42`.
- **Boolean as integer** — API returns `1` instead of `true`.
- **Array as single value** — API returns an object where an array is expected.
- **String as number** — price field returned as `"$9.99"` instead of `9.99`.

## Common Causes

```swift
// Cause 1: String where Int expected
struct User: Codable {
    let age: Int
}
let json = #"{"age": "25"}"#.data(using: .utf8)!
let user = try JSONDecoder().decode(User.self, from: json)
// DecodingError.typeMismatch

// Cause 2: Int where Bool expected
struct Feature: Codable {
    let enabled: Bool
}
let json = #"{"enabled": 1}"#.data(using: .utf8)!
// DecodingError.typeMismatch

// Cause 3: Object where array expected
struct Response: Codable {
    let items: [String]
}
let json = #"{"items": "single_item"}"#.data(using: .utf8)!
// DecodingError.typeMismatch

// Cause 4: Nested type mismatch
struct Config: Codable {
    let settings: [String: Int]
}
let json = #"{"settings": {"port": "8080"}}"#
// DecodingError.typeMismatch: String vs Int
```

## How to Fix

### Fix 1: Use custom Decodable for flexible types

```swift
struct User: Codable {
    let age: Int

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        // Handle both "age": 25 and "age": "25"
        if let intAge = try? container.decode(Int.self, forKey: .age) {
            age = intAge
        } else if let strAge = try? container.decode(String.self, forKey: .age),
                  let intAge = Int(strAge) {
            age = intAge
        } else {
            age = 0
        }
    }
}
```

### Fix 2: Use a flexible string-or-int decoder

```swift
enum FlexibleInt: Codable {
    case int(Int)
    case string(String)

    var intValue: Int {
        switch self {
        case .int(let v): return v
        case .string(let v): return Int(v) ?? 0
        }
    }

    init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        if let intVal = try? container.decode(Int.self) {
            self = .int(intVal)
        } else if let strVal = try? container.decode(String.self) {
            self = .string(strVal)
        } else {
            throw DecodingError.typeMismatch(Int.self,
                DecodingError.Context(codingPath: decoder.codingPath,
                    debugDescription: "Expected Int or String"))
        }
    }
}
```

### Fix 3: Use JSONDecoder key/date strategies

```swift
let decoder = JSONDecoder()
decoder.keyDecodingStrategy = .convertFromSnakeCase
decoder.dateDecodingStrategy = .iso8601
// This handles some type mismatches automatically
```

### Fix 4: Validate with a wrapper type

```swift
@propertyWrapper struct FlexibleBool: Codable {
    var wrappedValue: Bool

    init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        if let bool = try? container.decode(Bool.self) {
            wrappedValue = bool
        } else if let int = try? container.decode(Int.self) {
            wrappedValue = int != 0
        } else if let str = try? container.decode(String.self) {
            wrappedValue = str.lowercased() == "true"
        } else {
            wrappedValue = false
        }
    }
}
```

## Examples

```swift
// Example 1: API returns price as "$9.99"
struct Product: Codable {
    let price: Double
}
let json = #"{"price": "$9.99"}"#.data(using: .utf8)!
// Type mismatch: expected Double, found String

// Example 2: Null type confusion
struct Config: Codable {
    let port: Int
}
let json = #"{"port": "8080"}"#.data(using: .utf8)!
// Type mismatch: expected Int, found String
```

## Related Errors

- [DecodingError]({{< relref "/languages/swift/json-decoding" >}}) — general JSON decoding error.
- [Key Not Found]({{< relref "/languages/swift/json-key-not-found" >}}) — missing key in JSON.
- [Could Not Cast Value of Type]({{< relref "/languages/swift/type-casting" >}}) — runtime type cast failure.
