---
title: "[Solution] Swift Error — URLError:secureConnectionFailed"
description: "Fix Swift URLError:secureConnectionFailed errors. Learn why SSL/TLS connections fail and how to handle certificate and security issues."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# URLError:secureConnectionFailed

This error occurs when the SSL/TLS handshake fails during an HTTPS connection. `URLSession` throws a `URLError` with code `.secureConnectionFailed`.

## Description

SSL/TLS establishes an encrypted connection between the client and server. The handshake involves certificate validation, protocol negotiation, and key exchange. Failures can be caused by expired certificates, unsupported TLS versions, or certificate pinning issues.

Common patterns:

- **Expired certificate** — server certificate has expired.
- **Self-signed certificate** — development servers using self-signed certs.
- **TLS version mismatch** — server only supports outdated TLS versions.
- **Certificate pinning** — pinned certificate doesn't match the server's.

## Common Causes

```swift
// Cause 1: Default URLSession rejects self-signed certs
let url = URL(string: "https://localhost:8443/api")!
let task = URLSession.shared.dataTask(with: url) { _, _, error in
    // error.code == .secureConnectionFailed (self-signed cert)
}

// Cause 2: Expired server certificate
let url = URL(string: "https://expired-cert.example.com")!
let task = URLSession.shared.dataTask(with: url) { _, _, error in
    // error.code == .secureConnectionFailed
}

// Cause 3: TLS version issue
// Server only supports TLS 1.0 but client requires 1.2+

// Cause 4: Certificate pinning mismatch
class Delegate: NSObject, URLSessionDelegate {
    func urlSession(_ session: URLSession,
                    didReceive challenge: URLAuthenticationChallenge,
                    completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
        // Custom pinning logic that rejects valid cert
    }
}
```

## How to Fix

### Fix 1: Handle SSL errors gracefully

```swift
func makeRequest(to url: URL) {
    let task = URLSession.shared.dataTask(with: url) { data, _, error in
        if let error = error as? URLError, error.code == .secureConnectionFailed {
            print("SSL connection failed: \(error.localizedDescription)")
            // Don't automatically bypass SSL — fix the server instead
        }
    }
    task.resume()
}
```

### Fix 2: Configure TLS for development servers

```swift
// For development only — not for production
class DevDelegate: NSObject, URLSessionDelegate {
    func urlSession(_ session: URLSession,
                    didReceive challenge: URLAuthenticationChallenge,
                    completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
        guard challenge.protectionSpace.authenticationMethod == NSURLAuthenticationMethodServerTrust,
              let serverTrust = challenge.protectionSpace.serverTrust else {
            completionHandler(.performDefaultHandling, nil)
            return
        }
        // Validate the certificate manually for dev servers
        let credential = URLCredential(trust: serverTrust)
        completionHandler(.useCredential, credential)
    }
}
```

### Fix 3: Update server to support modern TLS

```swift
// Ensure your server configuration supports TLS 1.2+
// On server side, configure nginx/Apache to support TLS 1.2 and 1.3
// Client-side verification:
let config = URLSessionConfiguration.default
config.tlsMinimumSupportedProtocolVersion = .TLSv12
```

### Fix 4: Fix certificate pinning

```swift
class SecureDelegate: NSObject, URLSessionDelegate {
    func urlSession(_ session: URLSession,
                    didReceive challenge: URLAuthenticationChallenge,
                    completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
        guard let serverTrust = challenge.protectionSpace.serverTrust,
              let certificate = SecTrustGetCertificateAtIndex(serverTrust, 0) else {
            completionHandler(.cancelAuthenticationChallenge, nil)
            return
        }
        // Verify against pinned certificate
        let serverCertData = SecCertificateCopyData(certificate) as Data
        let pinnedCertData = pinnedCertificateData
        if serverCertData == pinnedCertData {
            completionHandler(.useCredential, URLCredential(trust: serverTrust))
        } else {
            completionHandler(.cancelAuthenticationChallenge, nil)
        }
    }
}
```

## Examples

```swift
// Example 1: Self-signed cert rejection
let url = URL(string: "https://dev-server.local:8443")!
URLSession.shared.dataTask(with: url) { _, _, error in
    // .secureConnectionFailed on self-signed cert
}.resume()

// Example 2: Wrong certificate pin
let task = URLSession.shared.dataTask(with: url) { _, _, error in
    // Pinning fails after cert renewal
}
```

## Related Errors

- [URLError]({{< relref "/languages/swift/url-session-error" >}}) — general URLSession error.
- [URLError:cannotFindHost]({{< relref "/languages/swift/network-dns" >}}) — DNS failure.
- [Security Error]({{< relref "/languages/swift/security-error" >}}) — OSStatus security error.
