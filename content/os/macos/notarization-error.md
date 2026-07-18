---
title: "[Solution] macOS Notarization Error — App Not Notarized by Apple"
description: "Fix macOS notarization error: app cannot be opened because it has not been notarized, Apple notarization failed, app requires notarization."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 200
---

# Notarization Error — App Not Notarized by Apple

Fix macOS notarization error: app cannot be opened because it has not been notarized, Apple notarization failed, app requires notarization.

## Common Causes

- App developer has not submitted app for Apple notarization
- Apple notarization service rejected the app submission
- App was built with outdated development tools
- Notarization ticket not embedded in the app bundle

## How to Fix

### 1. Bypass Notarization Check

```bash
# Right-click app → Open → Click Open in dialog
# Or: sudo xattr -rd com.apple.quarantine /path/to/app.app
```

### 2. Check Notarization Status

```bash
stapler validate /path/to/app.app
# Or: spctl -a -v /path/to/app.app
```

### 3. Contact App Developer

```bash
# Ask developer to submit app to Apple for notarization
```

### 4. Adjust Gatekeeper Settings

```bash
# System Settings → Privacy & Security → Allow apps from identified developers
```

## Common Scenarios

This error commonly occurs when:

- App shows 'app is not verified' and cannot be opened
- stapler validate shows 'not notarized' for the app
- Gatekeeper prevents opening app because it lacks notarization
- App opens briefly then shows notarization error dialog

## Prevent It

- Contact app developer to submit for Apple notarization
- Use xattr command to remove quarantine flag for trusted apps
- Keep Gatekeeper enabled for security while allowing identified developers
- Verify app authenticity before bypassing notarization checks
