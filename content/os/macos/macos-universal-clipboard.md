---
title: "[Solution] macOS Universal Clipboard Not Working"
description: "Fix Universal Clipboard not working on Mac when copy/paste between Mac and iPhone/iPad fails or stops working."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["universal-clipboard", "copy-paste", "continuity", "handoff", "clipboard"]
weight: 5
---

# macOS Universal Clipboard Not Working Fix

Universal Clipboard allows you to copy text, images, or files on one Apple device and paste on another. When it fails, the clipboard content is empty or "Paste" is grayed out on the other device.

## What This Error Means

Universal Clipboard uses the same Bluetooth+Wi-Fi infrastructure as Handoff. Clipboard data is temporarily shared between devices via iCloud. Failures indicate connectivity or authentication issues.

## Common Causes

- Wi-Fi or Bluetooth disabled on either device
- Different Apple IDs on Mac and iOS device
- Handoff not enabled
- Bluetooth module stuck in bad state
- Clipboard content too large or unsupported format
- macOS/iOS version incompatibility

## How to Fix

### 1. Verify Handoff is enabled

```bash
# Check on Mac
defaults read com.apple.preference.general Handoff

# Must return 1 (enabled)
# Enable if disabled:
defaults write com.apple.preference.general Handoff -bool true
```

### 2. Toggle Wi-Fi and Bluetooth

```bash
# On Mac: Turn off Wi-Fi and Bluetooth, wait 30 seconds, turn back on
# On iPhone: Toggle Airplane Mode on/off
```

### 3. Sign out and back into iCloud on both devices

```bash
# On Mac: System Preferences → Apple ID → Sign Out → Sign In
# On iPhone: Settings → Apple ID → Sign Out → Sign In
```

### 4. Reset the pasteboard server

```bash
# Kill the pasteboard service to force a restart
killall pbcopy
killall pbpaste
```

## Related Errors

- [Handoff Error](macos-handoff-error) — general Handoff issues
- [AirDrop Error](macos-airdrop-error) — file transfer issues
- [iCloud Error](macos-icloud-error) — iCloud connectivity issues
