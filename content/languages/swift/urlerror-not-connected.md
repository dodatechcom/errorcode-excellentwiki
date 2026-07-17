---
title: "[Solution] Swift URLError Not Connected Fix"
description: "Fix Swift URLError not connected to internet. Learn why network requests fail when offline and how to check connectivity."
languages: ["swift"]
severities: ["error"]
error-types: ["network-error"]
tags: ["urlerror", "not-connected", "internet", "swift"]
weight: 5
---

## What This Error Means

A `URLError.notConnectedToInternet` error occurs when your app tries to make a network request but the device has no internet connection. This is the most common URLError in mobile apps.

## Common Causes

- Device is in airplane mode
- Wi-Fi is turned off
- Cellular data is disabled
- Network connection is unstable

## How to Fix

```swift
// WRONG: Not checking connectivity
let (data, _) = try await URLSession.shared.data(from: url)  // Throws when offline

// CORRECT: Check connectivity first
import Network

let monitor = NWPathMonitor()
monitor.pathUpdateHandler = { path in
    if path.status == .satisfied {
        // Connected - make request
    } else {
        // Not connected - show offline message
    }
}
monitor.start(queue: DispatchQueue.global())
```

```swift
// WRONG: Crashing on offline
func loadData() async {
    let (data, _) = try await URLSession.shared.data(from: url)  // May throw
}

// CORRECT: Handle offline gracefully
func loadData() async {
    do {
        let (data, _) = try await URLSession.shared.data(from: url)
        // Process data
    } catch let error as URLError where error.code == .notConnectedToInternet {
        // Show offline UI
        showOfflineMessage()
    }
}
```

## Examples

```swift
// Example 1: Network monitor
import Network

class NetworkMonitor {
    static let shared = NetworkMonitor()
    private let monitor = NWPathMonitor()
    private(set) var isConnected = false

    func startMonitoring() {
        monitor.pathUpdateHandler = { [weak self] path in
            self?.isConnected = path.status == .satisfied
        }
        monitor.start(queue: DispatchQueue.global())
    }
}

// Example 2: Check before request
if NetworkMonitor.shared.isConnected {
    fetchData()
} else {
    showCachedData()
}

// Example 3: Reachability check
func checkReachability(host: String = "https://www.apple.com") -> Bool {
    guard let url = URL(string: host) else { return false }
    let request = URLRequest(url: url, timeoutInterval: 5)
    // Check with URLSession
    return true
}
```

## Related Errors

- [URLError timed out](urlerror-timed-out) — request timeout
- [URLError cannot find host](urlerror-cannot-find-host) — DNS failure
- [URLError secure connection](urlerror-secure-connection) — SSL error
