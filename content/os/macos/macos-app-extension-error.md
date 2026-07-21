---
title: "[Solution] macOS App Extension Error -- App Extension Crash or Failure"
description: "Fix macOS app extension error when Today widgets, share extensions, or other extensions fail. Resolve app extension issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS App Extension Error -- App Extension Crash or Failure

macOS app extensions include Today widgets, Share extensions, Action extensions, and Finder sync extensions. When they fail, they may crash on launch, not appear in the system, or consume excessive resources.

## Common Causes
- Extension bundle identifier does not match the host app
- Extension is using APIs not available in the extension sandbox
- Extension container has corrupted state
- Host app has been updated but extension was not
- Extension memory limit is exceeded

## How to Fix
1. Verify the extension's bundle identifier and entitlements
2. Check the extension sandbox restrictions
3. Rebuild the extension and host app together
4. Delete the extension container and reinstall
5. Check Console.app for extension crash logs

```bash
# Find extension containers
ls -la ~/Library/Containers/ | grep -i extension

# Check extension crash reports
ls -lt ~/Library/Logs/DiagnosticReports/ | grep -i extension
```

## Examples

```bash
# View extension logs
log show --predicate 'subsystem == "com.apple.extensions"' --last 10m
```

This error is common when the extension uses APIs that are restricted in the extension sandbox, when the host app and extension are out of sync, or when the extension container has corrupted state.
