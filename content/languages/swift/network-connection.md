---
title: "[Solution] Swift Error — URLError:notConnectedToInternet"
description: "Fix Swift URLError:notConnectedToInternet. Learn how to handle no internet connection errors and check network reachability."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# URLError:notConnectedToInternet

This error occurs when a network request is attempted but the device has no internet connection. `URLSession` throws a `URLError` with code `.notConnectedToInternet`.

## Description

When a device is offline or in airplane mode, any network request fails with `.notConnectedToInternet`. The system provides this error before any request is sent, making it fast to detect. Apps should check connectivity before making requests and handle this error gracefully.

Common patterns:

- **No offline handling** — app crashes or shows errors on launch without connectivity.
- **Background fetch** — network calls in `applicationDidEnterBackground` without check.
- **Retry loop** — repeatedly retrying without checking connectivity.
- **Cached data ignored** — failing to show cached data when offline.

## Common Causes

```swift
// Cause 1: No connectivity check before request
let task = URLSession.shared.dataTask(with: url) { data, _, error in
    if let error = error as? URLError {
        if error.code == .notConnectedToInternet {
            // Handle offline — but many apps miss this
        }
    }
}

// Cause 2: Force-unwrapping result on offline
let (data, _) = try! URLSession.shared.data(from: url) // Crashes on offline

// Cause 3: Background sync without connectivity check
func applicationDidEnterBackground() {
    syncToServer() // Will fail if offline
}

// Cause 4: Ignoring network errors in Combine/Publishers
URLSession.shared.dataTaskPublisher(for: url)
    .sink(receiveCompletion: { _ in },
          receiveValue: { _ in }) // Ignores errors
```

## How to Fix

### Fix 1: Check NWPathMonitor before requests

```swift
import Network

let monitor = NWPathMonitor()
monitor.pathUpdateHandler = { path in
    if path.status == .satisfied {
        print("Connected")
    } else {
        print("No internet connection")
    }
}
monitor.start(queue: DispatchQueue(label: "NetworkMonitor"))
```

### Fix 2: Handle error in completion handler

```swift
func fetchData(from url: URL, completion: @escaping (Result<Data, Error>) -> Void) {
    let task = URLSession.shared.dataTask(with: url) { data, _, error in
        if let error = error as? URLError, error.code == .notConnectedToInternet {
            completion(.failure(NetworkError.offline))
            return
        }
        guard let data = data else {
            completion(.failure(NetworkError.noData))
            return
        }
        completion(.success(data))
    }
    task.resume()
}

enum NetworkError: Error {
    case offline
    case noData
}
```

### Fix 3: Use cached data when offline

```swift
func loadData() async -> Data? {
    do {
        let (data, _) = try await URLSession.shared.data(from: url)
        cacheData(data)
        return data
    } catch let error as URLError where error.code == .notConnectedToInternet {
        return loadFromCache() // Show cached data
    } catch {
        return nil
    }
}
```

### Fix 4: Show appropriate user feedback

```swift
func handleError(_ error: Error) {
    if let urlError = error as? URLError,
       urlError.code == .notConnectedToInternet {
        showAlert(title: "No Internet", message: "Please check your connection and try again.")
    }
}
```

## Examples

```swift
// Example 1: Force-try on offline device
let url = URL(string: "https://api.example.com/data")!
let data = try! URLSession.shared.data(from: url).0 // Fatal error on offline

// Example 2: No retry on transient offline
func syncData() {
    let task = URLSession.shared.dataTask(with: uploadURL) { _, _, error in
        if let error = error {
            print("Sync failed: \(error)") // No retry
        }
    }
    task.resume()
}
```

## Related Errors

- [URLError:timedOut]({{< relref "/languages/swift/network-timeout" >}}) — request timeout.
- [URLError]({{< relref "/languages/swift/url-session-error" >}}) — general URLSession error.
- [URLError:cannotFindHost]({{< relref "/languages/swift/network-dns" >}}) — DNS resolution failure.
