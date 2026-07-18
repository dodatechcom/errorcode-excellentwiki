---
title: "[Solution] macOS Certificate Error — Certificate Revoked or Expired"
description: "Fix macOS certificate error: certificate expired, certificate revoked, Mac cannot verify certificate chain, certificate warnings."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 185
---

# Certificate Error — Certificate Revoked or Expired

Fix macOS certificate error: certificate expired, certificate revoked, Mac cannot verify certificate chain, certificate warnings.

## Common Causes

- SSL certificate has expired and needs renewal
- Certificate revoked by certificate authority
- Intermediate certificate missing from certificate chain
- System keychain does not trust the certificate issuer

## How to Fix

### 1. Check Certificate Status

```bash
# Keychain Access → Find certificate → Get Info → Check expiry and trust settings
```

### 2. Update System Certificates

```bash
security find-certificate -a -c 'DigiCert' /Library/Keychains/System.keychain
# System Settings → Software Update → Install all updates
```

### 3. Trust Certificate Manually

```bash
# Keychain Access → Import certificate → Get Info → Trust → Always Trust
```

### 4. Check Certificate Chain

```bash
# Use Keychain Access to verify complete certificate chain from root to leaf
```

## Common Scenarios

This error commonly occurs when:

- Website shows 'certificate revoked' warning in Safari
- Certificate expires after macOS update and stops working
- SSL certificate from internal server not trusted by Mac
- Email app shows certificate verification error when connecting to server

## Prevent It

- Keep macOS updated to maintain current certificate trust store
- Manually trust certificates for internal servers in Keychain Access
- Contact certificate authority to renew expired certificates
- Verify certificate chain completeness before trusting new certificates
