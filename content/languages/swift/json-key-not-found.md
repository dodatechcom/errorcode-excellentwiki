---
title: "[Solution] Swift Error — JSON Key Not Found"
description: "Fix Swift JSON key not found errors during decoding. Learn why missing keys cause DecodingError and how to handle optional JSON fields."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# JSON Key Not Found

This error occurs when `JSONDecoder` encounters a missing key in the JSON that corresponds to a non-optional property in your `Decodable` struct.

## Description

When a `Decodable` struct has non-optional properties, `JSONDecoder` requires those keys to be present in the JSON. If a key is missing (the entire key-value pair, not just the value), decoding fails with `DecodingError.keyNotFound`. This is different from having a key with a `null` value.

Common patterns:

- **API adds/removes fields** — backend evolves but Swift models don't update.
- **Different API versions** — v1 returns fewer fields than v2.
- **Conditional fields** — some responses include a field, others don't.
- **Nested object missing key** — parent object exists but child key is absent.

## Common Causes

```swift
// Cause 1: Non-optional property with missing key
struct User: Codable {
    let name: String
    let age: Int
    let phone: String // Not in JSON
}
let json = #"{"name": "Alice", "age": 30}"#.data(using: .utf8)!
let user = try JSONDecoder().decode(User.self, from: json)
// DecodingError.keyNotFound(CodingKeys("phone"), ...)

// Cause 2: Key casing mismatch
struct Response: Codable {
    let userName: String
}
let json = #"{"user_name": "Alice"}"#.data(using: .utf8)!
// Key "userName" not found (JSON has "user_name")

// Cause 3: Nested missing key
struct Address: Codable {
    let city: String
    let zip: String
}
struct Profile: Codable {
    let name: String
    let address: Address
}
let json = #"{"name": "Alice", "address": {"city": "NY"}}"#
// DecodingError.keyNotFound("zip" inside address)

// Cause 4: Array element missing key
struct Item: Codable {
    let id: Int
    let value: String
}
let json = #"[{"id": 1}]"#.data(using: .utf8)!
// Fails on second element's missing "value"
```

## How to Fix

### Fix 1: Use CodingKeys to map different key names

```swift
struct User: Codable {
    let name: String

    enum CodingKeys: String, CodingKey {
        case name = "user_name"
    }
}
```

### Fix 2: Make missing fields optional

```swift
struct User: Codable {
    let name: String
    let phone: String? // Won't fail if missing
}
```

### Fix 3: Use `decodeIfPresent` with custom init

```swift
struct User: Codable {
    let name: String
    let phone: String

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        name = try container.decode(String.self, forKey: .name)
        phone = try container.decodeIfPresent(String.self, forKey: .phone) ?? ""
    }
}
```

### Fix 4: Use JSONDecoder with key decoding strategy

```swift
let decoder = JSONDecoder()
decoder.keyDecodingStrategy = .convertFromSnakeCase
// "user_name" in JSON maps to "userName" in Swift
let user = try decoder.decode(User.self, from: data)
```

## Examples

```swift
// Example 1: API evolution
struct Product: Codable {
    let id: Int
    let name: String
    let rating: Double // Added in API v2
}
// V1 response: {"id": 1, "name": "Widget"}
// Decoding fails: "rating" key not found

// Example 2: Typo in CodingKeys
struct Config: Codable {
    let backgroundColor: String
    enum CodingKeys: String, CodingKey {
        case backgroundColor = "background_color" // correct
        // Missing: case fontSize = "font_size"
    }
    let fontSize: Int // Will fail if JSON uses "font_size"
}
```

## Related Errors

- [DecodingError]({{< relref "/languages/swift/json-decoding" >}}) — general JSON decoding error.
- [Type Mismatch]({{< relref "/languages/swift/json-type-mismatch" >}}) — JSON type doesn't match Swift type.
- [Key Not Found in Dictionary]({{< relref "/languages/swift/dictionary-key" >}}) — Swift dictionary key missing.
