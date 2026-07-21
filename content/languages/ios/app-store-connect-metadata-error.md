---
title: "[Solution] App Store Connect Metadata Error"
description: "Fix App Store Connect metadata validation errors during app submission."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# App Store Connect Metadata Error

Metadata errors occur when required fields are missing, screenshots are wrong size, or descriptions contain prohibited content.

## Common Causes
- Missing app description or keywords
- Screenshots wrong size for target device
- Privacy policy URL missing
- App category not set correctly

## How to Fix
1. Complete all required metadata fields in App Store Connect
2. Upload screenshots at correct dimensions for each device
3. Add privacy policy URL
4. Set correct app category and subcategory

```bash
# Upload metadata using fastlane:
$ fastlane deliver --skip_screenshots

# Or validate metadata:
$ fastlane run validate_play_store_metadata
```

## Examples
```swift
// Required metadata fields:
// - App Name (max 30 chars)
// - Subtitle (max 30 chars)
// - Description (max 4000 chars)
// - Keywords (max 100 chars)
// - Support URL
// - Marketing URL (optional)
// - Privacy Policy URL
// - Screenshots for each device size
// - App Preview videos (optional)
```
