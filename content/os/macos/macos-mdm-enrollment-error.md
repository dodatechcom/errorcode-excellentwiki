---
title: "[Solution] macOS MDM Enrollment Error — Fix Device Management"
description: "Fix macOS MDM enrollment errors with these step-by-step solutions. Includes terminal commands and system settings."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime"]
weight: 319
---

# macOS MDM Enrollment Error — Fix Device Management

MDM enrollment errors prevent a Mac from registering with a Mobile Device Management server, blocking enterprise configuration and policy deployment.

## Common Causes

1. MDM enrollment profile is missing or corrupt
2. Network cannot reach the MDM server
3. Device certificate has expired or is invalid
4. DEP/ABM assignment is not configured
5. Previous enrollment was not properly removed

## How to Fix

### Fix 1: Check Enrollment Profile

```bash
# Check installed MDM profiles
profiles list

# View MDM enrollment details
profiles show -type enrollment

# Remove corrupted profile
profiles remove -identifier com.company.mdm
```

### Fix 2: Verify Network and Server Access

```bash
# Test MDM server connectivity
curl -v https://mdm.example.com/checkin

# Verify certificate chain
openssl s_client -connect mdm.example.com:443

# Check network proxy settings
networksetup -getwebproxy Wi-Fi
networksetup -getsecurewebproxy Wi-Fi
```

### Fix 3: Check Device Certificate

```bash
# View installed certificates
security find-certificate -a -c "MDM" -Z /Library/Keychains/System.keychain

# Verify certificate trust settings
security trust -d /Library/Keychains/System.keychain

# Re-enroll device
sudo profiles install -path /path/to/enrollment.mobileconfig
```

## Related Errors

- [macOS VoiceOver Error](/os/macos/macos-voiceover-error/)
- [NSURLErrorServerCertificateUntrusted](/os/macos/nsurlerror-tls-error/)
- [NSURLErrorCannotConnectToHost](/os/macos/nsurlerror-cannot-connect/)
