---
title: "[Solution] Swift URLError Timed Out Fix"
description: "Fix Swift URLError timed out errors. Learn why network requests timeout and how to handle timeout errors properly."
languages: ["swift"]
severities: ["error"]
error-types: ["network-error"]
tags: ["urlerror", "timeout", "network", "swift"]
weight: 5
---

## What This Error Means

A `URLError.timedOut` error occurs when a network request exceeds the allowed time limit. This happens when the server is slow, the connection is unstable, or the request is too large.

## Common Causes

- Server is slow or overloaded
- Large data transfer
- Unstable network connection
- Timeout interval too short

## How to Fix

```swift
// WRONG: Default timeout too short
let (data, _) = try await URLSession.shared.data(from: url)  // 60s default

// CORRECT: Increase timeout
var request = URLRequest(url: url)
request.timeoutInterval = 120  // 2 minutes
let (data, _) = try await URLSession.shared.data(for: request)
```

```swift
// WRONG: Not handling timeout
func fetchData() async throws -> Data {
    let (data, _) = try await URLSession.shared.data(from: url)
    return data  // May throw timeout
}

// CORRECT: Handle timeout specifically
func fetchData() async throws -> Data {
    do {
        let (data, _) = try await URLSession.shared.data(from: url)
        return data
    } catch let error as URLError where error.code == .timedOut {
        throw NetworkError.timeout
    }
}
```

## Examples

```swift
// Example 1: Custom timeout session
let config = URLSessionConfiguration.default
config.timeoutIntervalForRequest = 30
config.timeoutIntervalForResource = 600
let session = URLSession(configuration: config)

// Example 2: Retry with backoff
func fetchWithRetry(maxRetries: Int = 3) async throws -> Data {
    for attempt in 0..<maxRetries {
        do {
            return try await fetchData()
        } catch let error as URLError where error.code == .timedOut {
            let delay = UInt64(pow(2.0, Double(attempt))) * 1_000_000_000
            try await Task.sleep(nanoseconds: delay)
        }
    }
    throw URLError(.timedOut)
}

// Example 3: Timeout error enum
enum NetworkError: Error {
    case timeout
    case noConnection
    case serverError(Int)
}
```

## Related Errors

- [URLError not connected](urlerror-not-connected) — no internet
- [URLError cannot find host](urlerror-cannot-find-host) — DNS failure
- [URLError secure connection](urlerror-secure-connection) — SSL error
