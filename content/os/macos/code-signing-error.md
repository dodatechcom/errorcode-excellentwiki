---
title: "[Solution] macOS Code Signing Error — App Signature Invalid"
description: "Fix macOS code signing error: app signature invalid, code signature verification failed, ad-hoc signing error, signature corrupt."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 201
---

# Code Signing Error — App Signature Invalid

Fix macOS code signing error: app signature invalid, code signature verification failed, ad-hoc signing error, signature corrupt.

## Common Causes

- App code signature corrupted during download or transfer
- Developer certificate used for signing has expired
- Code signature does not match the app binary
- Third-party modification invalidated original signature

## How to Fix

### 1. Verify Code Signature

```bash
codesign -dv --verbose=4 /path/to/app.app
spctl -a -v /path/to/app.app
```

### 2. Re-sign App (Developer Only)

```bash
codesign -f -s 'Developer ID Application: Name' /path/to/app.app
# Requires valid Apple Developer certificate
```

### 3. Remove and Re-download App

```bash
# Delete current copy → Re-download from official source
```

### 4. Check Signature in Keychain Access

```bash
# Keychain Access → Certificates → Verify developer certificate is valid
```

## Common Scenarios

This error commonly occurs when:

- App shows 'code signature invalid' when launching
- codesign reports 'invalid signature' or 'corrupt signature'
- App cannot be opened because its code signature is wrong
- Developer certificate expired causing signature verification failure

## Prevent It

- Download apps only from official sources to preserve signatures
- Contact developer if app signature is invalid or expired
- Re-download app if signature appears corrupted
- Verify code signature before installing downloaded apps
