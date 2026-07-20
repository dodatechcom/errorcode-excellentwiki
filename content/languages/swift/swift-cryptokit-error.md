---
title: "[Solution] Swift CryptoKit Error — Key Generation & Encryption"
description: "Fix Swift CryptoKit errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 138
---

CryptoKit errors occur during key generation, encryption/decryption operations, signing, or digest calculations.

## Common Causes

```swift
// Invalid key size
let key = SymmetricKey(size: .bits128) // Wrong size for AES-GCM

// Wrong data length for hash
let hash = SHA256.hash(data: Data()) // Empty data
```

## How to Fix

**1. Symmetric encryption**

```swift
import CryptoKit

func encrypt(_ data: Data, using key: SymmetricKey) throws -> Data {
    let sealedBox = try AES.GCM.seal(data, using: key)
    return sealedBox.combined!
}

func decrypt(_ data: Data, using key: SymmetricKey) throws -> Data {
    let sealedBox = try AES.GCM.SealedBox(combined: data)
    return try AES.GCM.open(sealedBox, using: key)
}
```

**2. Key generation**

```swift
let key = SymmetricKey(size: .bits256)
let keyData = key.withUnsafeBytes { Data($0) }
```

**3. Hashing**

```swift
let data = Data("Hello".utf8)
let hash = SHA256.hash(data: data)
let hashString = hash.map { String(format: "%02x", $0) }.joined()
```

**4. HMAC signing**

```swift
let key = SymmetricKey(size: .bits256)
let signature = HMAC<SHA256>.authenticationCode(for: Data("Message".utf8), using: key)
let isValid = HMAC<SHA256>.isValidAuthenticationCode(signature, for: Data("Message".utf8), using: key)
```

**5. P256 signing**

```swift
let privateKey = P256.Signing.PrivateKey()
let publicKey = privateKey.publicKey

let data = Data("Sign this".utf8)
let signature = try privateKey.signature(for: data)
let isValid = publicKey.isValidSignature(signature, for: data)
```

## Examples

Complete CryptoKit usage:
```swift
class CryptoManager {
    private let key: SymmetricKey
    
    init() {
        self.key = SymmetricKey(size: .bits256)
    }
    
    func encrypt(_ plaintext: String) throws -> String {
        let data = Data(plaintext.utf8)
        let sealedBox = try AES.GCM.seal(data, using: key)
        return sealedBox.combined!.base64EncodedString()
    }
    
    func decrypt(_ ciphertext: String) throws -> String {
        guard let data = Data(base64Encoded: ciphertext) else {
            throw CryptoError.invalidData
        }
        let sealedBox = try AES.GCM.SealedBox(combined: data)
        let decrypted = try AES.GCM.open(sealedBox, using: key)
        return String(decoding: decrypted, as: UTF8.self)
    }
    
    func hash(_ data: Data) -> String {
        SHA256.hash(data: data).map { String(format: "%02x", $0) }.joined()
    }
}

enum CryptoError: Error {
    case invalidData
    case encryptionFailed
}
```

## Related Errors

- [Secure Enclave Error](/languages/swift/swift-secure-enclave-error)
- [LocalAuthentication Error](/languages/swift/swift-localauthentication-error)
- [Data Error](/languages/swift/swift-data-error)
