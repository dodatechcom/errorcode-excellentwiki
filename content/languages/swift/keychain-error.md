---
title: "[Solution] Swift Error — Keychain Error (errSecItemNotFound)"
description: "Fix Swift Keychain errors. Learn about errSecItemNotFound, keychain query failures, and how to securely store and retrieve credentials."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Keychain Error — errSecItemNotFound

This error occurs when querying the Keychain for an item that doesn't exist. The Security framework returns `errSecItemNotFound` (OSStatus -25300) when no matching item is found.

## Description

The iOS/macOS Keychain provides encrypted storage for sensitive data like passwords, tokens, and certificates. `errSecItemNotFound` indicates the query didn't match any stored item. This is common with incorrect service names, access groups, or account identifiers.

Common patterns:

- **Wrong service name** — querying with a different service than used for storage.
- **Access group mismatch** — items stored with one access group, queried with another.
- **App reinstall** — keychain items persist after uninstall (but may need re-authentication).
- **Simulator issues** — keychain behaves differently on simulator.

## Common Causes

```swift
// Cause 1: Wrong service name in query
let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrService as String: "com.wrong.bundle",
    kSecAttrAccount as String: "userToken"
]
var item: CFTypeRef?
let status = SecItemCopyMatching(query as CFDictionary, &item)
// errSecItemNotFound — wrong service name

// Cause 2: Access group mismatch
let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrAccessGroup as String: "com.wrong.group",
    kSecAttrAccount as String: "userToken"
]

// Cause 3: Keychain cleared
// After app uninstall/reinstall, keychain may be cleared

// Cause 4: Wrong item class
// Stored as kSecClassInternetPassword, queried as kSecClassGenericPassword
```

## How to Fix

### Fix 1: Use consistent service name

```swift
let service = Bundle.main.bundleIdentifier ?? "com.default.app"

func saveToken(_ token: String) {
    let query: [String: Any] = [
        kSecClass as String: kSecClassGenericPassword,
        kSecAttrService as String: service,
        kSecAttrAccount as String: "authToken",
        kSecValueData as String: token.data(using: .utf8)!
    ]
    SecItemAdd(query as CFDictionary, nil)
}

func loadToken() -> String? {
    let query: [String: Any] = [
        kSecClass as String: kSecClassGenericPassword,
        kSecAttrService as String: service,
        kSecAttrAccount as String: "authToken",
        kSecReturnData as String: true
    ]
    var item: CFTypeRef?
    let status = SecItemCopyMatching(query as CFDictionary, &item)
    guard status == errSecSuccess, let data = item as? Data else { return nil }
    return String(data: data, encoding: .utf8)
}
```

### Fix 2: Handle errSecItemNotFound gracefully

```swift
func loadFromKeychain(account: String) -> Data? {
    let query: [String: Any] = [
        kSecClass as String: kSecClassGenericPassword,
        kSecAttrService as String: service,
        kSecAttrAccount as String: account,
        kSecReturnData as String: true
    ]
    var item: CFTypeRef?
    let status = SecItemCopyMatching(query as CFDictionary, &item)
    switch status {
    case errSecSuccess:
        return item as? Data
    case errSecItemNotFound:
        return nil // Expected — item doesn't exist yet
    default:
        print("Keychain error: \(status)")
        return nil
    }
}
```

### Fix 3: Update instead of add when item exists

```swift
func saveOrUpdate(key: String, value: Data) {
    let query: [String: Any] = [
        kSecClass as String: kSecClassGenericPassword,
        kSecAttrService as String: service,
        kSecAttrAccount as String: key
    ]
    let attributes: [String: Any] = [
        kSecValueData as String: value
    ]
    let status = SecItemUpdate(query as CFDictionary, attributes as CFDictionary)
    if status == errSecItemNotFound {
        var addQuery = query
        addQuery[kSecValueData as String] = value
        SecItemAdd(addQuery as CFDictionary, nil)
    }
}
```

### Fix 4: Create a reusable Keychain helper

```swift
struct KeychainHelper {
    static func save(_ data: Data, forKey key: String) {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: Bundle.main.bundleIdentifier ?? "",
            kSecAttrAccount as String: key,
            kSecValueData as String: data
        ]
        SecItemDelete(query as CFDictionary)
        SecItemAdd(query as CFDictionary, nil)
    }

    static func load(forKey key: String) -> Data? {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: Bundle.main.bundleIdentifier ?? "",
            kSecAttrAccount as String: key,
            kSecReturnData as String: true
        ]
        var item: CFTypeRef?
        let status = SecItemCopyMatching(query as CFDictionary, &item)
        return status == errSecSuccess ? item as? Data : nil
    }
}
```

## Examples

```swift
// Example 1: Querying after reinstall
// Keychain items may persist but app data is gone
let savedToken = loadToken() // Returns nil if keychain was cleared

// Example 2: Simulator keychain issues
// Keychain on simulator may not work identically to device
// Always test on physical device for keychain operations
```

## Related Errors

- [Security Error]({{< relref "/languages/swift/security-error" >}}) — general OSStatus security error.
- [File Permission Denied]({{< relref "/languages/swift/file-permission" >}}) — file access permission error.
- [Core Data Error]({{< relref "/languages/swift/coredata-error" >}}) — persistence storage errors.
