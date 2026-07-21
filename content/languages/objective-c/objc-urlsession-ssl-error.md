---
title: "Objective-C NSURLSessionDelegate SSL Error"
description: "Fix Objective-C NSURLSession SSL authentication errors when server certificate validation fails."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Server uses self-signed certificate not in trust store
- App Transport Security (ATS) blocks HTTP connections
- Certificate has expired or hostname does not match
- NSURLSession uses default trust evaluation rejecting custom CAs
- Forgetting to call completionHandler with proper disposition

## How to Fix

```objc
// WRONG: Bypassing SSL validation entirely (NEVER do this)
- (void)URLSession:(NSURLSession *)session
    didReceiveChallenge:(NSURLAuthenticationChallenge *)challenge
    completionHandler:(void (^)(NSURLSessionAuthChallengeDisposition, NSURLCredential *))completionHandler {
    completionHandler(NSURLSessionAuthChallengeUseCredential,
        [NSURLCredential credentialForTrust:challenge.protectionSpace.serverTrust]);
}

// CORRECT: Validate certificate properly
- (void)URLSession:(NSURLSession *)session
    didReceiveChallenge:(NSURLAuthenticationChallenge *)challenge
    completionHandler:(void (^)(NSURLSessionAuthChallengeDisposition, NSURLCredential *))completionHandler {
    if ([challenge.protectionSpace.authenticationMethod
        isEqualToString:NSURLAuthenticationMethodServerTrust]) {
        SecTrustRef trust = challenge.protectionSpace.serverTrust;
        if ([self evaluateTrust:trust]) {
            NSURLCredential *credential = [NSURLCredential credentialForTrust:trust];
            completionHandler(NSURLSessionAuthChallengeUseCredential, credential);
            return;
        }
    }
    completionHandler(NSURLSessionAuthChallengeCancelAuthenticationChallenge, nil);
}
```

```enrl
// WRONG: ATS exception too broad
// Info.plist
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>

// CORRECT: Domain-specific exception
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSExceptionDomains</key>
    <dict>
        <key>api.example.com</key>
        <dict>
            <key>NSExceptionRequiresForwardSecrecy</key>
            <false/>
        </dict>
    </dict>
</dict>
```

## Examples

```objc
// Example 1: Custom certificate pinning
- (void)URLSession:(NSURLSession *)session
    didReceiveChallenge:(NSURLAuthenticationChallenge *)challenge
    completionHandler:(void (^)(NSURLSessionAuthChallengeDisposition, NSURLCredential *))completionHandler {
    SecTrustRef serverTrust = challenge.protectionSpace.serverTrust;
    SecCertificateRef certificate = SecTrustGetCertificateAtIndex(serverTrust, 0);
    NSData *remoteCertData = (__bridge_transfer NSData *)SecCertificateCopyData(certificate);
    NSData *localCertData = [NSData dataWithContentsOfFile:
        [[NSBundle mainBundle] pathForResource:@"cert" ofType:@"cer"]];
    
    if ([remoteCertData isEqualToData:localCertData]) {
        NSURLCredential *credential = [NSURLCredential credentialForTrust:serverTrust];
        completionHandler(NSURLSessionAuthChallengeUseCredential, credential);
    } else {
        completionHandler(NSURLSessionAuthChallengeCancelAuthenticationChallenge, nil);
    }
}
```

## Related Errors

- [SSL error](objc-ssl-error) -- SSL/TLS issues
- [URLSession error](objc-nsurlsession-error) -- session problems
