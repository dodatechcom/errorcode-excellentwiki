---
title: "[Solution] Swift URLError Network Error Fix"
description: "Fix Swift URLError network errors. Learn why network requests fail and how to handle URL loading system errors."
languages: ["swift"]
severities: ["error"]
error-types: ["network-error"]
tags: ["urlerror", "network", "urlsession", "swift"]
weight: 5
---

## What This Error Means

A `URLError` is thrown by the URL loading system when a network request fails. This covers a wide range of network issues from connectivity problems to server errors.

## Common Causes

- No internet connection
- Server unreachable
- Invalid URL
- Request timeout
- SSL/TLS certificate issues

## How to Fix

```swift
// WRONG: Not handling network errors
let url = URL(string: "https://api.example.com/data")!
let (data, _) = try await URLSession.shared.data(from: url)  // May throw

// CORRECT: Handle URLError
do {
    let (data, _) = try await URLSession.shared.data(from: url)
} catch let error as URLError {
    switch error.code {
    case .notConnectedToInternet:
        print("No internet connection")
    case .timedOut:
        print("Request timed out")
    default:
        print("Network error: \(error.localizedDescription)")
    }
}
```

```swift
// WRONG: Not checking HTTP status code
let (data, response) = try await URLSession.shared.data(from: url)
// May have 404 or 500 status

// CORRECT: Check status code
let (data, response) = try await URLSession.shared.data(from: url)
if let httpResponse = response as? HTTPURLResponse {
    guard (200...299).contains(httpResponse.statusCode) else {
        throw URLError(.badServerResponse)
    }
}
```

## Examples

```swift
// Example 1: Network request with error handling
func fetchData() async throws -> Data {
    let url = URL(string: "https://api.example.com/data")!
    let (data, response) = try await URLSession.shared.data(from: url)
    guard let httpResponse = response as? HTTPURLResponse,
          httpResponse.statusCode == 200 else {
        throw URLError(.badServerResponse)
    }
    return data
}

// Example 2: Check connectivity
let isConnected = try await checkNetworkConnectivity()

// Example 3: Retry on failure
func fetchWithRetry(maxRetries: Int = 3) async throws -> Data {
    for attempt in 0..<maxRetries {
        do {
            return try await fetchData()
        } catch {
            if attempt == maxRetries - 1 { throw error }
            try await Task.sleep(nanoseconds: 1_000_000_000)
        }
    }
    throw URLError(.unknown)
}
```

## Related Errors

- [URLError not connected](urlerror-not-connected) — no internet
- [URLError timed out](urlerror-timed-out) — request timeout
- [URLError secure connection](urlerror-secure-connection) — SSL error
- [URLError bad server response](urlerror-bad-server-response) — server error
