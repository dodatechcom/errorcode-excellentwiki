---
title: "[Solution] macOS NSURLErrorServerCertificateUntrusted — Fix SSL/TLS Errors"
description: "Fix macOS NSURLErrorServerCertificateUntrusted (-1202) with these step-by-step solutions. Includes terminal commands and system settings."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime"]
weight: 309
---

# macOS NSURLErrorServerCertificateUntrusted — Fix SSL/TLS Errors

NSURLErrorServerCertificateUntrusted (-1202) occurs when the server's SSL/TLS certificate cannot be verified against the system's trusted certificate store.

## Common Causes

1. Server certificate is self-signed or expired
2. Intermediate certificate authority is not installed
3. System clock is incorrect, causing date validation to fail
4. Certificate does not match the hostname
5. App has SSL pinning configured with wrong certificate

## How to Fix

### Fix 1: Verify Server Certificate

```bash
# View certificate details
openssl s_client -connect example.com:443 -showcerts

# Check certificate expiration
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates

# Verify certificate chain
openssl s_client -connect example.com:443 -CApath /etc/ssl/certs
```

### Fix 2: Check System Date and Time

```bash
# View current system time
date

# Check NTP synchronization
systemsetup -getusingnetworktime

# Force time sync
sudo sntp -sS time.apple.com
```

### Fix 3: Implement Certificate Pinning Correctly

```swift
func urlSession(_ session: URLSession, didReceive challenge: URLAuthenticationChallenge,
                completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
    guard let serverTrust = challenge.protectionSpace.serverTrust,
          let certificate = SecTrustGetCertificateAtIndex(serverTrust, 0) else {
        completionHandler(.cancelAuthenticationChallenge, nil)
        return
    }
    let serverCertData = SecCertificateCopyData(certificate) as Data
    if serverCertData == pinnedCertificateData {
        completionHandler(.useCredential, URLCredential(trust: serverTrust))
    } else {
        completionHandler(.cancelAuthenticationChallenge, nil)
    }
}
```

## Related Errors

- [NSURLErrorCannotConnectToHost](/os/macos/nsurlerror-cannot-connect/)
- [NSURLErrorTimedOut](/os/macos/nsurlerror-timedout/)
- [NSURLErrorDNSLookupFailed](/os/macos/nsurlerror-dns-failed/)
