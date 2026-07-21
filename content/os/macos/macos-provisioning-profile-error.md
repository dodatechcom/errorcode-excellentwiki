---
title: "[Solution] macOS Provisioning Profile Error -- Profile Missing or Expired"
description: "Fix macOS provisioning profile error when the provisioning profile is missing, expired, or invalid. Resolve provisioning issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Provisioning Profile Error -- Profile Missing or Expired

Provisioning profiles link your app to your Apple Developer account and signing certificates. When the profile is missing, expired, or mismatched, the app cannot be signed or distributed.

## Common Causes
- Provisioning profile has expired
- Certificate associated with the profile was revoked
- Bundle identifier does not match the profile
- Profile was generated for a different team
- Xcode automatic signing is not configured correctly

## How to Fix
1. Regenerate the provisioning profile in Apple Developer portal
2. Ensure the bundle identifier matches exactly
3. Download and install the new profile in Xcode
4. Enable automatic signing in Xcode build settings
5. Delete old profiles and let Xcode re-fetch them

```bash
# List installed provisioning profiles
ls -la ~/Library/MobileDevice/Provisioning\ Profiles/

# Remove old profiles
rm -rf ~/Library/MobileDevice/Provisioning\ Profiles/*.mobileprovision
```

## Examples

```bash
# Check profile details
security cms -D -i ~/Library/MobileDevice/Provisioning\ Profiles/*.mobileprovision | plutil -p -
```

This error is common after the 1-year profile expiration, when the Apple Developer certificate is renewed, or when the bundle identifier was changed without updating the profile.
