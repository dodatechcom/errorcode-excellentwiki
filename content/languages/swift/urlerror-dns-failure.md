---
title: "[Solution] Swift URLError DNS Failure Fix"
description: "Fix Swift URLError DNS failure. Learn why DNS resolution fails and how to handle DNS-related network errors."
languages: ["swift"]
severities: ["error"]
error-types: ["network-error"]
weight: 5
---

## What This Error Means

A `URLError.dnsLookupFailed` error occurs when the DNS system cannot resolve a hostname to an IP address. This is similar to `cannotFindHost` but specifically indicates a DNS resolution failure.

## Common Causes

- DNS server unreachable
- Domain name doesn't exist
- DNS server overloaded
- Network firewall blocking DNS

## How to Fix

```swift
// WRONG: Not handling DNS failure
let (data, _) = try await URLSession.shared.data(from: url)

// CORRECT: Handle DNS failure
do {
    let (data, _) = try await URLSession.shared.data(from: url)
} catch let error as URLError where error.code == .dnsLookupFailed {
    // DNS failed - try cached data or show offline message
    showOfflineMode()
}
```

```swift
// WRONG: No fallback for DNS issues
func fetchData() async throws -> Data {
    let (data, _) = try await URLSession.shared.data(from: url)
    return data
}

// CORRECT: Provide fallback
func fetchData() async throws -> Data {
    do {
        let (data, _) = try await URLSession.shared.data(from: url)
        return data
    } catch let error as URLError where error.code == .dnsLookupFailed {
        // Try cached or alternative source
        return try loadCachedData()
    }
}
```

## Examples

```swift
// Example 1: Network path monitoring
import Network

let monitor = NWPathMonitor()
monitor.pathUpdateHandler = { path in
    if path.status == .satisfied && !path.usesInterfaceType(.wifi) {
        // On cellular - DNS may be slower
    }
}

// Example 2: Custom DNS resolution
func resolveHost(_ host: String) async throws -> String {
    // Use custom DNS resolver if needed
    return host
}

// Example 3: Fallback URLs
let urls = [
    URL(string: "https://primary.example.com/api"),
    URL(string: "https://backup.example.com/api")
]
for url in urls.compactMap({ $0 }) {
    do {
        let (data, _) = try await URLSession.shared.data(from: url)
        return data
    } catch {
        continue
    }
}
```

## Related Errors

- [URLError cannot find host](urlerror-cannot-find-host) — hostname not found
- [URLError not connected](urlerror-not-connected) — no internet
- [URLError timed out](urlerror-timed-out) — request timeout
