---
title: "[Solution] macOS SSL Error — SSL Certificate Not Trusted or Handshake Failed"
description: "Fix macOS SSL error: SSL certificate not trusted, SSL handshake failed, HTTPS connections failing, certificate verification errors."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 184
---

# SSL Error — SSL Certificate Not Trusted or Handshake Failed

Fix macOS SSL error: SSL certificate not trusted, SSL handshake failed, HTTPS connections failing, certificate verification errors.

## Common Causes

- System root certificates outdated or missing
- SSL certificate expired or issued by untrusted authority
- Clock incorrect causing certificate validity check to fail
- Third-party app using outdated SSL/TLS library

## How to Fix

### 1. Check System Clock

```bash
date
# Incorrect date/time causes SSL certificates to appear invalid
```

### 2. Update System Keychain Certificates

```bash
security find-certificate -a -c 'Apple' /Library/Keychains/System.keychain
# System Settings → General → Software Update → Install all updates
```

### 3. Test SSL Connection

```bash
curl -vI https://google.com
# Look for SSL handshake errors in output
```

### 4. Fix Certificate Trust Settings

```bash
# Keychain Access → System keychain → Find certificate → Get Info → Trust → Always Trust
```

## Common Scenarios

This error commonly occurs when:

- Browser shows 'This connection is not private' SSL error
- HTTPS websites fail to load with certificate error
- SSL handshake fails when connecting to specific servers
- Apps that use HTTPS show SSL verification errors

## Prevent It

- Keep macOS updated to maintain current root certificate store
- Set correct date and time in System Settings → General → Date & Time
- Update system keychain certificates if SSL errors persist
- Check with website administrator for certificate issues on their end
