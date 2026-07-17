---
title: "[Solution] Swift EncodingError Fix"
description: "Fix Swift EncodingError when JSON encoding fails. Learn why Codable encoding fails and how to handle JSON serialization errors."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["encoding", "json", "codable", "swift"]
weight: 5
---

## What This Error Means

An `EncodingError` is thrown when `JSONEncoder` cannot encode a Swift type into JSON data. This can happen when the type contains values that cannot be represented in JSON, like `Date` without proper formatting or `URL` without string conversion.

## Common Causes

- Non-encodable values (Date, URL, etc.)
- Nil values in non-optional properties
- Custom types without Codable conformance
- Encoding strategy mismatch

## How to Fix

```swift
// WRONG: Date not encodable
struct Event: Codable {
    let name: String
    let date: Date  // Date needs encoding strategy
}

let encoder = JSONEncoder()
let data = try encoder.encode(event)  // May fail

// CORRECT: Set date encoding strategy
let encoder = JSONEncoder()
encoder.dateEncodingStrategy = .iso8601
let data = try encoder.encode(event)
```

```swift
// WRONG: URL not directly encodable
struct Link: Codable {
    let name: String
    let url: URL  // URL needs conversion
}

// CORRECT: Use custom encoding
struct Link: Codable {
    let name: String
    let url: URL

    enum CodingKeys: String, CodingKey {
        case name, url
    }

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        name = try container.decode(String.self, forKey: .name)
        url = try container.decode(URL.self, forKey: .url)
    }

    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(name, forKey: .name)
        try container.encode(url.absoluteString, forKey: .url)
    }
}
```

```swift
// WRONG: Not handling encoding errors
let data = try JSONEncoder().encode(object)

// CORRECT: Handle encoding errors
do {
    let data = try JSONEncoder().encode(object)
} catch let EncodingError.invalidValue(value, context) {
    print("Invalid value: \(value) at \(context.codingPath)")
}
```

## Examples

```swift
// Example 1: Custom encoder settings
let encoder = JSONEncoder()
encoder.dateEncodingStrategy = .iso8601
encoder.keyEncodingStrategy = .convertToSnakeCase
encoder.outputFormatting = .prettyPrinted

// Example 2: Encode with fallback
func safeEncode<T: Encodable>(_ value: T) -> Data? {
    let encoder = JSONEncoder()
    encoder.dateEncodingStrategy = .iso8601
    return try? encoder.encode(value)
}

// Example 3: Check encoding
struct User: Codable {
    let name: String
    let email: String
}
let user = User(name: "Alice", email: "alice@example.com")
let data = try JSONEncoder().encode(user)
```

## Related Errors

- [Decoding error](decoding-error-swift) — JSON decoding failed
- [Nil unwrap error](nil-unwrap-error) — force unwrapping nil
- [Type cast error](type-cast-error) — type casting failed
