---
title: "[Solution] Swift Error — URLError"
description: "Fix Swift URLError in URLSession. Learn about URLSession error codes, how to handle network failures, and implement robust error handling."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["urlsession", "networking", "urlerror", "http", "request"]
weight: 5
---

# URLError

A `URLError` is thrown by `URLSession` when a network request fails. The error contains a `code` property indicating the specific failure reason.

## Description

`URLError` is the base error type for all URL loading system failures. It wraps various network-level issues including connectivity problems, timeouts, SSL failures, and bad server responses. Proper error handling is essential for network-dependent apps.

Common patterns:

- **No error handling** — force-trying `try dataTask(with:).resume()` results.
- **Ignoring error codes** — treating all URLErrors the same way.
- **Missing reachability check** — making requests without checking connectivity.
- **No retry logic** — giving up after a single transient failure.

## Common Causes

```swift
// Cause 1: No error handling on data task
let task = URLSession.shared.dataTask(with: url) { data, response, error in
    // error is optional — must check it
    let json = try! JSONSerialization.jsonObject(with: data!) // May crash
}
task.resume()

// Cause 2: Force-unwrap data
let task = URLSession.shared.dataTask(with: url) { data, _, error in
    let content = String(data: data!, encoding: .utf8)! // Crashes if data nil
}
task.resume()

// Cause 3: Ignoring error
let (data, _) = try! URLSession.shared.data(from: url) // Crashes on network error

// Cause 4: Not handling non-200 status codes
let task = URLSession.shared.dataTask(with: url) { data, response, _ in
    let httpResponse = response as! HTTPURLResponse
    // Not checking httpResponse.statusCode
}
```

## How to Fix

### Fix 1: Always check for errors in completion handlers

```swift
let task = URLSession.shared.dataTask(with: url) { data, response, error in
    if let error = error {
        print("Request failed: \(error.localizedDescription)")
        return
    }
    guard let data = data else { return }
    // Process data
}
task.resume()
```

### Fix 2: Use try/catch with async/await

```swift
func fetchData(from url: URL) async throws -> Data {
    let (data, response) = try await URLSession.shared.data(from: url)
    guard let httpResponse = response as? HTTPURLResponse,
          200..<300 ~= httpResponse.statusCode else {
        throw URLError(.badServerResponse)
    }
    return data
}
```

### Fix 3: Create reusable error handler

```swift
enum NetworkError: Error {
    case noData
    case invalidResponse
    case serverError(Int)
    case decodingError
}

func handleNetworkError(_ error: Error) {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .notConnectedToInternet:
            print("No internet connection")
        case .timedOut:
            print("Request timed out")
        default:
            print("Network error: \(urlError.localizedDescription)")
        }
    }
}
```

### Fix 4: Implement retry logic

```swift
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

## Examples

```swift
// Example 1: Force-unwrapping network response
let url = URL(string: "https://api.example.com/data")!
let (data, _) = try! URLSession.shared.data(from: url) // Crashes on failure
let json = try! JSONSerialization.jsonObject(with: data) // Crashes if data nil

// Example 2: Ignoring error in async code
let task = URLSession.shared.dataTask(with: url) { data, _, _ in
    // What if error is non-nil? Data will be nil
    process(data!) // Fatal error
}
```

## Related Errors

- [URLError:notConnectedToInternet]({{< relref "/languages/swift/network-connection" >}}) — no internet connection.
- [URLError:timedOut]({{< relref "/languages/swift/network-timeout" >}}) — request timeout.
- [URLError:cannotFindHost]({{< relref "/languages/swift/network-dns" >}}) — DNS resolution failure.
