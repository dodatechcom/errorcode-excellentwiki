---
title: "[Solution] Swift URLError Bad Server Response Fix"
description: "Fix Swift URLError bad server response. Learn why servers return unexpected responses and how to handle HTTP status codes."
languages: ["swift"]
severities: ["error"]
error-types: ["network-error"]
weight: 5
---

## What This Error Means

A `URLError.badServerResponse` error occurs when the server returns a response outside the 200-299 status code range. This indicates the server processed the request but returned an error or unexpected response.

## Common Causes

- Server returns 4xx or 5xx status codes
- Response format not as expected
- API endpoint changed
- Authentication required but missing

## How to Fix

```swift
// WRONG: Not checking status code
let (data, _) = try await URLSession.shared.data(from: url)
// May have 404 or 500 status

// CORRECT: Check status code
let (data, response) = try await URLSession.shared.data(from: url)
guard let httpResponse = response as? HTTPURLResponse else {
    throw URLError(.badServerResponse)
}
switch httpResponse.statusCode {
case 200...299:
    // Success
case 401:
    throw NetworkError.unauthorized
case 404:
    throw NetworkError.notFound
case 500...599:
    throw NetworkError.serverError(httpResponse.statusCode)
default:
    throw URLError(.badServerResponse)
}
```

```swift
// WRONG: Assuming response is JSON
let (data, _) = try await URLSession.shared.data(from: url)
let json = try JSONSerialization.jsonObject(with: data)  // May fail

// CORRECT: Validate response format
let (data, response) = try await URLSession.shared.data(from: url)
guard let httpResponse = response as? HTTPURLResponse,
      (200...299).contains(httpResponse.statusCode) else {
    throw URLError(.badServerResponse)
}
let json = try JSONSerialization.jsonObject(with: data)
```

## Examples

```swift
// Example 1: Handle different status codes
enum APIError: Error {
    case badResponse(Int)
    case unauthorized
    case notFound
    case serverError(Int)
}

// Example 2: Retry on server error
func fetchWithRetry() async throws -> Data {
    let (data, response) = try await URLSession.shared.data(from: url)
    guard let httpResponse = response as? HTTPURLResponse else {
        throw URLError(.badServerResponse)
    }
    if httpResponse.statusCode == 503 {
        // Service unavailable - retry
        try await Task.sleep(nanoseconds: 1_000_000_000)
        return try await fetchWithRetry()
    }
    return data
}

// Example 3: Decode error response
struct ErrorResponse: Codable {
    let message: String
    let code: Int
}
```

## Related Errors

- [URLError not connected](urlerror-not-connected) — no internet
- [URLError timed out](urlerror-timed-out) — request timeout
- [Decoding error](decoding-error-swift) — JSON decoding failed
