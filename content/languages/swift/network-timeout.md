---
title: "[Solution] Swift Error — URLError:timedOut"
description: "Fix Swift URLError:timedOut errors. Learn why network requests time out and how to configure timeouts and handle slow connections."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# URLError:timedOut

This error occurs when a network request exceeds its allowed time limit. `URLSession` throws a `URLError` with code `.timedOut`.

## Description

Network requests have default timeout intervals (typically 60 seconds for resources). If the server doesn't respond within this window, the request fails with `.timedOut`. This is common with slow servers, large uploads/downloads, or congested networks.

Common patterns:

- **Large file downloads** — slow connections hitting timeout on big transfers.
- **Slow API** — backend taking too long to process complex queries.
- **Background uploads** — uploads timing out in background sessions.
- **No timeout configuration** — using default timeouts for time-sensitive operations.

## Common Causes

```swift
// Cause 1: Using default timeout for slow server
let task = URLSession.shared.dataTask(with: slowServerURL) { data, _, error in
    if let error = error as? URLError, error.code == .timedOut {
        // Server took too long
    }
}

// Cause 2: Large upload without extended timeout
let uploadTask = session.uploadTask(with: request, from: largeData) { _, _, error in
    // May timeout on large uploads with default timeout
}

// Cause 3: DNS resolution timeout
let task = URLSession.shared.dataTask(with: url) { _, _, error in
    // DNS can be slow on some networks
}

// Cause 4: Background session timeout
let config = URLSessionConfiguration.backgroundSessionConfiguration(withIdentifier: "upload")
// Background sessions have stricter timeouts
```

## How to Fix

### Fix 1: Configure appropriate timeout interval

```swift
let config = URLSessionConfiguration.default
config.timeoutIntervalForRequest = 30 // 30 seconds for request
config.timeoutIntervalForResource = 300 // 5 minutes for resource
let session = URLSession(configuration: config)
```

### Fix 2: Use per-request timeout via URLRequest

```swift
var request = URLRequest(url: url)
request.timeoutInterval = 10 // 10 seconds for this specific request
let task = session.dataTask(with: request) { data, _, error in
    if let error = error as? URLError, error.code == .timedOut {
        print("Request timed out")
    }
}
task.resume()
```

### Fix 3: Implement retry with exponential backoff

```swift
func fetchWithTimeout(url: URL, timeout: TimeInterval = 15) async throws -> Data {
    var request = URLRequest(url: url)
    request.timeoutInterval = timeout
    let (data, _) = try await URLSession.shared.data(for: request)
    return data
}

func retryFetch(url: URL, retries: Int = 3) async throws -> Data {
    for i in 0..<retries {
        do {
            return try await fetchWithTimeout(url: url)
        } catch let error as URLError where error.code == .timedOut {
            if i == retries - 1 { throw error }
            try await Task.sleep(nanoseconds: UInt64(pow(2.0, Double(i))) * 1_000_000_000)
        }
    }
    throw URLError(.timedOut)
}
```

### Fix 4: Show appropriate user feedback

```swift
func handleTimeout() {
    let alert = UIAlertController(
        title: "Request Timed Out",
        message: "The server took too long to respond. Please try again.",
        preferredStyle: .alert
    )
    alert.addAction(UIAlertAction(title: "Retry", style: .default) { _ in
        self.retryRequest()
    })
    present(alert, animated: true)
}
```

## Examples

```swift
// Example 1: Very short timeout
var request = URLRequest(url: url)
request.timeoutInterval = 0.1 // 100ms — almost certainly times out
let task = URLSession.shared.dataTask(with: request) { _, _, error in
    // error.code == .timedOut
}

// Example 2: Upload timeout
let largeData = Data(repeating: 0, count: 100_000_000) // 100MB
var uploadRequest = URLRequest(url: uploadURL)
uploadRequest.httpMethod = "POST"
// Default timeout may not be enough for 100MB upload
let task = session.uploadTask(with: uploadRequest, from: largeData)
```

## Related Errors

- [URLError:notConnectedToInternet]({{< relref "/languages/swift/network-connection" >}}) — no internet connection.
- [URLError]({{< relref "/languages/swift/url-session-error" >}}) — general URLSession error.
- [URLError:cannotFindHost]({{< relref "/languages/swift/network-dns" >}}) — DNS failure.
