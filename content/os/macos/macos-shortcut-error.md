---
title: "[Solution] macOS Shortcuts Error -- Shortcuts App Not Running Automations"
description: "Fix macOS Shortcuts error when Shortcuts app fails to run automations or workflows. Resolve Shortcuts issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Shortcuts Error -- Shortcuts App Not Running Automations

The Shortcuts app on macOS allows you to create and run automated workflows. When shortcuts fail, automations may not trigger, actions may produce errors, or the app may crash.

## Common Causes
- Shortcut contains actions that require specific permissions
- Shortcut references apps or services that are not available
- iCloud sync has not downloaded the shortcut
- macOS version does not support certain shortcut actions
- Shortcut contains deprecated or broken actions

## How to Fix
1. Open the Shortcuts app and check for error indicators on actions
2. Grant required permissions for the shortcut actions
3. Ensure iCloud sync is enabled for Shortcuts
4. Update the shortcut to use current action versions
5. Rebuild the shortcut from scratch if it is corrupted

```bash
# Check Shortcuts errors
log show --predicate 'process == "Shortcuts"' --last 10m

# List shortcuts from terminal
shortcuts list
```

## Examples

```bash
# Run a shortcut from terminal
shortcuts run "My Shortcut Name"
```

This error is common when shortcuts reference apps that are not installed, when permissions are not granted, or when iCloud sync has not downloaded the shortcuts.
