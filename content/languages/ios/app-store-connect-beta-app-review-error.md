---
title: "[Solution] App Store Connect Beta App Review Error"
description: "Fix TestFlight beta app review and external testing configuration errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# App Store Connect Beta App Review Error

Beta app review errors occur when the build does not meet beta testing requirements, when testing information is incomplete, or when compliance questions are not answered.

## Common Causes
- Build does not have required entitlements for beta
- Missing beta app review information
- Export compliance not answered
- Age rating questions incomplete

## How to Fix
1. Ensure build includes all required entitlements
2. Complete beta app review information in App Store Connect
3. Answer export compliance questions
4. Complete age rating questionnaire

```bash
# Upload build for beta testing:
$ fastlane ios beta

# Or manually via Xcode:
# Product > Archive > Distribute App > App Store Connect
# Select "Upload for Beta App Review"
```

## Examples
```swift
// Required for TestFlight beta:
// 1. Build uploaded to App Store Connect
// 2. Test Information filled in (description, contact, notes)
// 3. Export Compliance answered (uses encryption?)
// 4. Beta App Review Info provided if required
// 5. Add internal/external testers
```
