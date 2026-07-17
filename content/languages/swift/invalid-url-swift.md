---
title: "[Solution] Swift Invalid URL Format Fix"
description: "Fix Swift invalid URL format errors. Learn why URL initialization fails and how to create URLs properly."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

An invalid URL format error occurs when you try to create a URL from a string that doesn't conform to URL standards. `URL(string:)` returns nil for invalid strings, and force-unwrapping nil causes a crash.

## Common Causes

- URL string contains spaces or invalid characters
- Missing protocol (http/https)
- Force-unwrapping nil URL result
- URL string from user input without validation

## How to Fix

```swift
// WRONG: Force-unwrapping invalid URL
let url = URL(string: "not a url")!  // Fatal error

// CORRECT: Use optional binding
if let url = URL(string: "https://example.com") {
    // Use URL
}
```

```swift
// WRONG: URL with spaces
let urlString = "https://example.com/path with spaces"
let url = URL(string: urlString)  // nil

// CORRECT: Encode the URL string
let encoded = urlString.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed)
if let url = URL(string: encoded ?? "") {
    // Use URL
}
```

```swift
// WRONG: User input without validation
let userInput = "htp://invalid-protocol.com"
let url = URL(string: userInput)  // nil

// CORRECT: Validate URL components
func isValidURL(_ string: String) -> Bool {
    guard let url = URL(string: string) else { return false }
    return url.scheme != nil && url.host != nil
}
```

## Examples

```swift
// Example 1: Safe URL creation
let urlString = "https://example.com/path"
if let url = URL(string: urlString) {
    print(url.absoluteString)
}

// Example 2: URL from components
var components = URLComponents()
components.scheme = "https"
components.host = "example.com"
components.path = "/search"
components.queryItems = [URLQueryItem(name: "q", value: "swift")]
let url = components.url

// Example 3: URL with percent encoding
let query = "hello world"
let encoded = query.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed)
```

## Related Errors

- [URL error](url-error-swift) — URLError network error
- [Nil unwrap error](nil-unwrap-error) — force unwrapping nil
- [Decoding error](decoding-error-swift) — JSON decoding failed
