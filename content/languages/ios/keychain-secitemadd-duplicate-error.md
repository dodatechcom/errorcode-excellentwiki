---
title: "[Solution] Keychain SecItemAdd Duplicate Error"
description: "Fix duplicate item errors when adding items to the iOS Keychain."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Keychain SecItemAdd Duplicate Error

SecItemAdd returns errSecDuplicateItem when an item with the same service and account already exists in the Keychain.

## Common Causes
- Item already stored with same service and account
- Previous app installation left Keychain data
- Incorrect keychain access group configuration
- Query attributes match existing item

## How to Fix
1. Delete existing item before adding the new one
2. Use update instead of add for existing items
3. Set kSecAttrSynchronizable appropriately
4. Handle errSecDuplicateItem in your code

```swift
// Delete then add pattern:
let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrService as String: "com.example.app",
    kSecAttrAccount as String: "userToken"
]
SecItemDelete(query as CFDictionary)

var addQuery = query
addQuery[kSecValueData as String] = tokenData
SecItemAdd(addQuery as CFDictionary, nil)
```

## Examples
```swift
// Complete Keychain helper:
func saveToKeychain(key: String, value: Data) {
    let query: [String: Any] = [
        kSecClass as String: kSecClassGenericPassword,
        kSecAttrService as String: Bundle.main.bundleIdentifier!,
        kSecAttrAccount as String: key
    ]
    SecItemDelete(query as CFDictionary)

    var addQuery = query
    addQuery[kSecValueData as String] = value
    let status = SecItemAdd(addQuery as CFDictionary, nil)
    assert(status == errSecSuccess, "Keychain save failed: \(status)")
}
```
