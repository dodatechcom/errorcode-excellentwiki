---
title: "[Solution] Swift Error — OSStatus Error"
description: "Fix Swift OSStatus security errors. Learn about Security framework error codes, certificate issues, and common OSStatus failures."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["security", "osstatus", "certificate", "ssl", "keychain"]
weight: 5
---

# OSStatus Error

An `OSStatus` error is a numeric error code from the Apple Security framework. Common values include `errSecParam` (-50), `errSecDuplicateItem` (-25299), and various SSL/certificate errors.

## Description

The Security framework uses `OSStatus` (a 32-bit integer) to indicate errors. Each value maps to a specific security operation failure. These errors are common when working with Keychain, certificates, SSL pinning, and cryptographic operations.

Common patterns:

- **Duplicate item** — trying to add a Keychain item that already exists.
- **Invalid parameters** — malformed query dictionaries.
- **Certificate errors** — SSL certificate validation failures.
- **Not available** — security operation not supported on current platform.

## Common Causes

```swift
// Cause 1: Duplicate Keychain item
let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrService as String: "com.app.service",
    kSecAttrAccount as String: "user"
]
let status = SecItemAdd(query as CFDictionary, nil)
// errSecDuplicateItem (-25299) if item already exists

// Cause 2: Invalid query parameters
let query: [String: Any] = [
    kSecClass as String: "invalid_class"
]
var item: CFTypeRef?
let status = SecItemCopyMatching(query as CFDictionary, &item)
// errSecParam (-50)

// Cause 3: Certificate trust failure
let policy = SecPolicyCreateSSL(true, "example.com" as CFString)
var trust: SecTrust?
SecTrustCreateWithCertificates(certChain as CFTypeRef, policy, &trust)
var error: CFError?
SecTrustEvaluateWithError(trust!, &error)
// May return various OSStatus errors

// Cause 4: Data conversion issue
let password = "secret"
let data = password.data(using: .utf8)!
// If data is empty or nil, operations fail
```

## How to Fix

### Fix 1: Delete before adding to avoid duplicates

```swift
func saveToKeychain(key: String, value: Data) {
    let query: [String: Any] = [
        kSecClass as String: kSecClassGenericPassword,
        kSecAttrService as String: Bundle.main.bundleIdentifier ?? "",
        kSecAttrAccount as String: key
    ]
    // Delete existing item first
    SecItemDelete(query as CFDictionary)
    // Now add
    var addQuery = query
    addQuery[kSecValueData as String] = value
    let status = SecItemAdd(addQuery as CFDictionary, nil)
    guard status == errSecSuccess else {
        print("Keychain save failed: \(status)")
        return
    }
}
```

### Fix 2: Validate query parameters

```swift
func queryKeychain(account: String) -> Data? {
    guard !account.isEmpty else { return nil } // Prevent errSecParam

    let query: [String: Any] = [
        kSecClass as String: kSecClassGenericPassword,
        kSecAttrService as String: Bundle.main.bundleIdentifier ?? "",
        kSecAttrAccount as String: account,
        kSecReturnData as String: true
    ]
    var item: CFTypeRef?
    let status = SecItemCopyMatching(query as CFDictionary, &item)
    return status == errSecSuccess ? item as? Data : nil
}
```

### Fix 3: Handle specific OSStatus codes

```swift
func handleOSStatus(_ status: OSStatus) {
    switch status {
    case errSecSuccess:
        break
    case errSecDuplicateItem:
        print("Item already exists")
    case errSecItemNotFound:
        print("Item not found")
    case errSecParam:
        print("Invalid parameters")
    case errSecAuthFailed:
        print("Authentication failed")
    case errSecInteractionNotAllowed:
        print("Keychain interaction not allowed")
    default:
        print("Security error: \(status)")
    }
}
```

### Fix 4: Use proper certificate validation

```swift
func validateCertificate(_ trust: SecTrust, forHost host: String) -> Bool {
    let policy = SecPolicyCreateSSL(true, host as CFString)
    SecTrustSetPolicies(trust, policy)
    var error: CFError?
    return SecTrustEvaluateWithError(trust, &error)
}
```

## Examples

```swift
// Example 1: errSecDuplicateItem
let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrService as String: "com.app",
    kSecAttrAccount as String: "token",
    kSecValueData as String: "data".data(using: .utf8)!
]
let status = SecItemAdd(query as CFDictionary, nil)
// -25299 if "token" already exists

// Example 2: errSecParam from empty query
let emptyQuery: [String: [:]] = [:]
var item: CFTypeRef?
let status = SecItemCopyMatching(emptyQuery as CFDictionary, &item)
// -50: invalid parameters
```

## Related Errors

- [Keychain Error]({{< relref "/languages/swift/keychain-error" >}}) — keychain-specific errSecItemNotFound.
- [URLError:secureConnectionFailed]({{< relref "/languages/swift/network-ssl" >}}) — SSL connection failures.
- [File Permission Denied]({{< relref "/languages/swift/file-permission" >}}) — access permission errors.
