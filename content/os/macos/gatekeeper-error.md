---
title: "[Solution] macOS Gatekeeper Error — 'X is damaged and can't be opened'"
description: "Fix macOS Gatekeeper error: 'is damaged and can't be opened' or 'cannot be opened because Apple cannot check it for malicious software.' Bypass or fix code signing."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 5
---

# Gatekeeper Error — "X is damaged and can't be opened"

A Gatekeeper error occurs when macOS refuses to open an application because it is not notarized by Apple, is missing a valid code signature, or has been corrupted during download. The most common messages are "is damaged and can't be opened" and "cannot be opened because Apple cannot check it for malicious software."

## Description

Gatekeeper is macOS's application verification system. It checks that:

- The app has a valid code signature from an Apple-registered developer
- The app has been notarized by Apple (macOS 10.14.5+)
- The app hasn't been modified since it was signed
- The app isn't flagged in Apple's malware database

Common error messages:

- `"AppName" is damaged and can't be opened. You should move it to the Trash.`
- `"AppName" cannot be opened because Apple cannot check it for malicious software.`
- `"AppName" is from an unidentified developer.`

## Common Causes

- App downloaded from the internet is not notarized by Apple
- Download was corrupted or incomplete
- Quarantine extended attribute is set on the app bundle
- App was modified after being signed (e.g., patching, cracking)

## How to Fix Gatekeeper Errors

### 1. Remove the Quarantine Attribute

```bash
# Remove the quarantine flag that triggers Gatekeeper
xattr -d com.apple.quarantine /Applications/AppName.app

# Or for all apps in a folder
xattr -rd com.apple.quarantine /Applications/AppName.app
```

### 2. Bypass Gatekeeper for a Single App

```bash
# Right-click (or Control-click) the app → Select "Open"
# Click "Open" in the dialog that appears
# This opens the app once and adds a permanent exception
```

### 3. Allow Apps from Anywhere (Not Recommended)

```bash
# Check current Gatekeeper setting
spctl --status

# Disable Gatekeeper entirely
sudo spctl --master-disable

# Re-enable after installing the app
sudo spctl --master-enable
```

### 4. Re-download the App

```bash
# If the app is corrupted:
# 1. Move the app to Trash
# 2. Empty Trash
# 3. Download a fresh copy from the developer's website
# 4. Open with right-click → Open (Step 2)
```

### 5. Sign the App Yourself (for Developers)

```bash
# Ad-hoc signature for local development
codesign --force --deep --sign - /Applications/YourApp.app

# Verify the signature
codesign --verify --verbose /Applications/YourApp.app
```

## Examples

This error commonly occurs when:

- Downloading open-source apps from GitHub releases (not notarized)
- Installing apps from torrent sites
- After macOS update raises the notarization requirements
- Copying an app from a different Mac that modified the signature

## Related Errors

- [SIP Error](sip-error) — System Integrity Protection blocks modifications to Gatekeeper itself
- [Finder Error](finder-error) — "The operation can't be completed" when Gatekeeper blocks an action
- [Keychain Error](keychain-error) — certificate issues preventing code signing
