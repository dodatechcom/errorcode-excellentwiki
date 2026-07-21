---
title: "[Solution] Provisioning Profile Expired"
description: "Fix expired provisioning profile errors in iOS app builds."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Provisioning Profile Expired

An expired provisioning profile prevents code signing and archive submission. Profiles are valid for one year and must be renewed before expiration.

## Common Causes
- Profile not renewed in the developer portal
- Automatic signing did not regenerate the profile
- Profile expired while app was in development
- CI/CD pipeline cached an old profile

## How to Fix
1. Log in to the Apple Developer portal and regenerate the profile
2. Download the new profile and double-click to install
3. For automatic signing, Xcode will regenerate on next build
4. Update CI/CD pipeline to fetch fresh profiles

```swift
// Check profile expiration date:
// $ security cms -D -i YourProfile.mobileprovision | \
//   grep -A1 ExpirationDate

// Regenerate in developer portal:
// https://developer.apple.com/account/resources/profiles/list
// Click the expired profile > Edit > Generate
```

## Examples
```swift
// Example: Script to check profile expiry
#!/bin/bash
PROFILE="$1"
EXPIRY=$(security cms -D -i "$PROFILE" | \
  plutil -extract ExpirationDate raw -)
echo "Profile expires: $EXPIRY"

if [[ $(date -j -f "%Y-%m-%dT%H:%M:%SZ" "$EXPIRY" +%s) < $(date +%s) ]]; then
    echo "WARNING: Profile has expired!"
fi
```
