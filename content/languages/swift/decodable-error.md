---
title: "[Solution] Swift Decoding Error — JSONDecoder Fix"
description: "Fix Swift Decodable and JSONDecoder errors. Learn how to handle JSON parsing failures with proper error handling."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["decodable", "json-decoding", "json", "codable", "swift"]
weight: 5
---

# Decoding Error — JSONDecoder Failure

A decoding error occurs when JSONDecoder fails to parse JSON data into a Swift type.

## Description

JSONDecoder uses the Decodable protocol to convert JSON into Swift objects. Failures happen when the JSON structure doesn't match the expected type, keys are missing, or values have wrong types.

Common causes:

- **Missing keys** — JSON missing required properties
- **Type mismatch** — JSON value type doesn't match Swift property
- **Invalid JSON** — malformed JSON data
- **Wrong date format** — date strings not matching decoder format

## Common Causes

```swift
// Cause 1: Missing key
struct User: Decodable {
    let name: String
    let email: String
}
let json = #"{"name": "Alice"}"#  // Missing "email"
let user = try JSONDecoder().decode(User.self, from: Data(json.utf8))  // Error

// Cause 2: Type mismatch
struct Config: Decodable {
    let count: Int
}
let json = #"{"count": "five"}"#  // String instead of Int
let config = try JSONDecoder().decode(Config.self, from: Data(json.utf8))  // Error

// Cause 3: Invalid JSON
let json = #"{"name": "Alice""#  // Missing closing brace
let user = try JSONDecoder().decode(User.self, from: Data(json.utf8))  // Error

// Cause 4: Wrong date format
struct Event: Decodable {
    let date: Date
}
let json = #"{"date": "2024-01-01"}"#
let decoder = JSONDecoder()  // No date strategy set
let event = try decoder.decode(Event.self, from: Data(json.utf8))  // Error
```

## How to Fix

### Fix 1: Use optional properties

```swift
// Wrong
struct User: Decodable {
    let name: String
    let email: String
}

// Correct
struct User: Decodable {
    let name: String
    let email: String?
}
```

### Fix 2: Provide default values

```swift
// Wrong
struct Config: Decodable {
    let count: Int
}

// Correct
struct Config: Decodable {
    let count: Int
    
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        count = (try? container.decode(Int.self, forKey: .count)) ?? 0
    }
}
```

### Fix 3: Use custom decoding

```swift
// Wrong
struct User: Decodable {
    let name: String
}

// Correct
struct User: Decodable {
    let name: String
    let age: Int
    
    enum CodingKeys: String, CodingKey {
        case name
        case age
    }
    
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        name = try container.decode(String.self, forKey: .name)
        age = (try? container.decode(Int.self, forKey: .age)) ?? 0
    }
}
```

### Fix 4: Handle date format

```swift
// Wrong
let decoder = JSONDecoder()

// Correct
let decoder = JSONDecoder()
decoder.dateDecodingStrategy = .formatted(dateFormatter)
decoder.keyDecodingStrategy = .convertFromSnakeCase
```

## Examples

```swift
// Example 1: Complete decoding with error handling
struct User: Decodable {
    let id: Int
    let name: String
    let email: String?
}

func decodeUser(from data: Data) -> User? {
    let decoder = JSONDecoder()
    decoder.keyDecodingStrategy = .convertFromSnakeCase
    return try? decoder.decode(User.self, from: data)
}

// Example 2: Custom decoding with defaults
struct Settings: Decodable {
    let theme: String
    let fontSize: Int
    let notifications: Bool
    
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        theme = (try? container.decode(String.self, forKey: .theme)) ?? "light"
        fontSize = (try? container.decode(Int.self, forKey: .fontSize)) ?? 12
        notifications = (try? container.decode(Bool.self, forKey: .notifications)) ?? true
    }
}
```

## Related Errors

- [Type Cast Failed]({{< relref "/languages/swift/type-cast-failed" >}}) — force cast failure
- [Nil Unwrap]({{< relref "/languages/swift/nil-unwrap" >}}) — force unwrapping nil
- [URL Session Error]({{< relref "/languages/swift/url-error-swift" >}}) — network request failed
