---
title: "[Solution] macOS Sandbox Restriction Error — App Cannot Access Files"
description: "Fix macOS sandbox restriction error: app cannot access files outside sandbox, sandbox violation in Console, file access denied."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 203
---

# Sandbox Restriction Error — App Cannot Access Files

Fix macOS sandbox restriction error: app cannot access files outside sandbox, sandbox violation in Console, file access denied.

## Common Causes

- App sandbox profile restricting file system access
- App requesting access to files outside its sandbox container
- macOS sandbox enforcement blocking legacy file operations
- App needs specific file access entitlement not granted

## How to Fix

### 1. Check Sandbox Permissions

```bash
# System Settings → Privacy & Security → File and Folders → Enable for app
```

### 2. Grant Full Disk Access

```bash
# System Settings → Privacy & Security → Full Disk Access → Add app
```

### 3. Check App Sandbox Profile

```bash
# App → Contents → _MASReceipt → Check sandbox entitlements
```

### 4. Contact Developer

```bash
# Developer needs to add required entitlements or adjust sandbox profile
```

## Common Scenarios

This error commonly occurs when:

- App shows 'access denied' when trying to open or save files
- App cannot read files from Documents or Desktop folder
- Sandbox violation warnings appear in Console app
- App was working before macOS update but now shows sandbox errors

## Prevent It

- Grant necessary file system permissions in System Settings
- Contact app developer if sandbox restrictions block legitimate access
- Check Privacy settings to ensure app has required file access
- Update app to latest version for improved sandbox compatibility
