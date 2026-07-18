---
title: "[Solution] macOS App Store Error — App Store Not Loading"
description: "Fix macOS App Store error: App Store not loading, App Store blank page, App Store connection error or crash."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 190
---

# App Store Error — App Store Not Loading

Fix macOS App Store error: App Store not loading, App Store blank page, App Store connection error or crash.

## Common Causes

- App Store cache corrupted or outdated
- Apple ID authentication issue with App Store
- Network connection preventing App Store from loading
- App Store application bundle corrupted

## How to Fix

### 1. Clear App Store Cache

```bash
rm -rf ~/Library/Caches/com.apple.appstore
rm -rf ~/Library/Cookies/com.apple.appstore*
killall App Store
```

### 2. Sign Out and Back Into Apple ID

```bash
# App Store → Store → Sign Out → Sign In
# Or System Settings → Apple ID → Sign Out → Sign In
```

### 3. Reset App Store Preferences

```bash
defaults delete com.apple.appstore
rm -rf ~/Library/Preferences/com.apple.appstore.plist
sudo shutdown -r now
```

### 4. Check Apple System Status

```bash
# Visit https://www.apple.com/support/systemstatus/ for App Store outages
```

## Common Scenarios

This error commonly occurs when:

- App Store opens to blank white page and never loads
- App Store shows 'Cannot connect to App Store' error
- App Store crashes immediately on launch
- Featured apps and updates not appearing in App Store

## Prevent It

- Keep macOS updated for App Store stability fixes
- Clear App Store cache if it fails to load
- Sign out and back into Apple ID if authentication issues occur
- Check Apple System Status page before extensive troubleshooting
