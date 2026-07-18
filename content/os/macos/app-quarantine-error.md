---
title: "[Solution] macOS App Quarantine Error — App Downloaded from Internet Warning"
description: "Fix macOS app quarantine error: app downloaded from internet warning every launch, cannot remove quarantine extended attribute."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 205
---

# App Quarantine Error — App Downloaded from Internet Warning

Fix macOS app quarantine error: app downloaded from internet warning every launch, cannot remove quarantine extended attribute.

## Common Causes

- Quarantine extended attribute set during download
- Browser or download manager setting quarantine flag on all downloads
- Gatekeeper re-applying quarantine after removal
- Quarantine database preventing app from running without warning

## How to Fix

### 1. Remove Quarantine Attribute

```bash
xattr -d com.apple.quarantine /path/to/app.app
# Remove quarantine flag from downloaded app
```

### 2. Remove Quarantine Recursively

```bash
xattr -rd com.apple.quarantine /path/to/app.app
# Remove quarantine from app and all its contents
```

### 3. Check Quarantine Status

```bash
xattr -l /path/to/app.app
# Look for com.apple.quarantine in extended attributes
```

### 4. Download App from App Store

```bash
# Download from App Store instead of third-party website to avoid quarantine
```

## Common Scenarios

This error commonly occurs when:

- 'App downloaded from internet' warning appears every launch
- App shows quarantine warning even after clicking Open
- xattr command fails to remove quarantine attribute
- Quarantine warning appears for apps installed from DMG files

## Prevent It

- Download apps from App Store to avoid quarantine warnings
- Remove quarantine attribute once for trusted third-party apps
- Move apps to /Applications/ before removing quarantine flag
- Keep Gatekeeper enabled to maintain system security
