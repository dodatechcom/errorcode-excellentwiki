---
title: "[Solution] macOS Launch Services Errors (-10810, -10811)"
description: "Fix macOS Launch Services errors -10810 and -10811. Causes and solutions for application launch and registration failures."
platforms: ["macos"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# macOS Launch Services Errors (-10810, -10811)

Launch Services errors occur when macOS cannot launch, register, or manage applications. These errors affect `open`, `NSWorkspace`, and automated app launching.

## What This Error Means

- `-10810 (kLSApplicationNotRunning)` — The application is not running or cannot be found
- `-10811 (kLSApplicationNotFound)` — No application found that matches the requested criteria

These codes indicate the Launch Services database is stale, the application bundle is damaged, or the system cannot resolve the application to launch.

## Common Causes

- Launch Services database is corrupted or stale
- Application bundle is damaged or missing Info.plist
- Application was moved or deleted without proper deregistration
- macOS quarantine flag blocking unsigned applications

## How to Fix

### Rebuild Launch Services Database

```bash
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -kill -r -domain local -domain system -domain user
```

### Reset Launch Services for Specific App

```bash
# Deregister the application
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -u "/Applications/AppName.app"

# Re-register the application
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -f "/Applications/AppName.app"
```

### Remove Quarantine Flag

```bash
# Check quarantine status
ls -lO /Applications/AppName.app

# Remove quarantine
xattr -d com.apple.quarantine /Applications/AppName.app
```

### Verify Application Bundle

```bash
# Check Info.plist exists and is valid
plutil -lint /Applications/AppName.app/Contents/Info.plist

# Verify code signature
codesign --verify --deep /Applications/AppName.app
```

## Related Errors

- [Cocoa Error Codes]({{< relref "/os/macos/cocoa-error" >}}) — Foundation framework errors
- [OSStatus Authentication Errors]({{< relref "/os/macos/osstatus-auth" >}}) — Authentication failures that may prevent app launch
- [CloudKit Errors]({{< relref "/os/macos/cloudkit-error" >}}) — CloudKit errors in apps using iCloud
