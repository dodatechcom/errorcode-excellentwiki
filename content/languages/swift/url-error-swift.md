---
title: "[Solution] Swift URL / URLSession Error Fix"
description: "Fix Swift URLSession and URL errors. Learn how to handle network request failures, invalid URLs, and connection issues."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["url-error", "urlsession", "networking", "http", "swift"]
weight: 5
---

# URL / URLSession Error — Network Request Failed

URL and URLSession errors occur when network requests fail due to invalid URLs, connection issues, or server errors.

## Description

URLSession is Swift's API for making network requests. Errors can occur at various stages: URL creation, connection, data transfer, or response parsing.

Common causes:

- **Invalid URL** — malformed URL string
- **No internet connection** — device offline
- **Server error** — 4xx or 5xx HTTP status
- **Timeout** — request took too long
- **SSL/TLS error** — certificate validation failure

## Common Causes

```swift
// Cause 1: Invalid URL
let url = URL(string: "not a valid url")  // nil

// Cause 2: No internet
let task = URLSession.shared.dataTask(with: url) { data, response, error in
    if let error = error {
        print(error)  // NSURLErrorNotConnectedToInternet
    }
}

// Cause 3: Server error
let task = URLSession.shared.dataTask(with: url) { data, response, error in
    if let httpResponse = response as? HTTPURLResponse {
        if httpResponse.statusCode >= 400 {
            print("Server error: \(httpResponse.statusCode)")
        }
    }
}

// Cause 4: Timeout
let config = URLSessionConfiguration.default
config.timeoutIntervalForRequest = 5
let session = URLSession(configuration: config)
```

## How to Fix

### Fix 1: Validate URL before use

```swift
// Wrong
let url = URL(string: userInput)!
let task = URLSession.shared.dataTask(with: url)

// Correct
guard let url = URL(string: userInput) else {
    print("Invalid URL")
    return
}
let task = URLSession.shared.dataTask(with: url)
```

### Fix 2: Handle network errors

```swift
// Wrong
let task = URLSession.shared.dataTask(with: url) { data, response, error in
    // Ignoring error
}

// Correct
let task = URLSession.shared.dataTask(with: url) { data, response, error in
    if let error = error {
        print("Network error: \(error.localizedDescription)")
        return
    }
    guard let httpResponse = response as? HTTPURLResponse,
          (200...299).contains(httpResponse.statusCode) else {
        print("Server error")
        return
    }
}
```

### Fix 3: Set timeout

```swift
// Wrong
let task = URLSession.shared.dataTask(with: url)

// Correct
let config = URLSessionConfiguration.default
config.timeoutIntervalForRequest = 30
let session = URLSession(configuration: config)
let task = session.dataTask(with: url)
```

### Fix 4: Use async/await (iOS 15+)

```swift
// Wrong
let task = URLSession.shared.dataTask(with: url) { data, response, error in
    // Completion handler
}

// Correct
do {
    let (data, response) = try await URLSession.shared.data(from: url)
    let httpResponse = response as! HTTPURLResponse
    guard (200...299).contains(httpResponse.statusCode) else {
        throw URLError(.badServerResponse)
    }
} catch {
    print("Error: \(error)")
}
```

## Examples

```swift
// Example 1: Complete network request
func fetchUser(id: Int) async throws -> User {
    guard let url = URL(string: "https://api.example.com/users/\(id)") else {
        throw URLError(.badURL)
    }
    
    let (data, response) = try await URLSession.shared.data(from: url)
    
    guard let httpResponse = response as? HTTPURLResponse,
          httpResponse.statusCode == 200 else {
        throw URLError(.badServerResponse)
    }
    
    return try JSONDecoder().decode(User.self, from: data)
}

// Example 2: Retry logic
func fetchWithRetry(url: URL, retries: Int = 3) async throws -> Data {
    for attempt in 0..<retries {
        do {
            let (data, _) = try await URLSession.shared.data(from: url)
            return data
        } catch {
            if attempt == retries - 1 { throw error }
            try await Task.sleep(nanoseconds: UInt64(pow(2.0, Double(attempt))) * 1_000_000_000)
        }
    }
    throw URLError(.unknown)
}
```

## Related Errors

- [Decoding Error]({{< relref "/languages/swift/decodable-error" >}}) — JSONDecoder failure
- [SwiftUI Error]({{< relref "/languages/swift/swiftui-error" >}}) — SwiftUI runtime error
- [Memory Error]({{< relref "/languages/swift/memory-error-swift" >}}) — memory corruption
