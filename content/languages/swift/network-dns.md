---
title: "[Solution] Swift Error — URLError:cannotFindHost"
description: "Fix Swift URLError:cannotFindHost errors. Learn why DNS resolution fails and how to handle hostname lookup errors in URLSession."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["dns", "hostname", "network", "urlsession", "lookup"]
weight: 5
---

# URLError:cannotFindHost

This error occurs when the system cannot resolve a hostname to an IP address via DNS. `URLSession` throws a `URLError` with code `.cannotFindHost`.

## Description

DNS (Domain Name System) translates human-readable hostnames into IP addresses. When DNS resolution fails, the URL loading system cannot establish a connection. This error is different from `.cannotConnectToHost` (which means DNS succeeded but the server refused the connection).

Common patterns:

- **Typos in URLs** — misspelled domain names.
- **DNS server issues** — DNS server down or unreachable.
- **Local development** — pointing to `localhost` when no server is running.
- **Corporate network** — DNS filtering blocking certain domains.

## Common Causes

```swift
// Cause 1: Typo in URL
let url = URL(string: "https://api.exampel.com/data")! // misspelled
let task = URLSession.shared.dataTask(with: url) { _, _, error in
    // error.code == .cannotFindHost
}

// Cause 2: Custom hostname that doesn't exist
let url = URL(string: "https://my-custom-api.local/data")!
let task = URLSession.shared.dataTask(with: url) { _, _, error in
    // DNS can't resolve .local without mDNS
}

// Cause 3: DNS server unreachable
// If device has no DNS configuration, all lookups fail

// Cause 4: Using IP address bypasses DNS
let url = URL(string: "https://192.168.1.100:8080/api")!
// This would NOT produce cannotFindHost — it skips DNS
```

## How to Fix

### Fix 1: Validate URLs before making requests

```swift
func makeRequest(to urlString: String) {
    guard let url = URL(string: urlString),
          let host = url.host,
          !host.isEmpty else {
        print("Invalid URL")
        return
    }
    let task = URLSession.shared.dataTask(with: url) { data, _, error in
        if let error = error as? URLError, error.code == .cannotFindHost {
            print("Cannot find host: \(host)")
        }
    }
    task.resume()
}
```

### Fix 2: Provide fallback URLs

```swift
let primaryURL = URL(string: "https://api-primary.example.com/data")!
let fallbackURL = URL(string: "https://api-fallback.example.com/data")!

func fetchWithFallback() async throws -> Data {
    do {
        let (data, _) = try await URLSession.shared.data(from: primaryURL)
        return data
    } catch let error as URLError where error.code == .cannotFindHost {
        let (data, _) = try await URLSession.shared.data(from: fallbackURL)
        return data
    }
}
```

### Fix 3: Check network status before DNS lookup

```swift
import Network

func checkConnectivity() async -> Bool {
    let monitor = NWPathMonitor()
    return await withCheckedContinuation { continuation in
        monitor.pathUpdateHandler = { path in
            continuation.resume(returning: path.status == .satisfied)
            monitor.cancel()
        }
        monitor.start(queue: .global())
    }
}
```

### Fix 4: Show user-friendly error messages

```swift
func handleError(_ error: Error) {
    if let urlError = error as? URLError {
        switch urlError.code {
        case .cannotFindHost:
            print("Server not found. Please check the URL.")
        case .cannotConnectToHost:
            print("Cannot connect to server.")
        default:
            print("Network error: \(urlError.localizedDescription)")
        }
    }
}
```

## Examples

```swift
// Example 1: Misspelled hostname
let url = URL(string: "https://gogle.com")! // "gogle" not found
let task = URLSession.shared.dataTask(with: url) { _, _, error in
    // error.code == .cannotFindHost
}

// Example 2: Expired domain
let url = URL(string: "https://expired-domain-12345.com/api")!
// DNS lookup fails if domain expired
```

## Related Errors

- [URLError:notConnectedToInternet]({{< relref "/languages/swift/network-connection" >}}) — no internet connection.
- [URLError:secureConnectionFailed]({{< relref "/languages/swift/network-ssl" >}}) — SSL/TLS failure.
- [URLError]({{< relref "/languages/swift/url-session-error" >}}) — general URLSession error.
