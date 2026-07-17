---
title: "[Solution] Gatekeeper App Can't Be Opened Error on Mac"
description: "Fix Gatekeeper errors on macOS when apps cannot be opened, show 'damaged' warnings, or are blocked from running."
platforms: ["macos"]
severities: ["error"]
error-types: ["system-error"]
tags: ["gatekeeper", "app-security", "notarization", "quarantine", "code-signing", "macos"]
weight: 5
---

# Gatekeeper App Can't Be Opened Error on Mac

Apps show "is damaged and can't be opened", "can't be opened because it is from an unidentified developer", or "was not expected to run".

## What This Error Means

Gatekeeper is macOS's security feature that verifies apps are properly signed and notarized by Apple. These errors occur when apps fail verification due to missing signatures, corrupted downloads, or notarization issues.

## Common Causes

- App not signed by identified developer
- App not notarized by Apple
- Download corrupted during transfer
- App modified after signing
- Quarantine attribute on downloaded file
- Enterprise certificates expired

## How to Fix

### Remove Quarantine Attribute

```bash
# Remove quarantine flag from downloaded app
xattr -d com.apple.quarantine /Applications/AppName.app

# Remove from all files in app bundle
xattr -rd com.apple.quarantine /Applications/AppName.app
```

### Allow App in Security Settings

```bash
# Open Security & Privacy settings
open x-apple.systempreferences:com.apple.preference.security

# Go to General tab
# Click "Allow Anyway" next to blocked app message

# Or via command line:
spctl --add --label "approved" /Applications/AppName.app
```

### Temporarily Disable Gatekeeper

```bash
# Check Gatekeeper status
spctl --status

# Disable Gatekeeper (not recommended for regular use)
sudo spctl --master-disable

# Re-enable after installing app
sudo spctl --master-enable
```

### Verify App Signature

```bash
# Check app signature
codesign -v /Applications/AppName.app

# Check detailed signature info
codesign -dv --verbose=4 /Applications/AppName.app

# Check if app is notarized
spctl -a -v /Applications/AppName.app
```

### Re-download the App

```bash
# Clear browser download cache
# Download fresh copy from official source
# Ensure download completes fully before opening
```

## Related Errors

- [SIP Error]({{< relref "/os/macos/macos-sip-error-v2" >}}) — System protection
- [Apple ID Error]({{< relref "/os/macos/macos-apple-id-error-v2" >}}) — Account issues
- [macOS Recovery Error]({{< relref "/os/macos/macos-macos-recovery-error" >}}) — Recovery mode
