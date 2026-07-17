---
title: "[Solution] macOS NSURLError Server Trust Evaluation (-1202)"
description: "Fix macOS NSURLError server trust evaluation error -1202. Causes and solutions for SSL/TLS certificate validation failures."
platforms: ["macos"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# macOS NSURLError Server Trust Evaluation (-1202)

NSURLErrorServerTrustEvaluationFailed (`-1202`) indicates that the server's SSL/TLS certificate failed trust evaluation. This security error prevents the connection to protect against man-in-the-middle attacks.

## What This Error Means

Error code `-1202` maps to `NSURLErrorServerTrustEvaluationFailed` in `NSURLErrorDomain`. The system's URL loading stack rejected the server's certificate chain during TLS handshake. This is a security-critical error that should never be silently bypassed.

## Common Causes

- Self-signed certificate not added to the system trust store
- Certificate has expired or is not yet valid
- Certificate chain is incomplete (missing intermediate CA)
- Hostname does not match the certificate's CN or SAN

## How to Fix

### Add Self-Signed Certificate to Keychain

```bash
# Import certificate to system keychain
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain certificate.pem
```

### Verify Certificate Chain

```bash
# Check certificate details
openssl s_client -connect example.com:443 -showcerts

# Verify certificate expiry
openssl x509 -in certificate.pem -noout -dates
```

### Bypass for Development Only

```swift
// NEVER use in production — for development/testing only
class TrustedSessionDelegate: NSObject, URLSessionDelegate {
    func urlSession(_ session: URLSession,
                    didReceive challenge: URLAuthenticationChallenge,
                    completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
        if challenge.protectionSpace.authenticationMethod == NSURLAuthenticationMethodServerTrust {
            completionHandler(.useCredential, URLCredential(trust: challenge.protectionSpace.serverTrust!))
        }
    }
}
```

### Fix Certificate Configuration

```bash
# Generate properly configured self-signed certificate
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes \
    -subj "/CN=your.domain.com" \
    -addext "subjectAltName=DNS:your.domain.com"
```

## Related Errors

- [NSURLError]({{< relref "/os/macos/nsurlerror" >}}) — General network connection errors
- [Core Foundation Errors]({{< relref "/os/macos/core-foundation" >}}) — Low-level TLS/network errors
- [OSStatus Authentication Errors]({{< relref "/os/macos/osstatus-auth" >}}) — Authentication failures related to certificates
