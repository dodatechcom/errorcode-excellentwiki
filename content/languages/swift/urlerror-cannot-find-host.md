---
title: "[Solution] Swift URLError Cannot Find Host Fix"
description: "Fix Swift URLError cannot find host. Learn why DNS resolution fails and how to handle hostname resolution errors."
languages: ["swift"]
severities: ["error"]
error-types: ["network-error"]
tags: ["urlerror", "dns", "hostname", "network", "swift"]
weight: 5
---

## What This Error Means

A `URLError.cannotFindHost` error occurs when the URL loading system cannot resolve the hostname in a URL. This is typically a DNS resolution failure, meaning the domain name doesn't exist or DNS servers are unreachable.

## Common Causes

- Domain name doesn't exist
- DNS server unreachable
- Typo in hostname
- DNS cache issues

## How to Fix

```swift
// WRONG: Not handling DNS failure
let (data, _) = try await URLSession.shared.data(from: url)  // Throws when DNS fails

// CORRECT: Handle DNS failure gracefully
do {
    let (data, _) = try await URLSession.shared.data(from: url)
} catch let error as URLError where error.code == .cannotFindHost {
    print("DNS resolution failed: \(error.localizedDescription)")
    // Show user-friendly error message
}
```

```swift
// WRONG: Hardcoded hostname
let url = URL(string: "https://api.example.com")!  // May be wrong

// CORRECT: Validate hostname
func validateHost(_ host: String) -> Bool {
    return !host.isEmpty && host.contains(".")
}

let host = "api.example.com"
if validateHost(host), let url = URL(string: "https://\(host)") {
    // Use URL
}
```

## Examples

```swift
// Example 1: Check DNS resolution
func checkDNS(host: String) async -> Bool {
    guard let url = URL(string: "https://\(host)") else { return false }
    do {
        let (_, response) = try await URLSession.shared.data(from: url)
        return (response as? HTTPURLResponse)?.statusCode == 200
    } catch {
        return false
    }
}

// Example 2: Custom error handling
enum NetworkError: Error {
    case dnsFailure(String)
    case noConnection
    case serverError(Int)
}

// Example 3: Fallback to alternative host
let primaryHost = "api.example.com"
let fallbackHost = "api-backup.example.com"
```

## Related Errors

- [URLError not connected](urlerror-not-connected) — no internet
- [URLError timed out](urlerror-timed-out) — request timeout
- [URLError secure connection](urlerror-secure-connection) — SSL error
