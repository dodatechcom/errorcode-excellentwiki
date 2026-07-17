---
title: "[Solution] Mac Touch ID Error"
description: "Fix Touch ID errors on Mac when fingerprint recognition fails, Touch ID is grayed out, or 'Unable to complete Touch ID enrollment.'"
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Mac Touch ID Error Fix

Touch ID errors include fingerprint not recognized, "Unable to complete Touch ID enrollment," Touch ID grayed out in settings, or Touch ID requiring passcode too frequently.

## What This Error Means

Touch ID uses a Secure Enclave to store fingerprint data. Errors can be software-related (driver, preferences) or hardware-related (sensor failure, Secure Enclave issue).

## Common Causes

- Corrupt Touch ID enrollment data
- Moisture or dirt on the sensor
- macOS update breaking Touch ID driver
- Secure Enclave issue
- Fingerprint changes (cuts, wear)

## How to Fix

### 1. Delete existing fingerprints and re-enroll

```bash
# System Preferences → Touch ID → Remove all fingerprints
# Click "Add Fingerprint" to re-enroll
# Clean the sensor with a lint-free cloth before enrolling
```

### 2. Reset Touch ID

```bash
# Delete Touch ID data
sudo rm -f /var/db/SystemPolicy entitlements

# Delete the Secure Enclave enrollment
sudo tmutil thinlocalsnapshots / 100000000 4
```

### 3. Check Touch ID hardware

```bash
# Run Apple Diagnostics
# Hold D during startup (Intel) or Cmd+D in Recovery (Apple Silicon)
# Check for Touch ID-related error codes
```

### 4. Restart biometric services

```bash
# Restart the biometric agent
killall biometrickitd
```

## Related Errors

- [Face ID Error](macos-face-id-error) — Face ID issues on iPhone/Mac
- [Keychain Error](keychain-error) — keychain unlock with Touch ID
- [Apple ID Error](macos-apple-id-error) — authentication issues
