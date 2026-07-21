---
title: "[Solution] Info.plist Privacy Description Missing"
description: "Fix missing NSUsageDescription keys required for privacy-sensitive APIs in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Info.plist Privacy Description Missing

Missing privacy description strings cause crashes when the app first accesses the protected resource. iOS requires usage descriptions for camera, microphone, location, photos, and other APIs.

## Common Causes
- Privacy key not added to Info.plist for used API
- Key name misspelled in Info.plist
- Description string is empty
- New iOS version requires additional privacy keys

## How to Fix
1. Add the required NSUsageDescription key to Info.plist
2. Provide a clear, specific description string
3. Check Apple documentation for new required keys per iOS version
4. Test all privacy-sensitive features before submission

```xml
<!-- Required keys for common APIs -->
<key>NSCameraUsageDescription</key>
<string>This app uses the camera to scan documents.</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>This app accesses photos to set your profile picture.</string>
<key>NSMicrophoneUsageDescription</key>
<string>This app uses the microphone for voice messages.</string>
```

## Examples
```swift
// Check which permissions are needed:
// Camera: NSCameraUsageDescription
// Photos: NSPhotoLibraryUsageDescription
// Location: NSLocationWhenInUseUsageDescription, NSLocationAlwaysUsageDescription
// Microphone: NSMicrophoneUsageDescription
// Contacts: NSContactsUsageDescription
// Calendar: NSCalendarsUsageDescription
// Reminders: NSRemindersUsageDescription
// Health: NSHealthShareUsageDescription, NSHealthUpdateUsageDescription
// Speech: NSSpeechRecognitionUsageDescription
// Bluetooth: NSBluetoothAlwaysUsageDescription
// Motion: NSMotionUsageDescription
// NFC: NFCReaderUsageDescription
```
