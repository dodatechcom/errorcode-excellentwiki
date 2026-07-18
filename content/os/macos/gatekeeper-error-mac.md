---
title: "[Solution] macOS Gatekeeper Error — App Blocked from Opening"
description: "Fix macOS Gatekeeper error: app blocked by Gatekeeper, cannot open unidentified developer app, Gatekeeper settings prevent launch."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 199
---

# Gatekeeper Error — App Blocked from Opening

Fix macOS Gatekeeper error: app blocked by Gatekeeper, cannot open unidentified developer app, Gatekeeper settings prevent launch.

## Common Causes

- App not signed with Apple-issued developer certificate
- Gatekeeper set to allow apps only from App Store
- Developer ID certificate expired or revoked
- App downloaded from untrusted source flagged by Gatekeeper

## How to Fix

### 1. Override Gatekeeper for Specific App

```bash
# Right-click app → Open → Click Open in confirmation dialog
# Or: sudo xattr -rd com.apple.quarantine /path/to/app.app
```

### 2. Adjust Gatekeeper Settings

```bash
# System Settings → Privacy & Security → Security → Allow apps from: App Store and identified developers
```

### 3. Check App Signature

```bash
codesign -dv --verbose=4 /path/to/app.app
# Look for 'Signature=' and 'Authority=' in output
```

### 4. Temporarily Disable Gatekeeper (Not Recommended)

```bash
sudo spctl --master-disable
# Re-enable after installation: sudo spctl --master-enable
```

## Common Scenarios

This error commonly occurs when:

- Double-clicking app shows 'App is damaged and can't be opened'
- Gatekeeper blocks app with 'unidentified developer' warning
- Right-click → Open shows no override option
- Gatekeeper blocks app even after allowing unidentified developers

## Prevent It

- Keep Gatekeeper enabled for system security
- Only override Gatekeeper for apps from trusted sources
- Check app code signature before manually bypassing Gatekeeper
- Re-enable Gatekeeper after installing unverified apps
