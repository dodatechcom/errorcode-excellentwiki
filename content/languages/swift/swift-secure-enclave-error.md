---
title: "[Solution] Swift Secure Enclave Error — Key Tag & Biometric"
description: "Fix Swift Secure Enclave errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 139
---

Secure Enclave errors occur when key tag mismatches, biometric protection isn't available, or hardware requirements aren't met.

## Common Causes

```swift
// Key tag mismatch
let tag = "com.app.securekey"
// Stored with different tag

// Biometric not available
let accessControl = SecAccessControlCreateWithFlags(
    kCFAllocatorDefault,
    kSecAttrAccessibleWhenUnlockedThisDeviceOnly,
    [.biometryCurrentSet],
    nil
)!
```

## How to Fix

**1. Generate Secure Enclave key**

```swift
import Security

func generateSecureKey(tag: String) throws -> SecKey {
    let accessControl = SecAccessControlCreateWithFlags(
        kCFAllocatorDefault,
        kSecAttrAccessibleWhenUnlockedThisDeviceOnly,
        [.privateKeyUsage, .biometryCurrentSet],
        nil
    )!
    
    let attributes: [String: Any] = [
        kSecAttrKeyType as String: kSecAttrKeyTypeECSECPrimeRandom,
        kSecAttrKeySizeInBits as String: 256,
        kSecAttrTokenID as String: kSecAttrTokenIDSecureEnclave,
        kSecPrivateKeyAttrs as String: [
            kSecAttrIsPermanent as String: true,
            kSecAttrApplicationTag as String: tag.data(using: .utf8)!,
            kSecAttrAccessControl as String: accessControl
        ]
    ]
    
    var error: Unmanaged<CFError>?
    guard let privateKey = SecKeyCreateRandomKey(attributes as CFDictionary, &error) else {
        throw error!.takeRetainedValue() as Error
    }
    
    return privateKey
}
```

**2. Retrieve key**

```swift
func retrieveKey(tag: String) -> SecKey? {
    let query: [String: Any] = [
        kSecClass as String: kSecClassKey,
        kSecAttrApplicationTag as String: tag.data(using: .utf8)!,
        kSecAttrKeyType as String: kSecAttrKeyTypeECSECPrimeRandom,
        kSecReturnRef as String: true
    ]
    
    var item: CFTypeRef?
    let status = SecItemCopyMatching(query as CFDictionary, &item)
    
    guard status == errSecSuccess else { return nil }
    return item as! SecKey
}
```

**3. Delete key**

```swift
func deleteKey(tag: String) {
    let query: [String: Any] = [
        kSecClass as String: kSecClassKey,
        kSecAttrApplicationTag as String: tag.data(using: .utf8)!
    ]
    SecItemDelete(query as CFDictionary)
}
```

**4. Check Secure Enclave availability**

```swift
func isSecureEnclaveAvailable() -> Bool {
    var error: Unmanaged<CFError>?
    guard let accessControl = SecAccessControlCreateWithFlags(
        kCFAllocatorDefault,
        kSecAttrAccessibleWhenUnlockedThisDeviceOnly,
        [.privateKeyUsage],
        &error
    ) else {
        return false
    }
    
    let attributes: [String: Any] = [
        kSecAttrKeyType as String: kSecAttrKeyTypeECSECPrimeRandom,
        kSecAttrKeySizeInBits as String: 256,
        kSecAttrTokenID as String: kSecAttrTokenIDSecureEnclave,
        kSecPrivateKeyAttrs as String: [
            kSecAttrIsPermanent as String: false,
            kSecAttrAccessControl as String: accessControl
        ]
    ]
    
    return SecKeyCreateRandomKey(attributes as CFDictionary, nil) != nil
}
```

**5. Sign with Secure Enclave key**

```swift
func sign(_ data: Data, with key: SecKey) throws -> Data {
    var error: Unmanaged<CFError>?
    guard let signature = SecKeyCreateSignature(
        key,
        .ecdsaSignatureMessageX962SHA256,
        data as CFData,
        &error
    ) else {
        throw error!.takeRetainedValue() as Error
    }
    return signature as Data
}
```

## Examples

Complete Secure Enclave manager:
```swift
class SecureEnclaveManager {
    private let keyTag = "com.app.securekey"
    
    func getOrCreateKey() throws -> SecKey {
        if let existing = retrieveKey(tag: keyTag) {
            return existing
        }
        return try generateSecureKey(tag: keyTag)
    }
    
    func encrypt(_ data: Data) throws -> Data {
        let key = try getOrCreateKey()
        var error: Unmanaged<CFError>?
        guard let encrypted = SecKeyCreateEncryptedData(
            key,
            .ecdhKeyExchangeStandard,
            data as CFData,
            &error
        ) else {
            throw error!.takeRetainedValue() as Error
        }
        return encrypted as Data
    }
}
```

## Related Errors

- [CryptoKit Error](/languages/swift/swift-cryptokit-error)
- [LocalAuthentication Error](/languages/swift/swift-localauthentication-error)
- [Keychain Error](/languages/swift/keychain-error)
