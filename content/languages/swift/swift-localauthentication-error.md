---
title: "[Solution] Swift LAContext Biometric Evaluation Error"
description: "Fix Swift LocalAuthentication errors. Actionable solutions with Swift code examples."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 140
---

LocalAuthentication errors occur when biometric evaluation fails, policy evaluation isn't configured correctly, or fallback options are missing.

## Common Causes

```swift
// Not checking biometry availability
let context = LAContext()
context.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, localizedReason: "Auth") { success, error in
    // Not handling error types
}

// Wrong policy for device state
context.evaluatePolicy(.deviceOwnerAuthentication, localizedReason: "Auth")
```

## How to Fix

**1. Check biometry availability**

```swift
import LocalAuthentication

func checkBiometry() -> LABiometryType {
    let context = LAContext()
    var error: NSError?
    
    guard context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error) else {
        return .none
    }
    
    return context.biometryType
}
```

**2. Evaluate policy**

```swift
func authenticate(reason: String, completion: @escaping (Bool, Error?) -> Void) {
    let context = LAContext()
    context.localizedCancelTitle = "Use Passcode"
    
    context.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics,
                          localizedReason: reason) { success, error in
        DispatchQueue.main.async {
            completion(success, error)
        }
    }
}
```

**3. Handle specific errors**

```swift
func handleError(_ error: Error?) -> String {
    guard let laError = error as? LAError else {
        return "Unknown error"
    }
    
    switch laError.code {
    case .biometryLockout:
        return "Biometry locked. Use passcode."
    case .biometryNotEnrolled:
        return "No biometrics enrolled."
    case .biometryNotAvailable:
        return "Biometry not available."
    case .userCancel:
        return "Cancelled by user."
    case .userFallback:
        return "User chose fallback."
    default:
        return laError.localizedDescription
    }
}
```

**4. Async/await usage**

```swift
func authenticate() async throws {
    let context = LAContext()
    context.localizedReason = "Authenticate"
    
    do {
        try await context.evaluatePolicy(
            .deviceOwnerAuthenticationWithBiometrics,
            localizedReason: "Authenticate to continue"
        )
    } catch {
        throw error
    }
}
```

**5. Custom biometry reason**

```swift
let context = LAContext()
context.touchIDAuthenticationAllowableReuseDuration = 10 // Reuse within 10 seconds

context.evaluatePolicy(
    .deviceOwnerAuthenticationWithBiometrics,
    localizedReason: "Unlock your secure vault"
) { success, error in
    // Handle result
}
```

## Examples

Complete biometric auth flow:
```swift
class BiometricAuthManager {
    static let shared = BiometricAuthManager()
    
    func authenticate(reason: String) async throws -> Bool {
        let context = LAContext()
        context.localizedReason = reason
        context.localizedFallbackTitle = "Use Passcode"
        
        var error: NSError?
        guard context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error) else {
            throw error ?? LAError(.biometryNotAvailable)
        }
        
        do {
            try await context.evaluatePolicy(
                .deviceOwnerAuthenticationWithBiometrics,
                localizedReason: reason
            )
            return true
        } catch {
            throw error
        }
    }
    
    var biometryType: LABiometryType {
        let context = LAContext()
        var error: NSError?
        guard context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error) else {
            return .none
        }
        return context.biometryType
    }
}
```

## Related Errors

- [CryptoKit Error](/languages/swift/swift-cryptokit-error)
- [Secure Enclave Error](/languages/swift/swift-secure-enclave-error)
- [Keychain Error](/languages/swift/keychain-error)
