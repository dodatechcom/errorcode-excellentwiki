---
title: "[Solution] Code Signing Error: Library Validation Failed"
description: "Fix library validation errors in macOS app code signing."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Code Signing Error: Library Validation Failed

Library validation checks that all loaded libraries are signed by the same team as the main app. Third-party libraries may fail this validation.

## Common Causes
- Third-party framework signed by different team
- Dynamically loaded libraries not signed by your team
- Plugin bundles from external sources
- Debug builds loading unsigned libraries

## How to Fix
1. Re-sign third-party libraries with your team certificate
2. Disable library validation if legally permissible
3. Ensure all embedded frameworks are signed by your team
4. For development, use the disable-library-validation entitlement

```swift
// For development, add entitlement:
// com.apple.security.cs.disable-library-validation = true

// For production, re-sign all frameworks:
// $ codesign --force --sign "iPhone Distribution: Your Team" \
//   Frameworks/ThirdParty.framework

// Or use embed-in-framework approach for CocoaPods
```

## Examples
```swift
// Example: Re-signing all frameworks
// Script to re-sign all embedded frameworks:
#!/bin/bash
APP="$1"
SIGNING_IDENTITY="iPhone Distribution: Your Team (TEAMID)"

for framework in "$APP"/Frameworks/*.framework; do
    codesign --force --sign "$SIGNING_IDENTITY" "$framework"
done

codesign --force --sign "$SIGNING_IDENTITY" "$APP"
```
