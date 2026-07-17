---
title: "[Solution] Swift DecodingError Fix"
description: "Fix Swift DecodingError when JSON decoding fails. Learn why Codable decoding fails and how to handle JSON parsing errors."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A `DecodingError` is thrown when `JSONDecoder` cannot decode JSON data into the expected Swift type. This typically happens due to missing keys, type mismatches, or invalid JSON format.

## Common Causes

- Missing required keys in JSON
- Type mismatch (string vs int)
- Nested JSON structure mismatch
- Invalid JSON format

## How to Fix

```swift
// WRONG: Assuming all keys present
struct User: Codable {
    let name: String
    let email: String
}

let json = #"{"name": "Alice"}"#  // Missing "email"
let user = try JSONDecoder().decode(User.self, from: Data(json.utf8))  // DecodingError

// CORRECT: Make optional keys optional
struct User: Codable {
    let name: String
    let email: String?
}
```

```swift
// WRONG: Strict decoding
let json = #"{"name": "Alice", "age": "25"}"#  // age is String, not Int
struct User: Codable {
    let name: String
    let age: Int
}
let user = try JSONDecoder().decode(User.self, from: Data(json.utf8))  // Type mismatch

// CORRECT: Handle type coercion
struct User: Codable {
    let name: String
    let age: Int

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        name = try container.decode(String.self, forKey: .name)
        age = (try? container.decode(Int.self, forKey: .age)) ?? 0
    }
}
```

```swift
// WRONG: Not handling errors
let user = try JSONDecoder().decode(User.self, from: data)

// CORRECT: Handle decoding errors
do {
    let user = try JSONDecoder().decode(User.self, from: data)
} catch let DecodingError.keyNotFound(key, context) {
    print("Missing key: \(key.stringValue)")
} catch let DecodingError.typeMismatch(type, context) {
    print("Type mismatch: expected \(type)")
} catch {
    print("Decoding error: \(error)")
}
```

## Examples

```swift
// Example 1: Safe decoding extension
extension DecodingError {
    var details: String {
        switch self {
        case .keyNotFound(let key, let context):
            return "Missing key '\(key.stringValue)': \(context.debugDescription)"
        case .typeMismatch(let type, let context):
            return "Type mismatch: expected \(type), \(context.debugDescription)"
        case .valueNotFound(let type, let context):
            return "Value not found: expected \(type), \(context.debugDescription)"
        case .dataCorrupted(let context):
            return "Data corrupted: \(context.debugDescription)"
        @unknown default:
            return "Unknown decoding error"
        }
    }
}

// Example 2: Custom decoder
let decoder = JSONDecoder()
decoder.keyDecodingStrategy = .convertFromSnakeCase
decoder.dateDecodingStrategy = .iso8601

// Example 3: Flexible decoding
struct FlexibleUser: Codable {
    let name: String
    let age: Int?

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        name = try container.decode(String.self, forKey: .name)
        age = try? container.decodeIfPresent(Int.self, forKey: .age)
    }
}
```

## Related Errors

- [Encoding error](encoding-error-swift) — JSON encoding failed
- [Nil unwrap error](nil-unwrap-error) — force unwrapping nil
- [Key not found](key-not-found-swift) — dictionary key missing
