---
title: "[Solution] Swift DateFormat Error — String Mismatch & Locale"
description: "Fix Swift DateFormat string errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 122
---

`DateFormat` errors occur when format strings don't match expected dates, locale/timezone settings cause unexpected parsing, or formatters produce incorrect output.

## Common Causes

```swift
// Incorrect format string
let formatter = DateFormatter()
formatter.dateFormat = "MM/dd/yyyy" // But date is "2024-01-15"

// Missing locale for non-English
formatter.locale = Locale(identifier: "en_US_POSIX")
// Wrong locale causes parsing failure
```

## How to Fix

**1. Match format to date string**

```swift
let formatter = DateFormatter()
formatter.dateFormat = "yyyy-MM-dd'T'HH:mm:ssZ"
let date = formatter.date(from: "2024-01-15T10:30:00+0000")
```

**2. Use ISO8601DateFormatter**

```swift
let formatter = ISO8601DateFormatter()
formatter.formatOptions = [.withInternetDateTime, .withFractionalSeconds]
let date = formatter.date(from: "2024-01-15T10:30:00.000Z")
```

**3. Set proper locale**

```swift
let formatter = DateFormatter()
formatter.locale = Locale(identifier: "en_US_POSIX")
formatter.dateFormat = "yyyy-MM-dd'T'HH:mm:ss.SSSZ"
```

**4. Custom date decoding**

```swift
struct Event: Decodable {
    let date: Date
    
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        let dateString = try container.decode(String.self, forKey: .date)
        
        let formatter = ISO8601DateFormatter()
        formatter.formatOptions = .withInternetDateTime
        
        guard let date = formatter.date(from: dateString) else {
            throw DecodingError.dataCorruptedError(
                forKey: .date,
                in: container,
                debugDescription: "Invalid date format"
            )
        }
        self.date = date
    }
}
```

**5. Formatting for display**

```swift
let outputFormatter = DateFormatter()
outputFormatter.dateStyle = .medium
outputFormatter.timeStyle = .short
outputFormatter.locale = Locale.current

let displayString = outputFormatter.string(from: date)
```

## Examples

Complete date handling:
```swift
enum DateUtils {
    static let iso8601: ISO8601DateFormatter = {
        let f = ISO8601DateFormatter()
        f.formatOptions = .withInternetDateTime
        return f
    }()
    
    static let display: DateFormatter = {
        let f = DateFormatter()
        f.dateStyle = .medium
        f.timeStyle = .short
        f.locale = Locale.current
        return f
    }()
    
    static func parse(_ string: String) -> Date? {
        iso8601.date(from: string) ?? display.date(from: string)
    }
}
```

## Related Errors

- [JSONDecoder Error](/languages/swift/swift-jsondecoder-error)
- [JSONEncoder Error](/languages/swift/swift-jsonencoder-error)
- [Codable Custom Error](/languages/swift/swift-codable-custom-error)
