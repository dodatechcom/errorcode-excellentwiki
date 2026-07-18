---
title: "[Solution] macOS App Crash Error — App Quits Unexpectedly"
description: "Fix macOS app crash: app quits unexpectedly, crash report generated, app crashes on launch or during use, crash log created."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 206
---

# App Crash Error — App Quits Unexpectedly

Fix macOS app crash: app quits unexpectedly, crash report generated, app crashes on launch or during use, crash log created.

## Common Causes

- App bug or code error causing unexpected termination
- Incompatible app version with current macOS
- Corrupted app preferences or cache files
- System resource exhaustion causing app to be killed

## How to Fix

### 1. Check Crash Reports

```bash
ls -lt ~/Library/Logs/DiagnosticReports/ | head -10
cat ~/Library/Logs/DiagnosticReports/AppName_YYYY-MM-DD.crash
```

### 2. Delete App Preferences

```bash
defaults delete com.developer.appname
rm -rf ~/Library/Caches/com.developer.appname
```

### 3. Reinstall the App

```bash
# Delete app from /Applications/
# Download fresh copy from App Store or developer website
```

### 4. Check System Resources

```bash
top -l 1 -o cpu -n 10
# Check if system is low on memory or CPU
```

## Common Scenarios

This error commonly occurs when:

- App crashes immediately on launch with error dialog
- App quits during specific action like opening a file
- Crash report generated with specific error code
- App works for a while then crashes unexpectedly

## Prevent It

- Keep apps updated to latest compatible versions
- Delete corrupted app preferences if crash happens on startup
- Check crash report for specific error details
- Reinstall app from official source if crashes persist
