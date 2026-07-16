---
title: "[Solution] Swift Error — JSON Value Not Found"
description: "Fix Swift JSON value not found errors during decoding. Learn why null values and missing optional fields cause DecodingError.valueNotFound."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["json", "null", "nil", "decoding", "codable"]
weight: 5
---

# JSON Value Not Found

This error occurs when `JSONDecoder` encounters a `null` JSON value for a non-optional Swift property. The key exists but its value is `null`, which cannot be assigned to a non-optional type.

## Description

Unlike "key not found" (the key is absent entirely), "value not found" means the key exists but has a `null` value. In JSON, `{"name": null}` is different from `{}`. Swift's `DecodingError.valueNotFound` is thrown when a non-optional property receives `null`.

Common patterns:

- **Nullable API fields** — API returns `null` for optional fields in Swift.
- **Incomplete data** — partial responses with null placeholders.
- **Conditional nullability** — same field is sometimes present, sometimes null.
- **Nested null objects** — parent key present but value is `null`.

## Common Causes

```swift
// Cause 1: Null value for non-optional
struct User: Codable {
    let name: String
    let email: String
}
let json = #"{"name": "Alice", "email": null}"#.data(using: .utf8)!
let user = try JSONDecoder().decode(User.self, from: json)
// DecodingError.valueNotFound(String.self, ...)

// Cause 2: Null in nested object
struct Address: Codable {
    let city: String
}
struct Profile: Codable {
    let address: Address?
}
let json = #"{"address": null}"#.data(using: .utf8)!
// This actually works — Address? is optional
// But if Address itself had non-optional fields...

// Cause 3: Null in array elements
struct Response: Codable {
    let items: [String]
}
let json = #"{"items": [null, "hello"]}"#.data(using: .utf8)!
// DecodingError.valueNotFound(String.self, ...)

// Cause 4: Server returning null for deleted fields
struct Record: Codable {
    let id: Int
    let deletedAt: Date
}
let json = #"{"id": 1, "deletedAt": null}"#
// DecodingError.valueNotFound(Date.self, ...)
```

## How to Fix

### Fix 1: Make nullable properties optional

```swift
struct User: Codable {
    let name: String
    let email: String? // Can handle null
}
```

### Fix 2: Use custom init with null handling

```swift
struct User: Codable {
    let name: String
    let email: String

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        name = try container.decode(String.self, forKey: .name)
        email = try container.decodeIfPresent(String.self, forKey: .email) ?? ""
    }
}
```

### Fix 3: Use a null-safe wrapper

```swift
struct NullSafe<T: Codable>: Codable {
    let value: T?

    init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        value = try? container.decode(T.self)
    }

    func encode(to encoder: Encoder) throws {
        var container = encoder.singleValueContainer()
        try container.encode(value)
    }
}

struct User: Codable {
    let name: String
    let email: NullSafe<String>
}
```

### Fix 4: Handle null in arrays

```swift
struct Response: Codable {
    let items: [String]

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        let rawItems = try container.decode([String?].self, forKey: .items)
        items = rawItems.compactMap { $0 }
    }
}
```

## Examples

```swift
// Example 1: API returns null for optional timestamp
struct Event: Codable {
    let name: String
    let startTime: Date
}
let json = #"{"name": "Meeting", "startTime": null}"#
// DecodingError.valueNotFound — Date can't be null

// Example 2: Null in deeply nested JSON
struct Config: Codable {
    let database: Database
}
struct Database: Codable {
    let host: String
}
let json = #"{"database": {"host": null}}"#
// DecodingError.valueNotFound inside database.host
```

## Related Errors

- [Key Not Found]({{< relref "/languages/swift/json-key-not-found" >}}) — key entirely absent from JSON.
- [DecodingError]({{< relref "/languages/swift/json-decoding" >}}) — general JSON decoding error.
- [Unexpectedly Found Nil]({{< relref "/languages/swift/unexpected-nil" >}}) — nil in unexpected context.
