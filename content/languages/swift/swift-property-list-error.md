---
title: "[Solution] Swift PropertyListSerialization Error — Plist Read/Write"
description: "Fix Swift PropertyListSerialization errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 118
---

`PropertyListSerialization` errors occur when reading or writing property list data with invalid formats, unsupported types, or encoding issues.

## Common Causes

```swift
// Invalid plist data
let data = Data("not a plist".utf8)
let plist = try PropertyListSerialization.propertyList(from: data, format: nil)

// Unsupported type in plist
let invalid: [String: Any] = ["date": Date()] // Date not plist-compatible
```

## How to Fix

**1. Validate plist format**

```swift
let data = try Data(contentsOf: url)
var format = PropertyListSerialization.PropertyListFormat.xml
let plist = try PropertyListSerialization.propertyList(
    from: data,
    options: [],
    format: &format
)
```

**2. Write plist data**

```swift
let dictionary: [String: Any] = [
    "name": "Example",
    "version": 1,
    "items": ["a", "b", "c"]
]

let data = try PropertyListSerialization.data(
    fromPropertyList: dictionary,
    format: .xml,
    options: 0
)
try data.write(to: url)
```

**3. Handle plist errors**

```swift
do {
    let plist = try PropertyListSerialization.propertyList(
        from: data, format: nil
    ) as? [String: Any]
} catch let error as NSError {
    print("Plist error: \(error.domain) - \(error.userInfo)")
}
```

**4. Codable plist encoding**

```swift
let encoder = PropertyListEncoder()
encoder.outputFormat = .xml
let data = try encoder.encode(model)

let decoder = PropertyListDecoder()
let model = try decoder.decode(Model.self, from: data)
```

**5. Binary vs XML format**

```swift
let encoder = PropertyListEncoder()
encoder.outputFormat = .binary // More compact
let binaryData = try encoder.encode(model)

encoder.outputFormat = .xml // Human-readable
let xmlData = try encoder.encode(model)
```

## Examples

Complete plist handling:
```swift
func readPlist(from url: URL) throws -> [String: Any] {
    let data = try Data(contentsOf: url)
    var format = PropertyListSerialization.PropertyListFormat.xml
    return try PropertyListSerialization.propertyList(
        from: data,
        options: [],
        format: &format
    ) as! [String: Any]
}

func writePlist(_ dict: [String: Any], to url: URL) throws {
    let data = try PropertyListSerialization.data(
        fromPropertyList: dict,
        format: .xml,
        options: 0
    )
    try data.write(to: url)
}
```

## Related Errors

- [JSONDecoder Error](/languages/swift/swift-jsondecoder-error)
- [UserDefaults Error](/languages/swift/swift-userdefaults-error)
- [Codable Custom Error](/languages/swift/swift-codable-custom-error)
