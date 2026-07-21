---
title: "[Solution] Objective-C Permission Error"
description: "Permission request errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C Permission Error

Permission request errors.

### Common Causes
Missing plist entry; wrong usage description

### How to Fix
```xml
<key>NSCameraUsageDescription</key>
<string>Camera access needed for photos</string>
```

### Examples
```objc
AVCaptureDevice *device = [AVCaptureDevice defaultDeviceWithMediaType:AVMediaTypeVideo];
if ([device hasPermission]) {
    // access granted
}
```
