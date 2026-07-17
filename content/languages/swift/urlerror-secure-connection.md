---
title: "[Solution] Swift URLError Secure Connection Failed Fix"
description: "Fix Swift URLError secure connection failed. Learn why SSL/TLS connections fail and how to handle certificate issues."
languages: ["swift"]
severities: ["error"]
error-types: ["network-error"]
weight: 5
---

## What This Error Means

A `URLError.secureConnectionFailed` error occurs when the URL loading system cannot establish a secure (HTTPS) connection. This is typically caused by SSL/TLS certificate issues.

## Common Causes

- Self-signed certificate
- Expired SSL certificate
- Certificate hostname mismatch
- SSL/TLS protocol version mismatch
- App Transport Security (ATS) restrictions

## How to Fix

```swift
// WRONG: Disabling ATS (insecure)
// Info.plist: NSAppTransportSecurity > NSAllowsArbitraryLoads = YES

// CORRECT: Use valid SSL certificates
// Ensure server has valid SSL certificate from trusted CA
```

```swift
// WRONG: Ignoring certificate errors
let session = URLSession(configuration: .default, delegate: nil, delegateQueue: nil)

// CORRECT: Handle certificate validation properly
class CertificateHandler: NSObject, URLSessionDelegate {
    func urlSession(_ session: URLSession,
                    didReceive challenge: URLAuthenticationChallenge,
                    completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
        if challenge.protectionSpace.authenticationMethod == NSURLAuthenticationMethodServerTrust {
            if let serverTrust = challenge.protectionSpace.serverTrust {
                var error: CFError?
                if SecTrustEvaluateWithError(serverTrust, &error) {
                    completionHandler(.useCredential, URLCredential(trust: serverTrust))
                    return
                }
            }
        }
        completionHandler(.cancelAuthenticationChallenge, nil)
    }
}
```

## Examples

```swift
// Example 1: ATS exception for specific domain
// Info.plist
// NSAppTransportSecurity > NSExceptionDomains > api.example.com
// NSExceptionRequiresForwardSecrecy = NO

// Example 2: Debug certificate issues
func checkCertificate() {
    let url = URL(string: "https://api.example.com")!
    let task = URLSession.shared.dataTask(with: url) { data, response, error in
        if let error = error as? URLError {
            print("Certificate error: \(error.code)")
        }
    }
    task.resume()
}

// Example 3: Custom trust evaluation
func urlSession(_ session: URLSession,
                didReceive challenge: URLAuthenticationChallenge,
                completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
    guard let serverTrust = challenge.protectionSpace.serverTrust else {
        completionHandler(.cancelAuthenticationChallenge, nil)
        return
    }
    // Custom validation logic
    completionHandler(.useCredential, URLCredential(trust: serverTrust))
}
```

## Related Errors

- [URLError not connected](urlerror-not-connected) — no internet
- [URLError timed out](urlerror-timed-out) — request timeout
- [URLError cannot find host](urlerror-cannot-find-host) — DNS failure
