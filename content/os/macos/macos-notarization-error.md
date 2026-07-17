---
title: "[Solution] macOS App Notarization Error"
description: "Fix app notarization errors on Mac when distributing apps. Resolve 'app needs to be notarized' or notarization submission failures."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# macOS App Notarization Error Fix

Notarization errors occur when distributing apps that haven't been submitted to Apple for automated security checks. macOS blocks notarized apps from running, and `stapler` fails to attach the notarization ticket.

## What This Error Means

Apple requires all apps distributed outside the App Store to be notarized. The notarization process scans for malicious content. If an app isn't notarized, macOS Gatekeeper blocks it from running on macOS 10.14.5 and later.

## Common Causes

- App not submitted to Apple's notary service
- Code signing issues (missing entitlements or hardened runtime)
- App contains unsigned frameworks or libraries
- `xcrun notarytool` submission failed
- Stapler fails because notarization is still processing

## How to Fix

### 1. Check notarization status

```bash
# Check if an app is notarized
spctl -a -v /Applications/MyApp.app
# Should show "accepted, source=Notarized Developer ID"

# Check stapler status
stapler validate /Applications/MyApp.app
```

### 2. Notarize the app

```bash
# Create a ZIP for notarization
ditto -c -k --keepParent MyApp.app MyApp.zip

# Submit for notarization
xcrun notarytool submit MyApp.zip --apple-id "developer@example.com" \
    --team-id "TEAMID" --password "app-specific-password" --wait

# Staple the notarization ticket
xcrun stapler staple MyApp.app
```

### 3. Sign with hardened runtime

```bash
# Sign the app with hardened runtime enabled
codesign --force --options runtime --deep --sign "Developer ID Application: Name (TEAMID)" MyApp.app
```

### 4. Check for signing issues

```bash
# Verify all binaries are signed
codesign --verify --deep --strict /Applications/MyApp.app

# Check for unsigned components
find MyApp.app -name "*.dylib" -exec codesign -dv {} \;
```

## Related Errors

- [Code Signing Error](macos-code-signing-error) — code signing failures
- [Gatekeeper Error](macos-gatekeeper-error) — app blocked by Gatekeeper
- [Xcode Error](macos-xcode-error) — build and archive errors
