---
title: "[Solution] macOS Gatekeeper — App Blocked Error"
description: "Fix Gatekeeper errors on Mac when apps are blocked from opening because they are from unidentified developers or unsigned."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# macOS Gatekeeper — App Blocked Error Fix

Gatekeeper errors occur when macOS blocks an app from opening because it's from an unidentified developer, not notarized, or has been tampered with. You'll see "'App' can't be opened because it is from an unidentified developer."

## What This Error Means

Gatekeeper is a macOS security feature that verifies apps are from identified developers and haven't been modified. Apps must be notarized by Apple and signed with a valid Developer ID certificate to pass Gatekeeper checks.

## Common Causes

- App downloaded from the internet without proper code signing
- App not notarized by Apple
- App from a developer whose certificate has expired
- Corrupted app bundle or modified binary
- macOS version enforcing stricter notarization requirements

## How to Fix

### 1. Open a blocked app via right-click

```bash
# Right-click (or Control-click) the app in Finder
# Select "Open" from the context menu
# Click "Open" in the confirmation dialog
# This bypasses Gatekeeper for this specific app
```

### 2. Allow the app in Security preferences

```bash
# After trying to open the blocked app
# Open System Preferences → Security & Privacy → General
# Click "Open Anyway" next to the blocked app message
```

### 3. Check the app's code signature

```bash
# Check if the app is signed
codesign -dv --verbose=4 /Applications/MyApp.app

# Check Gatekeeper assessment
spctl -a -v /Applications/MyApp.app
```

### 4. Disable Gatekeeper temporarily (not recommended)

```bash
# Disable Gatekeeper entirely
sudo spctl --master-disable

# Re-enable when done
sudo spctl --master-enable
```

## Related Errors

- [SIP Error](macos-sip-error) — System Integrity Protection blocks
- [Notarization Error](macos-notarization-error) — app notarization failures
- [Code Signing Error](macos-code-signing-error) — code signing issues
