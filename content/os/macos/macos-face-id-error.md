---
title: "[Solution] Face ID Error on iPhone/Mac"
description: "Fix Face ID errors when Face ID stops working, shows 'Face Not Recognized,' or fails to authenticate on iPhone or Mac."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["face-id", "biometric", "iphone", "true-depth", "authentication"]
weight: 5
---

# Face ID Error Fix

Face ID errors include "Face Not Recognized," Face ID being disabled, requiring passcode after reboot, or Face ID setup failing with "TrueDepth camera issue."

## What This Error Means

Face ID uses the TrueDepth camera system with infrared dot projector. Errors can stem from camera obstruction, software glitches, or TrueDepth hardware failure.

## Common Causes

- Camera or sensor obscured by case or screen protector
- Face changes (new glasses, facial hair, mask)
- TrueDepth camera hardware failure
- iOS/macOS update breaking Face ID
- Wet or dirty camera sensors

## How to Fix

### 1. Reset Face ID and re-enroll

```bash
# On iPhone: Settings → Face ID & Passcode → Reset Face ID
# Set up Face ID again in good lighting
# Hold device at arm's length during enrollment
```

### 2. Clean the TrueDepth camera

```bash
# Remove any case or screen protector
# Clean the front camera area with a soft, lint-free cloth
# Ensure the camera area is dry
```

### 3. Reset all settings (iPhone)

```bash
# Settings → General → Transfer or Reset iPhone → Reset → Reset All Settings
# This resets Face ID, Wi-Fi, and other settings without erasing data
```

### 4. Check TrueDepth camera

```bash
# Test the TrueDepth camera in another app (selfie, video call)
# Run Apple Diagnostics if on Mac
# If TrueDepth fails, the device may need hardware service
```

## Related Errors

- [Touch ID Error](macos-touch-id-error) — fingerprint sensor issues
- [Apple ID Error](macos-apple-id-error) — authentication failures
- [Camera Error](avfoundation) — camera framework errors
