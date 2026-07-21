---
title: "[Solution] macOS Installation Language Error -- Installer Language Not Available"
description: "Fix macOS installation language error when the installer language is not available or incorrect. Resolve Mac installer language issues."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Installation Language Error -- Installer Language Not Available

When running the macOS installer, the language selection may not show your preferred language, or the installer may default to a different language.

## Common Causes
- Installer was downloaded for a different region or language
- System locale settings are conflicting with the installer language
- Bootable USB installer was created with a different language
- Recovery Mode is downloading a recovery image with a different default language

## How to Fix
1. Select your preferred language from the language picker on the first installer screen
2. Re-download the installer from App Store with your Apple ID's region settings
3. After installation, change the language in System Preferences > Language & Region

```bash
# Check current system locale
locale

# Set system language from terminal
defaults write NSGlobalDomain AppleLanguages -array "en" "en-US"
```

## Examples

```bash
# Create a bootable installer with a specific language
sudo /Applications/Install\ macOS\ Sequoia.app/Contents/Resources/createinstallmedia --volume /Volumes/USBDrive
```

This error is common when using a bootable installer created on a Mac with different locale settings, when Apple ID region settings do not match your location, or when Internet Recovery downloads a different language variant.
