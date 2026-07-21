---
title: "[Solution] Provisioning Profile Does Not Include Devices"
description: "Fix device eligibility errors with development provisioning profiles."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Provisioning Profile Does Not Include Devices

Development provisioning profiles are limited to registered devices. If a device is not registered, the app cannot be installed on it.

## Common Causes
- Device UDID not registered in the developer portal
- Profile generated before device was added
- Device limit reached (100 per platform per year)
- Free account limits on device registration

## How to Fix
1. Register the device in the developer portal
2. Regenerate the provisioning profile to include the new device
3. Remove unused devices to stay within limits
4. Use ad-hoc or TestFlight for wider distribution

```swift
// Register device in developer portal:
// 1. Go to https://developer.apple.com/account/resources/devices
// 2. Click "+" to add new device
// 3. Enter device name and UDID

// Find UDID:
// Connect device to Mac > Open Finder > Select device
// Click on serial number to reveal UDID
// Or use: $ xcrun xctrace list devices
```

## Examples
```swift
// Example: Checking if device is in profile
// $ security cms -D -i embedded.mobileprovision | \
//   plutil -extract ProvisionedDevices -o - - | \
//   plutil -convert xml1 -

// Compare UDID list with connected devices
// If your device is missing, re-register and regenerate profile
```
