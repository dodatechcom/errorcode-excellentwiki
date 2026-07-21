---
title: "[Solution] macOS Notarization Stapler Error -- Stapling Ticket Failed"
description: "Fix macOS notarization stapler error when stapling the notarization ticket to an app fails. Resolve stapler issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Notarization Stapler Error -- Stapling Notarization Ticket Failed

After notarizing an app, the stapler embeds the notarization ticket into the app bundle. When stapling fails, users must have internet access for Gatekeeper to verify the app online.

## Common Causes
- App bundle structure is incorrect
- The notarization ticket has not been processed yet
- The app was not properly signed before stapling
- Apple's notary service has not completed processing
- The stapler encounters a corrupted ticket

## How to Fix
1. Wait for Apple's notarization to fully process (can take a few minutes)
2. Verify the notarization was approved before stapling
3. Ensure the app bundle is correctly structured
4. Re-run the stapler with verbose output
5. Check Apple's notarization service status

```bash
# Staple the notarization ticket
xcrun stapler staple MyApp.app

# Verify the staple
xcrun stapler validate MyApp.app
```

## Examples

```bash
# Check notarization status before stapling
xcrun notarytool info <submission-id> --apple-id developer@example.com --team-id TEAMID --password app-specific-password
```

This error is common when trying to staple before the notarization is fully processed, when the app bundle structure is incorrect, or when Apple's notary service is experiencing delays.
