---
title: "[Solution] macOS App Sandbox Error -- App Sandboxing Violation"
description: "Fix macOS app sandbox error when a sandboxed app violates sandbox restrictions. Resolve sandbox permission errors on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS App Sandbox Error -- App Sandboxing Violation

The macOS app sandbox restricts what resources an app can access. Sandbox violations occur when the app tries to access files, networks, or system resources without the proper entitlements.

## Common Causes
- App is trying to access files outside its container without entitlements
- Network entitlement is missing for outgoing connections
- App is trying to access hardware (camera, microphone) without entitlement
- File picker did not grant the app access to the selected file
- App is trying to use a service not available in sandbox

## How to Fix
1. Add the required entitlements to the app's entitlements file
2. Use NSOpenPanel to let the user grant file access
3. Enable the appropriate capabilities in Xcode's Signing & Capabilities
4. Test the app with sandbox evaluation tools
5. Review Apple's sandbox entitlement documentation

```bash
# Check sandbox entitlements
codesign -d --entitlements - /Applications/MyApp.app

# Evaluate sandbox restrictions
sandbox-exec -f profile.sb /Applications/MyApp.app/Contents/MacOS/MyApp
```

## Examples

```bash
# View sandbox violations in Console
log show --predicate 'eventMessage contains "sandbox" and eventMessage contains "deny"' --last 10m
```

This error is common when developing sandboxed Mac apps without the correct entitlements, when hard-coded file paths are used instead of NSOpenPanel, or when network entitlements are missing.
